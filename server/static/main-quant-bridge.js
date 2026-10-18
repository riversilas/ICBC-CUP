/* Main-root quantification UI adapter. No model or rating recalculation. */
function radarGeometry(n, cx, cy, R) {
  // 第 i 根轴的角度：从正上方开始顺时针
  return Array.from({length: n}, (_, i) => {
    const a = -Math.PI / 2 + i * 2 * Math.PI / n;
    return [cx + R * Math.cos(a), cy + R * Math.sin(a)];
  });
}

function radarPolygon(scores, pts) {
  return scores.map((s, i) => {
    const r = Math.max(0, Math.min(100, s === null ? 0 : s)) / 100;
    const cx = 260, cy = 235;
    return [cx + (pts[i][0] - cx) * r, cy + (pts[i][1] - cy) * r];
  });
}

function renderRadar(cur, prev, curYear, prevYear) {
  const n = cur.length;
  const cx = 260, cy = 235, R = 148;
  const pts = radarGeometry(n, cx, cy, R);
  const toPath = poly => poly.map((p, i) => `${i ? 'L' : 'M'}${p[0].toFixed(1)},${p[1].toFixed(1)}`).join(' ') + ' Z';

  // 背景网：4 圈 + n 条轴线
  let grid = '';
  [0.25, 0.5, 0.75, 1].forEach(k => {
    const ring = radarGeometry(n, cx, cy, R * k);
    grid += `<polygon points="${ring.map(p => p.join(',')).join(' ')}"
      fill="none" stroke="#dbe5d5" stroke-width="1"/>`;
  });
  pts.forEach(p => {
    grid += `<line x1="${cx}" y1="${cy}" x2="${p[0].toFixed(1)}" y2="${p[1].toFixed(1)}"
      stroke="#dbe5d5" stroke-width="1"/>`;
  });

  // 轴标签 + 数值（含与上年的变化箭头，突出塌陷/外扩）
  let labels = '';
  cur.forEach((d, i) => {
    const a = -Math.PI / 2 + i * 2 * Math.PI / n;
    const lx = cx + (R + 34) * Math.cos(a);
    const ly = cy + (R + 30) * Math.sin(a);
    const anchor = Math.abs(Math.cos(a)) < 0.25 ? 'middle'
                 : (Math.cos(a) > 0 ? 'start' : 'end');
    const val = d.available ? `${d.score}` : '—';
    const color = d.available ? '#1f6b4a' : '#a9b5ac';
    // 数值变化：增加红、减少绿；不解释为好坏
    let delta = '';
    const p = prev && prev[i] ? prev[i] : null;
    if (p && p.available && d.available) {
      const diff = d.score - p.score;
      if (Math.abs(diff) >= 0.05) {
        const up = diff > 0;
        delta = `<text x="${lx.toFixed(0)}" y="${(ly + 30).toFixed(0)}"
          text-anchor="${anchor}" font-size="11" data-change-sign="${up ? 'positive' : 'negative'}"
          fill="${up ? '#b4453a' : '#177245'}">${up ? '▲' : '▼'}${Math.abs(diff).toFixed(1)}</text>`;
      }
    }
    labels += `<text x="${lx.toFixed(0)}" y="${ly.toFixed(0)}" text-anchor="${anchor}"
      font-size="12.5" font-weight="600" fill="#2c4438">${E(d.short)}</text>
      <text x="${lx.toFixed(0)}" y="${(ly + 15).toFixed(0)}" text-anchor="${anchor}"
      font-size="11.5" fill="${color}">${val}</text>${delta}`;
  });

  // 缺失点不补零；仅全部可用时闭合，否则只画有效相邻线段。
  function series(items,color,dash,fill) {
    if(!items||items.length!==n)return '';
    const points=items.map((d,i)=>d&&d.available&&Number.isFinite(d.score)?radarPolygon(items.map(x=>x&&x.available?x.score:0),pts)[i]:null);
    let out='';
    if(points.every(Boolean))out+=`<path d="${toPath(points)}" fill="${fill}" stroke="${color}" stroke-width="2" stroke-dasharray="${dash}"/>`;
    else points.forEach((p,i)=>{const q=points[(i+1)%n];if(p&&q)out+=`<line x1="${p[0]}" y1="${p[1]}" x2="${q[0]}" y2="${q[1]}" stroke="${color}" stroke-width="2" stroke-dasharray="${dash}"/>`;});
    points.forEach((p,i)=>{if(p)out+=`<circle cx="${p[0]}" cy="${p[1]}" r="4" fill="${color}"><title>${E(items[i].short)}: ${items[i].score}</title></circle>`;});
    return out;
  }
  const prevPoly=prev&&prev.length===n;
  const shapes=series(prev,'#7a8f9b','4 3','rgba(120,140,155,.10)')+series(cur,'#1f6b4a','','rgba(31,107,74,.18)');

  const legend = `<div class="radar-legend">
    ${prevPoly ? `<span><i style="background:#7a8f9b"></i>${prevYear} 年（虚线）</span>` : ''}
    <span><i style="background:#1f6b4a"></i>${curYear} 年（实线）</span>
    <span class="muted">红色▲增加 · 绿色▼减少；分差不等于信用风险变化</span>
  </div>`;

  return `<svg viewBox="0 0 520 490" width="520" height="490" role="img"
      aria-label="五维碳表现雷达图">
    ${grid}${shapes}${labels}
    </svg>${legend}`;
}

