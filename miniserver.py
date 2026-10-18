# -*- coding: utf-8 -*-
"""零依赖 WSGI 开发服务器（仅用 Python 标准库）。

为什么不用 Flask/waitress：
    本工程的目标是「拷贝到任何一台有 Python 的机器就能跑」，比赛现场不能依赖
    联网装包。整个后端只用标准库实现，因此这里手写一个够用的 WSGI 容器。

app 本身是一个标准 WSGI application，所以将来要换成 gunicorn / waitress /
werkzeug，把本文件替换掉即可，业务代码不用动。
"""

from __future__ import annotations

import socket
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote


class _Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    server_version = "LvJian/2.0"
    app = None  # 由 serve() 注入

    # ---- 日志：保持精简，避免刷屏 ----
    def log_message(self, fmt, *args):  # noqa: D102
        if self.server.verbose:  # type: ignore[attr-defined]
            sys.stderr.write("  %s - %s\n" % (self.address_string(), fmt % args))

    # ---- 读取请求体：兼容 Content-Length 与 chunked ----
    def _read_body(self) -> bytes:
        if self.headers.get("Transfer-Encoding", "").lower() == "chunked":
            chunks = []
            while True:
                line = self.rfile.readline().strip()
                if not line:
                    break
                try:
                    size = int(line.split(b";")[0], 16)
                except ValueError:
                    break
                if size == 0:
                    self.rfile.readline()
                    break
                chunks.append(self.rfile.read(size))
                self.rfile.readline()
            return b"".join(chunks)
        length = int(self.headers.get("Content-Length") or 0)
        return self.rfile.read(length) if length else b""

    # ---- 把请求交给 WSGI app ----
    def _dispatch(self, method: str) -> None:
        body = self._read_body()
        path, _, query = self.path.partition("?")
        environ = {
            "REQUEST_METHOD": method,
            "SCRIPT_NAME": "",
            "PATH_INFO": unquote(path),
            "QUERY_STRING": query,
            "SERVER_NAME": self.server.server_address[0],  # type: ignore[attr-defined]
            "SERVER_PORT": str(self.server.server_address[1]),  # type: ignore[attr-defined]
            "SERVER_PROTOCOL": self.protocol_version,
            "REMOTE_ADDR": self.client_address[0],
            "CONTENT_TYPE": self.headers.get("Content-Type", ""),
            "CONTENT_LENGTH": str(len(body)),
            "wsgi.version": (1, 0),
            "wsgi.url_scheme": "http",
            "wsgi.input": _BytesReader(body),
            "wsgi.errors": sys.stderr,
            "wsgi.multithread": True,
            "wsgi.multiprocess": False,
            "wsgi.run_once": False,
        }
        for key, value in self.headers.items():
            name = "HTTP_" + key.upper().replace("-", "_")
            if name not in ("HTTP_CONTENT_TYPE", "HTTP_CONTENT_LENGTH"):
                environ[name] = value

        status_line: list[str] = []
        headers_out: list[tuple[str, str]] = []

        def start_response(status, response_headers, exc_info=None):
            status_line.append(status)
            headers_out.extend(response_headers)

        chunks = self.app(environ, start_response)
        try:
            payload = b"".join(chunks)
        finally:
            close = getattr(chunks, "close", None)
            if close:
                close()

        code = int(status_line[0].split(" ", 1)[0]) if status_line else 500
        self.send_response(code)
        sent = set()
        for key, value in headers_out:
            low = key.lower()
            if low in ("connection", "transfer-encoding"):
                continue
            self.send_header(key, value)
            sent.add(low)
        if "content-length" not in sent:
            self.send_header("Content-Length", str(len(payload)))
        self.send_header("Connection", "close")
        self.end_headers()
        if method != "HEAD" and payload:
            self.wfile.write(payload)

    def do_GET(self):        self._dispatch("GET")        # noqa: E704
    def do_HEAD(self):       self._dispatch("HEAD")       # noqa: E704
    def do_POST(self):       self._dispatch("POST")       # noqa: E704
    def do_PUT(self):        self._dispatch("PUT")        # noqa: E704
    def do_DELETE(self):     self._dispatch("DELETE")     # noqa: E704
    def do_OPTIONS(self):    self._dispatch("OPTIONS")    # noqa: E704


class _BytesReader:
    """最小化的 wsgi.input 实现。"""

    def __init__(self, data: bytes):
        self._data = data
        self._pos = 0

    def readable(self) -> bool:
        return True

    def read(self, size: int = -1) -> bytes:
        if size is None or size < 0:
            chunk = self._data[self._pos:]
            self._pos = len(self._data)
            return chunk
        chunk = self._data[self._pos:self._pos + size]
        self._pos += len(chunk)
        return chunk

    def readline(self) -> bytes:
        idx = self._data.find(b"\n", self._pos)
        if idx < 0:
            return self.read()
        line = self._data[self._pos:idx + 1]
        self._pos = idx + 1
        return line


class _Server(ThreadingHTTPServer):
    """ThreadingHTTPServer 本身已是线程化实现，这里只调参数。"""

    daemon_threads = True
    allow_reuse_address = True


def serve(app, host: str = "127.0.0.1", port: int = 8899, verbose: bool = False) -> None:
    handler = type("BoundHandler", (_Handler,), {"app": staticmethod(app)})
    httpd = _Server((host, port), handler)
    httpd.verbose = verbose  # type: ignore[attr-defined]
    httpd.serve_forever()