function radarDimList(cur, prev) {
  const pv = {};
  (prev || []).forEach(x => pv[x.key] = x);
  return '<div class="dim-list">' + cur.map(d => {
    const val = d.value === null ? '—'
      : `${d.value}${['gCO₂/kWh', '%'].includes(d.unit) ? ' ' + d.unit : d.unit}`;
    const sc = d.available ? `${d.score} 分` : '待补数据';
    const p = pv[d.key];
    let trend = '';
    if (p && p.available && d.available) {
      const diff = d.score - p.score;
      const up = diff > 0;
      trend = `<span style="color:${up ? '#b4453a' : '#177245'};font-weight:600">
        ${up ? '▲' : '▼'} ${Math.abs(diff).toFixed(1)}</span>`;
    }
    return `<div class="dim-row${d.available ? '' : ' na'}">
      <span class="nm">${E(d.label)}</span>
      <span class="vl">${sc}</span>
      <span class="nt">${d.value !== null ? '原始值 ' + val + '　' : ''}${trend}${trend ? '　' : ''}${E(d.note || d.desc)}</span>
    </div>`;
  }).join('') + '</div>';
}

function radarVerdict(v) {
  if (!v) return '';
  const cls = v.rating.startsWith('AAA') || v.rating.startsWith('AA') ? 'g'
            : (v.rating.startsWith('A') || v.rating === 'B+' ? 'i' : 'r');
  return `<div class="verdict">
    <div class="verdict-head">
      <span class="tag ${cls}" style="font-size:14px;padding:4px 12px">${v.rating} 级</span>
      <b>${v.label}</b>
      <span class="muted">原模型人工说明</span>
    </div>
    <div class="verdict-action">📌 ${v.action}</div>
    <div class="verdict-reason">${v.reason}</div>
  </div>`;
}

function showRadar() {
  const h = document.getElementById('d_radar_holder');
  if (!RADAR) return;
  if (h.style.display === 'none') {
    document.getElementById('d_radar').innerHTML =
      renderRadar(RADAR.cur, RADAR.prev, RADAR.curYear, RADAR.prevYear);
    document.getElementById('d_verdict').innerHTML = radarVerdict(RADAR.verdict);
    document.getElementById('d_radar_gaps').innerHTML =
      radarDimList(RADAR.cur, RADAR.prev) +
      (RADAR.missing.length
        ? `<div class="notice"><b>数据缺口（${RADAR.missing.length} 个维度）：</b>
           ${RADAR.missing.join('、')}。这几根轴在图中留空，不与缺失点闭合，
           <b>不代表该维度得 0 分</b>——平台不臆测缺失数据。</div>`
        : `<div class="notice good">
           <b>五项输入可计算。</b>原报告与分类仍待核对；数值齐备不等于已核验。请展开“数据来源与待核事项”查看来源。</div>`);
    h.style.display = 'block';
    h.scrollIntoView({behavior:'smooth', block:'center'});
  } else {
    h.style.display = 'none';
  }
}



let mainQuantRequest = 0;
let RADAR = null;
const MAIN_QUANT_PEER_CODES = ['601991', '600023', '600886'];

// Display mappings only: keep API values and the scoring algorithm unchanged.
function quantStatus(value) {
  return ({verified:'台账标记已核实，原文未独立复核', unverified:'未核验',
    partial:'资料不完整，原文未独立复核', disclosed:'台账记载已披露，原文未独立复核',
    estimated:'估算数据，未独立核验', demo:'演示数据，未核验',
    not_disclosed:'台账未取得相关资料', unavailable:'资料不足', missing:'资料不足',
    attachment_unverified:'附件数据，未独立核验'})[value] || '台账状态未说明，原文未独立复核';
}

function quantRadar(items) {
  const specs = {
    intensity:{short:'排放强度', label:'① 排放强度', desc:'按固定标尺展示度电排放强度，不用于判断机组技术水平。'},
    trend:{short:'强度变化', label:'② 强度变化趋势', desc:'排放强度年度变化率；负值为下降，正值为上升。'},
    green_capex:{short:'环保节能投入', label:'③ 环保节能投入占比', desc:'环保节能投入占资本开支的比例，不等于已核实的低碳转型资本支出。'},
    structure:{short:'清洁装机占比', label:'④ 清洁能源装机占比', desc:'沿用台账装机口径，不等于非化石能源发电量占比。'},
    carbon_compliance:{short:'相对参考强度偏离', label:'⑤ 相对参考强度偏离',
      desc:'相对当前模型年度参考强度的偏离；参考值由模型配置给出，不推定实际配额盈缺。',
      note:'正值表示强度低于演示参考值，负值表示高于；不代表配额结余、合规状态或现金流收益。'}
  };
  return (items || []).map(d => {
    const spec = specs[d.key];
    if (!spec) return {...d, short:'其他观测', label:'其他观测', desc:'口径待核对', note:'口径待核对'};
    return {...d, ...spec, note:spec.note || ((d.key === 'structure' || d.key === 'green_capex') ? spec.desc : (d.note || spec.desc))};
  });
}

function quantMethodRows(sm,k){const rows=[['模型版本',E(k.model_version||sm.model_version)],['排放强度',E(sm.intensity)],['强度趋势',E(sm.trend)],['结构口径',E(sm.structure_raw)],...((sm.dims||[]).map(d=>[E(d.label.replace('碳合规与边际收益','相对参考强度偏离')),E(d.formula)])),['综合方法',E(sm.composite)],['实际权重',Object.entries(k.weights_applied||{}).map(([key,w])=>E(({intensity:'强度',trend:'趋势',green_capex:'投入',structure:'结构',carbon_compliance:'参考偏离'})[key]||key)+': '+(w*100).toFixed(0)+'%').join('、')],['缺失处理',E(sm.missing_rule)],['评级分段',E(sm.rating_rule)]];return rows;}

function quantEvidence(items) {
  const labels = {'scope1_tco2 / scope2_tco2':'scope1直接排放 / scope2外购能源排放',
    scope1_tco2:'scope1直接排放', scope2_tco2:'scope2外购能源排放', power_gen_gwh:'发电量',
    intensity:'排放强度', clean_energy_share:'清洁能源占比', '企业自报排放强度':'企业自报排放强度（另口径）'};
  return (items || []).filter(x => Object.prototype.hasOwnProperty.call(labels, x.field)).map(x => {
    const note = x.field === 'clean_energy_share' ? '沿用台账口径参与结构计算，装机占比与发电量占比不可互换。' : x.note;
    return '<div class="evi"><b>' + E(labels[x.field]) + '</b> — ' + E(x.source || '来源未注明') + '<p>' + E(note || '') + ' 原文数值及边界未独立复核。</p></div>';
  }).join('') || '<p>暂无可展示的来源条目，原文未独立复核。</p>';
}

const originalQuantMarkup = `
  <div id="d_unavailable" class="card" style="display:none"><h2>碳表现概览</h2>
    <span class="badge neutral">暂不评级</span><p id="d_na_reason"></p>
    <p>当前资料不足，暂不生成评分。可继续查看已有数据与来源。</p></div>
  <div id="d_available" style="display:none">
    <section class="card"><h2>碳表现概览 <span id="d_quant_year" class="muted"></span></h2>
      <div class="grid">
        <div class="kpi"><div class="score-big" id="d_score_big">—</div><div class="l" id="d_rating_label">碳表现参考分 · 五维等权</div></div>
        <div class="kpi"><div class="v" id="d_ci">—</div><div class="l">排放强度 gCO₂/kWh</div><div class="bar"><i id="d_ci_bar"></i></div></div>
        <div class="kpi"><div class="v" id="d_dev">—</div><div class="l">相对年度参考强度偏离</div></div>
        <div class="kpi"><div class="v" id="d_tau">—</div><div class="l" id="d_tau_label">强度变化率（负值为下降）</div></div>
        <div class="kpi"><div class="v" id="d_rho">—</div><div class="l">清洁能源装机占比</div></div>
      </div>
      <p>五项名义权重各20%；缺项时按模型重归一化。综合分与雷达使用同一组分项结果，等级由综合分计算。</p>
    </section>
    <section class="card"><div class="card-head"><h2>五维参考评分 <span class="muted">不是信用评级</span></h2>
      <button type="button" class="sec" style="font-size:12px;padding:6px 14px" onclick="showRadar()">查看 / 收起雷达图</button></div>
      <div id="d_radar_holder" style="display:none;margin-top:4px"><div class="radar-wrap"><div id="d_radar"></div></div><div id="d_verdict"></div><div id="d_radar_gaps"></div></div>
    </section>
  </div>
  <details class="card"><summary>数据可信度 · 查看覆盖情况与年度</summary><div class="grid" style="margin-top:12px">
    <div class="kpi"><div class="v" id="d_grade">—</div><div class="l">台账可信度等级（不是认证）</div></div>
    <div class="kpi"><div class="v" id="d_cov">—</div><div class="l">数据覆盖度</div></div>
    <div class="kpi"><div class="v sm" id="d_years">—</div><div class="l">参与计算的年度</div></div>
    <div class="kpi"><div class="v sm" id="d_status">—</div><div class="l">资料状态</div></div></div><p id="d_note"></p></details>
  <details class="card"><summary>计算方法 · 公式、参数与使用限制</summary><div class="formula" id="d_method"></div></details>
  <details class="card" id="d_sources_details"><summary>数据来源与待核事项 · 原文未独立复核</summary><div id="d_evidence"></div><div id="d_ledger_sources"></div></details>
  <details class="card"><summary>同年度演示对照 · 排放强度由低到高</summary>
    <p id="d_peer_note">正在载入对照数据…</p><div class="tbl-wrap"><table id="d_peers"><thead><tr><th>代码</th><th>企业</th><th>年度</th><th>排放强度 gCO₂/kWh</th><th>资料性质</th></tr></thead><tbody></tbody></table></div></details>
  <details class="card"><summary>公开报告索引 · 可打开原文自行核对</summary><p>索引不代表原文已核验，也不保证与当前年度观测一一对应。</p><div id="d_reports"></div></details>`;

async function loadMainQuantBridge() {
  const host = $('mainQuantBridge');
  if (!host || !state.profile) return;
  const token = ++mainQuantRequest, code = state.profile.code;
  RADAR = null;
  host.innerHTML = '<div class="loading">载入碳表现量化…</div>';
  const current = () => token === mainQuantRequest && state.profile && state.profile.code === code;
  const put = (id, value) => {const el = $(id); if (el) el.textContent = value == null ? '—' : value;};
  const percent = value => value == null ? '—' : fmt(value) + '%';
  try {
    const res = await fetch('/api/main-quant/' + code), d = await res.json();
    if (!current()) return;
    if (!res.ok || !d.carbon) {
      host.innerHTML = '<section class="card"><h2>碳表现概览</h2><span class="badge neutral">暂不评级</span><p>该企业缺少本模型所需的同口径数据，不能与已完成计算的企业直接排名。可继续查看已有数据与来源。</p><p>数据仅供演示，原文未独立复核。本区评分不纳入当前参考报告；报告仅包含企业碳画像及已保存的补充信息。</p></section>';
      return;
    }
    const k = d.carbon;
    host.innerHTML = '<div class="intro">' + E(d.name) + ' · 碳表现概览</div><div class="notice"><b>演示数据 · 原文未独立复核</b><p>' + E(quantStatus(k.disclosure_status)) + '；年度、组织边界与气体口径尚待核对，不能视为已确认可比。</p><p>本区评分不纳入当前参考报告；报告仅包含企业碳画像及已保存的补充信息。</p></div>' + originalQuantMarkup;
    $('d_unavailable').style.display = k.available ? 'none' : 'block';
    $('d_available').style.display = k.available ? 'block' : 'none';
    if (!k.available) put('d_na_reason', '未取得本模型所需的可复算资料，暂不评级。');
    put('d_quant_year', k.year == null ? '年度未确认' : k.year + '年');
    put('d_score_big', k.carbon_score == null ? '暂不评级' : fmt(k.carbon_score) + '分');
    put('d_rating_label', '碳表现参考分 · 五维等权' + (k.rating ? '（' + k.rating + '）' : ''));
    put('d_ci', fmt(k.ci_g_per_kwh)); put('d_dev', percent(k.deviation_vs_baseline_pct));
    put('d_tau', percent(k.change_rate_pct)); put('d_rho', percent(k.clean_energy_share_pct));
    put('d_tau_label', (k.change_rate_basis || '强度变化率') + '（负值为下降）');
    // Shared sign semantics; CSS supplies theme-aware colours.
    [['d_dev', k.deviation_vs_baseline_pct], ['d_tau', k.change_rate_pct]].forEach(([id, value]) => {
      const el = $(id);
      el.style.removeProperty('color');
      el.dataset.changeSign = value == null || !Number.isFinite(Number(value)) ? 'neutral' : Number(value) > 0 ? 'positive' : Number(value) < 0 ? 'negative' : 'neutral';
    });
    $('d_ci_bar').style.width = Math.max(0, Math.min(100, k.score_intensity || 0)) + '%';
    put('d_grade', k.confidence_grade); put('d_cov', percent(k.data_coverage));
    put('d_years', (k.years_used || []).join('、') || '年度未确认'); put('d_status', quantStatus(k.disclosure_status));
    put('d_note', '可信度与评分分开显示，不参与加分；覆盖度不代表原文已核验。');
    const cur = quantRadar(k.radar), prev = quantRadar(k.radar_prev);
    RADAR = {cur, prev, curYear:k.year, prevYear:k.radar_prev_year, verdict:null, missing:cur.filter(x => !x.available).map(x => x.label)};
    $('d_method').innerHTML = table(['核算项', '计算口径与限制'], quantMethodRows(d.scoring_method || {}, k));
    $('d_evidence').innerHTML = quantEvidence(d.evidence);
    $('d_ledger_sources').innerHTML = '<h3>台账列示来源（未独立复核）</h3>' + (k.sources || []).map(s => '<p>' + E(s) + '</p>').join('');
    $('d_reports').innerHTML = (d.reports || []).map(x => source(x.title, /^https?:/.test(x.url) ? x.url : 'https://static.cninfo.com.cn/' + x.url)).join('<br>') || '<p>暂无报告索引。</p>';

    // Each peer comes from exactly the same endpoint and carbon field as the KPI.
    // Individual failures are kept visible and cannot make the core panel disappear.
    const peerResults = await Promise.all(MAIN_QUANT_PEER_CODES.map(async peerCode => {
      if (peerCode === String(code)) return {code:peerCode, data:d};
      try {
        const response = await fetch('/api/main-quant/' + peerCode);
        if (!response.ok) return {code:peerCode, error:true};
        return {code:peerCode, data:await response.json()};
      } catch (_) {return {code:peerCode, error:true};}
    }));
    if (!current()) return;
    const rows = peerResults.filter(x => x.data && x.data.carbon && k.year != null &&
      x.data.carbon.year === k.year && x.data.carbon.available && Number.isFinite(x.data.carbon.ci_g_per_kwh))
      .sort((a, b) => a.data.carbon.ci_g_per_kwh - b.data.carbon.ci_g_per_kwh);
    const excluded = peerResults.filter(x => !rows.includes(x)).map(x => x.code + (x.error ? '（载入失败）' : '（年度不同或资料不足）'));
    put('d_peer_note', (k.year == null ? '当前年度未确认，不生成同年度表。' : k.year + '年演示对照：按与顶部一致的排放强度字段排序，包含不同发电结构企业，不构成行业优劣排名。') + '全部原文未独立复核；同年度不等于边界、气体及核算方法已确认可比。' + (excluded.length ? ' 未纳入：' + excluded.join('、') + '。' : ''));
    document.querySelector('#d_peers tbody').innerHTML = rows.map(x => '<tr><td>' + E(x.code) + '</td><td>' + E(x.data.name) + '</td><td>' + E(x.data.carbon.year) + '</td><td>' + E(fmt(x.data.carbon.ci_g_per_kwh)) + '</td><td>演示口径 · 原文未独立复核</td></tr>').join('') || '<tr><td colspan="5">暂无可纳入的同年度数据。</td></tr>';
  } catch (e) {
    if (current()) host.textContent = '量化载入失败，请重试或继续查看已有数据与来源。';
  }
}
const localRenderProfile=renderProfile;
renderProfile=function(p){localRenderProfile(p);const host=document.createElement('section');host.id='mainQuantBridge';host.className='main-original-quant';$('profile').prepend(host);loadMainQuantBridge();};
