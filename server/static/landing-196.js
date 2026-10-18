/* Local-first fused introduction. No network, storage or business-data mutation. Host navigation is integrated separately. */
(function () {
  'use strict';
  function init() {
    const workspace = document.querySelector('.workspace');
    const brand = document.querySelector('body > .brand');
    if (!workspace || !brand || document.getElementById('landing196')) return;
    const arrow = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15m-6-6 6 6-6 6"/></svg>';
    // Independent sprout/coin artwork; all motion shares the pausable SVG timeline.
    const art = "<svg class=\"l196-orbit\" viewBox=\"0 -40 620 550\" fill=\"none\" role=\"img\" aria-labelledby=\"heroArtTitle\"><title id=\"heroArtTitle\">绿苗与金币，三色行星沿三条空间轨道环绕，象征追溯、记录与存证</title><defs><radialGradient id=\"heroGlow\"><stop stop-color=\"#498b59\" stop-opacity=\".32\"/><stop offset=\"1\" stop-color=\"#103b2d\" stop-opacity=\"0\"/></radialGradient><linearGradient id=\"heroGold\" x1=\"240\" y1=\"200\" x2=\"380\" y2=\"340\" gradientUnits=\"userSpaceOnUse\"><stop stop-color=\"#f0d998\"/><stop offset=\".5\" stop-color=\"#c3a04e\"/><stop offset=\"1\" stop-color=\"#9a6b00\"/></linearGradient><linearGradient id=\"sprout\" x1=\"270\" y1=\"130\" x2=\"360\" y2=\"240\" gradientUnits=\"userSpaceOnUse\"><stop stop-color=\"#93d49c\"/><stop offset=\"1\" stop-color=\"#30845b\"/></linearGradient><clipPath id=\"frontHalf\"><rect x=\"40\" y=\"225\" width=\"540\" height=\"100\"/></clipPath><radialGradient id=\"planet-a\" cx=\".3\" cy=\".25\"><stop stop-color=\"#fff\"/><stop offset=\".3\" stop-color=\"#d5b96f\"/><stop offset=\"1\" stop-color=\"#244b3b\"/></radialGradient><radialGradient id=\"planet-b\" cx=\".3\" cy=\".25\"><stop stop-color=\"#fff\"/><stop offset=\".3\" stop-color=\"#72cba5\"/><stop offset=\"1\" stop-color=\"#244b3b\"/></radialGradient><radialGradient id=\"planet-c\" cx=\".3\" cy=\".25\"><stop stop-color=\"#fff\"/><stop offset=\".3\" stop-color=\"#b7d9e4\"/><stop offset=\"1\" stop-color=\"#244b3b\"/></radialGradient><clipPath id=\"heroDepthBack\" clipPathUnits=\"userSpaceOnUse\"><rect x=\"30\" y=\"110\" width=\"560\" height=\"115\"/></clipPath><clipPath id=\"heroDepthFront\" clipPathUnits=\"userSpaceOnUse\"><rect x=\"30\" y=\"225\" width=\"560\" height=\"115\"/></clipPath></defs><circle cx=\"310\" cy=\"225\" r=\"215\" fill=\"url(#heroGlow)\"/><g class=\"hero-particle-stream\"><g opacity=\"0.12\"><path d=\"M30 0v6\" stroke=\"#c5a85e\" stroke-width=\"2\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"6s\" begin=\"-0s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.16499999999999998\"><path d=\"M103 47v7\" stroke=\"#67ae8a\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"7s\" begin=\"-1s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.21\"><path d=\"M176 94v8\" stroke=\"#67ae8a\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"8s\" begin=\"-2s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.255\"><path d=\"M249 141v9\" stroke=\"#c5a85e\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"9s\" begin=\"-3s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.12\"><path d=\"M322 188v10\" stroke=\"#67ae8a\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"10s\" begin=\"-4s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.16499999999999998\"><path d=\"M395 235v11\" stroke=\"#67ae8a\" stroke-width=\"2\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"11s\" begin=\"-5s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.21\"><path d=\"M468 282v12\" stroke=\"#c5a85e\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"12s\" begin=\"-6s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.255\"><path d=\"M541 329v13\" stroke=\"#67ae8a\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"6s\" begin=\"-7s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.12\"><path d=\"M54 376v14\" stroke=\"#67ae8a\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"7s\" begin=\"-8s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.16499999999999998\"><path d=\"M127 423v15\" stroke=\"#c5a85e\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"8s\" begin=\"-0s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.21\"><path d=\"M200 30v16\" stroke=\"#67ae8a\" stroke-width=\"2\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"9s\" begin=\"-1s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.255\"><path d=\"M273 77v17\" stroke=\"#67ae8a\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"10s\" begin=\"-2s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.12\"><path d=\"M346 124v18\" stroke=\"#c5a85e\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"11s\" begin=\"-3s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.16499999999999998\"><path d=\"M419 171v6\" stroke=\"#67ae8a\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"12s\" begin=\"-4s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.21\"><path d=\"M492 218v7\" stroke=\"#67ae8a\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"6s\" begin=\"-5s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.255\"><path d=\"M565 265v8\" stroke=\"#c5a85e\" stroke-width=\"2\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"7s\" begin=\"-6s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.12\"><path d=\"M78 312v9\" stroke=\"#67ae8a\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"8s\" begin=\"-7s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.16499999999999998\"><path d=\"M151 359v10\" stroke=\"#67ae8a\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"9s\" begin=\"-8s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.21\"><path d=\"M224 406v11\" stroke=\"#c5a85e\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"10s\" begin=\"-0s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.255\"><path d=\"M297 13v12\" stroke=\"#67ae8a\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"11s\" begin=\"-1s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.12\"><path d=\"M370 60v13\" stroke=\"#67ae8a\" stroke-width=\"2\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"12s\" begin=\"-2s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.16499999999999998\"><path d=\"M443 107v14\" stroke=\"#c5a85e\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"6s\" begin=\"-3s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.21\"><path d=\"M516 154v15\" stroke=\"#67ae8a\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"7s\" begin=\"-4s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.255\"><path d=\"M589 201v16\" stroke=\"#67ae8a\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"8s\" begin=\"-5s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.12\"><path d=\"M102 248v17\" stroke=\"#c5a85e\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"9s\" begin=\"-6s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.16499999999999998\"><path d=\"M175 295v18\" stroke=\"#67ae8a\" stroke-width=\"2\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"10s\" begin=\"-7s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.21\"><path d=\"M248 342v6\" stroke=\"#67ae8a\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"11s\" begin=\"-8s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.255\"><path d=\"M321 389v7\" stroke=\"#c5a85e\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"12s\" begin=\"-0s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.12\"><path d=\"M394 436v8\" stroke=\"#67ae8a\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"6s\" begin=\"-1s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.16499999999999998\"><path d=\"M467 43v9\" stroke=\"#67ae8a\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"7s\" begin=\"-2s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.21\"><path d=\"M540 90v10\" stroke=\"#c5a85e\" stroke-width=\"2\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"8s\" begin=\"-3s\" repeatCount=\"indefinite\"/></g><g opacity=\"0.255\"><path d=\"M53 137v11\" stroke=\"#67ae8a\" stroke-width=\"1\"/><animateTransform attributeName=\"transform\" type=\"translate\" from=\"0 -470\" to=\"0 470\" dur=\"9s\" begin=\"-4s\" repeatCount=\"indefinite\"/></g></g><g class=\"hero-depth-back\"><g transform=\"rotate(-28 310 225)\"><g clip-path=\"url(#heroDepthBack)\"><path d=\"M550 225A240 83 0 1 1 70 225A240 83 0 1 1 550 225\" stroke=\"#d5b96f\" stroke-opacity=\".25\" stroke-width=\"1.2\"/><g id=\"l196-planet-a-back\"><circle r=\"17\" fill=\"#d5b96f\" opacity=\".08\"/><circle r=\"9\" fill=\"url(#planet-a)\" stroke=\"#d5b96f\" stroke-width=\"1\"/><animateMotion dur=\"18s\" repeatCount=\"indefinite\" path=\"M550 225A240 83 0 1 1 70 225A240 83 0 1 1 550 225\" begin=\"-6s\"/></g></g></g><g transform=\"rotate(32 310 225)\"><g clip-path=\"url(#heroDepthBack)\"><path d=\"M550 225A240 83 0 1 1 70 225A240 83 0 1 1 550 225\" stroke=\"#72cba5\" stroke-opacity=\".25\" stroke-width=\"1.2\"/><g id=\"l196-planet-b-back\"><circle r=\"17\" fill=\"#72cba5\" opacity=\".08\"/><circle r=\"9\" fill=\"url(#planet-b)\" stroke=\"#72cba5\" stroke-width=\"1\"/><animateMotion dur=\"23s\" repeatCount=\"indefinite\" path=\"M550 225A240 83 0 1 1 70 225A240 83 0 1 1 550 225\" begin=\"-7.666666666666667s\"/></g></g></g><g transform=\"rotate(90 310 225)\"><g clip-path=\"url(#heroDepthBack)\"><path d=\"M550 225A240 83 0 1 1 70 225A240 83 0 1 1 550 225\" stroke=\"#b7d9e4\" stroke-opacity=\".25\" stroke-width=\"1.2\"/><g id=\"l196-planet-c-back\"><circle r=\"17\" fill=\"#b7d9e4\" opacity=\".08\"/><circle r=\"9\" fill=\"url(#planet-c)\" stroke=\"#b7d9e4\" stroke-width=\"1\"/><animateMotion dur=\"29s\" repeatCount=\"indefinite\" path=\"M550 225A240 83 0 1 1 70 225A240 83 0 1 1 550 225\" begin=\"-9.666666666666666s\"/></g></g></g></g><g class=\"hero-seed-coin\"><ellipse cx=\"310\" cy=\"329\" rx=\"91\" ry=\"15\" fill=\"#061f17\" opacity=\".6\"/><circle cx=\"315\" cy=\"271\" r=\"69\" fill=\"#725216\"/><circle cx=\"310\" cy=\"265\" r=\"69\" fill=\"url(#heroGold)\" stroke=\"#e3cc8c\" stroke-width=\"2\"/><g class=\"hero-brand-logo\" transform=\"translate(267 222) scale(0.3359375)\">\n\n<path d=\"M128 35C151 51 176 55 204 57V117C204 164 175 198 128 222C81 198 52 164 52 117V57C80 55 105 51 128 35Z\" fill=\"#174B39\" stroke=\"#9A6B00\" stroke-width=\"4\" stroke-linejoin=\"round\"/>\n<path d=\"M86 158C69 139 79 115 100 103L135 82C153 102 143 126 122 138L86 158Z\" stroke=\"#fff\" stroke-width=\"12\" stroke-linejoin=\"round\"/>\n<path d=\"M121 178C103 158 113 134 134 122L169 101C187 121 177 145 156 157L121 178Z\" stroke=\"#9A6B00\" stroke-width=\"12\" stroke-linejoin=\"round\"/>\n<path d=\"M115 137L128 129\" stroke=\"#174B39\" stroke-width=\"20\"/>\n<path d=\"M115 137L128 129\" stroke=\"#9A6B00\" stroke-width=\"12\" stroke-linecap=\"round\"/>\n<path d=\"M115 137L128 129\" stroke=\"#D4BA76\" stroke-width=\"5\" stroke-linecap=\"round\"/>\n\n</g><path d=\"M310 214C312 181 302 161 283 145\" stroke=\"#7cbf88\" stroke-width=\"7\" stroke-linecap=\"round\"/><path d=\"M304 187C269 188 247 165 244 133C277 129 307 149 304 187Z\" fill=\"url(#sprout)\"/><path d=\"M307 174C306 139 328 115 365 115C368 146 345 174 307 174Z\" fill=\"url(#sprout)\"/><path d=\"m255 144 43 35m55-50-40 36\" stroke=\"#d3ecd0\" stroke-opacity=\".55\" stroke-width=\"2\" stroke-linecap=\"round\"/></g><g class=\"hero-depth-front\"><g transform=\"rotate(-28 310 225)\"><g clip-path=\"url(#heroDepthFront)\"><path d=\"M550 225A240 83 0 1 1 70 225A240 83 0 1 1 550 225\" stroke=\"#d5b96f\" stroke-opacity=\".78\" stroke-width=\"1.8\"/><g id=\"l196-planet-a\"><circle r=\"17\" fill=\"#d5b96f\" opacity=\".08\"/><circle r=\"9\" fill=\"url(#planet-a)\" stroke=\"#d5b96f\" stroke-width=\"1\"/><animateMotion dur=\"18s\" repeatCount=\"indefinite\" path=\"M550 225A240 83 0 1 1 70 225A240 83 0 1 1 550 225\" begin=\"-6s\"/></g></g></g><g transform=\"rotate(32 310 225)\"><g clip-path=\"url(#heroDepthFront)\"><path d=\"M550 225A240 83 0 1 1 70 225A240 83 0 1 1 550 225\" stroke=\"#72cba5\" stroke-opacity=\".78\" stroke-width=\"1.8\"/><g id=\"l196-planet-b\"><circle r=\"17\" fill=\"#72cba5\" opacity=\".08\"/><circle r=\"9\" fill=\"url(#planet-b)\" stroke=\"#72cba5\" stroke-width=\"1\"/><animateMotion dur=\"23s\" repeatCount=\"indefinite\" path=\"M550 225A240 83 0 1 1 70 225A240 83 0 1 1 550 225\" begin=\"-7.666666666666667s\"/></g></g></g><g transform=\"rotate(90 310 225)\"><g clip-path=\"url(#heroDepthFront)\"><path d=\"M550 225A240 83 0 1 1 70 225A240 83 0 1 1 550 225\" stroke=\"#b7d9e4\" stroke-opacity=\".78\" stroke-width=\"1.8\"/><g id=\"l196-planet-c\"><circle r=\"17\" fill=\"#b7d9e4\" opacity=\".08\"/><circle r=\"9\" fill=\"url(#planet-c)\" stroke=\"#b7d9e4\" stroke-width=\"1\"/><animateMotion dur=\"29s\" repeatCount=\"indefinite\" path=\"M550 225A240 83 0 1 1 70 225A240 83 0 1 1 550 225\" begin=\"-9.666666666666666s\"/></g></g></g></g><g font-family=\"Microsoft YaHei, sans-serif\" font-size=\"10\" letter-spacing=\"2\"><text x=\"440\" y=\"100\" fill=\"#ddc585\">碳溯</text><text x=\"60\" y=\"327\" fill=\"#8bd2b0\">碳链</text><text x=\"345\" y=\"418\" fill=\"#c2dce6\">碳证</text></g></svg>";
    const landing = document.createElement('main');
    landing.id = 'landing196';
    landing.tabIndex = -1;
    landing.setAttribute('aria-label', '绿碳链证产品导引');
    landing.innerHTML = `
      <section class="l196-hero" aria-labelledby="l196-title"><div class="l196-hero-grid"><div class="l196-hero-copy"><p class="l196-kicker"><i></i> 绿碳链证 · 研究演示平台</p><h1 id="l196-title">看见低碳转型，<br>让每一步<span>有据可循。</span></h1><p class="l196-lead">查看企业排放与产出原值、同口径相对变化，核对来源，生成可追溯的参考报告。报告登记画像与已保存补充。</p><div class="l196-actions"><button class="l196-btn l196-primary" data-l196-enter="1">进入企业工作台 ${arrow}</button><button class="l196-btn l196-outline" data-l196-enter="4">已有报告？直接核验</button></div><div class="l196-hero-tags"><span>来源清晰</span><span>碳表现量化</span><span>边界透明</span></div></div><div class="l196-hero-art">${art}<p class="hero-art-signature">trace<span>·</span>record<span>·</span>attestation</p><div class="l196-motion-controls"><button type="button" class="l196-motion-toggle" aria-controls="l196-planet-a l196-planet-b l196-planet-c" aria-pressed="false">暂停轨道动画</button><span class="l196-motion-status" role="status"></span></div></div></div><a class="l196-scroll" href="#l196-journey"><span>向下探索 · 如何工作</span><span aria-hidden="true">↓</span></a></section>
      <nav class="l196-progress" aria-label="导引章节"><a href="#l196-data" aria-current="step"><span>01</span> 碳表现总览</a><a href="#l196-plan"><span>02</span> 四轴变化雷达</a><a href="#l196-report"><span>03</span> 报告登记</a><a href="#l196-verify"><span>04</span> 材料查验</a></nav>
      <div class="l196-journey" id="l196-journey"><header class="l196-section-heading l196-reveal"><p class="l196-kicker">FROM DATA TO EVIDENCE</p><h2>四步查看碳数据与核验报告</h2><p>沿着四个环节，理解企业信息如何进入参考报告。</p></header>
      <section class="l196-chapter l196-reveal" id="l196-data" aria-labelledby="l196-data-title"><div class="l196-chapter-copy"><span class="l196-number">01 / UNDERSTAND</span><h2 id="l196-data-title">选择企业，<br>看清碳表现总览。</h2><p>从企业公开 ESG 报告中提取范围一、范围二排放量与全口径发电量，按统一口径复算度电碳排放强度。结合允许可比时的同比变化，查看企业碳数据及其依据。</p><ul><li>排放强度 =（范围一 + 范围二）÷ 全口径发电量</li><li>同比仅在允许的可比口径下展示</li><li>缺失保留缺失，不补零、不拼接年份</li></ul></div><div class="l196-demo l196-profile-demo"><div class="l196-demo-top"><span>企业碳表现总览</span><span class="l196-mini-label">示意 · 非企业实测</span></div><div class="l196-metric-grid"><div><span>scope1</span><b>直接排放</b><small>tCO2</small></div><div><span>scope2</span><b>间接排放</b><small>tCO2</small></div></div><div class="l196-chart" aria-hidden="true"><div style="--bar:72%"><i></i><span>排放总量</span></div><div style="--bar:49%"><i></i><span>发电量</span></div><div style="--bar:58%"><i></i><span>排放强度</span></div></div><p class="l196-demo-foot">图形仅示意信息结构，不代表真实企业数值或绩效。</p></div></section>
      <section class="l196-chapter l196-reverse l196-reveal" id="l196-plan" aria-labelledby="l196-plan-title"><div class="l196-chapter-copy"><span class="l196-number">02 / CONNECT</span><h2 id="l196-plan-title">四轴变化雷达，<br>看清相对变化。</h2><p>查看scope1、scope2、发电量与排放强度。本期原值除以上期原值再乘100；上期＝100，不做标准化打分。</p><ul><li>排放轴向内下降为减排方向，向外上升为增排方向</li><li>发电量仅表示产出规模，不判好坏</li><li>刻度上限200，超限标注实际指数，缺值不补零</li></ul><p><b>仅表示相对变化，不是绩效评价，也不用于跨企业排名。</b></p></div><div class="l196-demo l196-plan-demo"><div class="l196-demo-top"><span>四轴相对变化 · 上期＝100</span><span class="l196-mini-label">结构示意 · 非实测</span></div><div class="l196-radar"><svg viewBox="0 0 340 300" role="img" aria-label="scope1、scope2、发电量、排放强度四轴相对变化示意，上期100，上限200，非绩效评价"><g fill="none" stroke="#bacbd4" stroke-dasharray="4 4"><path d="m170 54 98 98-98 98-98-98Z"/><path d="m170 78.5 73.5 73.5-73.5 73.5-73.5-73.5Z"/><path d="m170 103 49 49-49 49-49-49Z"/><path d="m170 127.5 24.5 24.5-24.5 24.5-24.5-24.5Z"/></g><path d="M170 54v196M72 152h196" stroke="#bacbd4"/><path d="m170 103 49 49-49 49-49-49Z" fill="none" stroke="#8198ac" stroke-width="2" stroke-dasharray="5 4"/><path d="m170 111 42 41-42 59-44-59Z" fill="#416b9b20" stroke="#416b9b" stroke-width="2"/><g fill="#397c9a" font-size="11" text-anchor="middle"><text x="170" y="19">scope1</text><text x="170" y="34">向内减排 / 向外增排</text><text x="298" y="145">scope2</text><text x="298" y="161">向内减排</text><text x="42" y="145">排放强度</text><text x="42" y="161">向内减排</text><text x="170" y="274" fill="#927d55">发电量 · 产出规模</text><text x="170" y="289" fill="#927d55">不判好坏</text></g><g fill="#617789" font-size="10"><text x="177" y="51">200 上限</text><text x="177" y="77">150</text><text x="177" y="101">100</text><text x="177" y="126">50</text><text x="177" y="150">0</text></g></svg></div><div class="l196-radar-legend"><span><i style="background:#416b9b"></i>本期相对指数</span><span><i style="background:#8198ac"></i>上期＝100（虚线）</span></div><p class="l196-demo-foot">仅示意相对变化，不是绩效评价，不用于跨企业排名。实测超200时在轴端标注实际指数。</p><div class="l196-track l196-radar-track"><div><span class="l196-track-dot">4</span><section><small>相对变化轴</small><h3>原值与变化分开看</h3><p>报告使用scope1、scope2、发电量三轴；总量和强度另列原值。</p></section></div></div></div></section>
      <section class="l196-chapter l196-reveal" id="l196-report" aria-labelledby="l196-report-title"><div class="l196-chapter-copy"><span class="l196-number">03 / PRESERVE</span><h2 id="l196-report-title">生成报告，<br>登记版本记录。</h2><p>报告保存企业碳画像、来源线索和已保存的补充记录，供后续查询与材料比对。排放总量与排放强度单独列示，不与独立观测轴重复混合。</p><ul><li>报告数值取自登记快照，而非实时替换</li><li>摘要对应登记内容，前后版本可追溯</li><li>来源状态和业务限制随报告保留</li></ul></div><div class="l196-demo l196-version-demo"><div class="l196-paper"><span class="l196-paper-brand">GREENCHAIN / 绿碳链证</span><h3>企业碳数据参考报告</h3><span class="l196-paper-line"></span><span class="l196-paper-line short"></span><div class="l196-paper-bars" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div><span class="l196-paper-line"></span><p>数据来源与限制 · 随报告保留</p></div><div class="l196-version-path"><span>上一版本</span><i aria-hidden="true"></i><b>本次快照</b></div><p class="l196-demo-foot">版本关联示意 · 非独立机构认证</p></div></section>
      <section class="l196-chapter l196-reverse l196-reveal" id="l196-verify" aria-labelledby="l196-verify-title"><div class="l196-chapter-copy"><span class="l196-number">04 / REVIEW</span><h2 id="l196-verify-title">材料查验，<br>核对登记内容。</h2><p>使用报告摘要查询已登记的企业、版本与报告内容，再按工作台提供的查验入口核对材料。记录查询、材料一致性和本地链状态分开说明，避免把“查得到”误认为“已证实”。</p><ul><li>历史报告可独立核验，不必先选择企业</li><li>材料变更后重新比对，不沿用旧结果</li><li>一致性查验不证明原始披露或 PDF 真实</li></ul><button class="l196-text-link" data-l196-enter="4">打开材料核验 ${arrow}</button></div><div class="l196-demo l196-verify-demo"><div class="l196-demo-top"><span>三个问题，分别回答</span><span class="l196-mini-label">核验边界</span></div><div class="l196-check-row"><span aria-hidden="true">01</span><div><h3>是否存在登记记录？</h3><p>查询摘要对应的版本与企业</p></div></div><div class="l196-check-row"><span aria-hidden="true">02</span><div><h3>提交材料是否一致？</h3><p>按查验入口比对材料与保存版本</p></div></div><div class="l196-check-row"><span aria-hidden="true">03</span><div><h3>本地链链接是否完整？</h3><p>检查本机记录前后关联</p></div></div><p class="l196-verification-limit">一致性不等于真实性；本机记录不等于多机构独立验证。</p></div></section></div>
      <section class="l196-values"><div class="l196-values-inner"><header class="l196-section-heading l196-reveal"><p class="l196-kicker">CLARITY BY DESIGN</p><h2>来源、版本与使用范围</h2></header><div class="l196-value-grid"><article class="l196-reveal"><span>01 — TRACEABLE</span><h3>数字有来处</h3><p>数据性质、来源链接和待核实项一起呈现，引用不冒充验证。</p></article><article class="l196-reveal"><span>02 — VERSIONED</span><h3>变更有脉络</h3><p>保存报告快照与前后版本关系，避免新内容覆盖旧结论。</p></article><article class="l196-reveal"><span>03 — HUMAN-LED</span><h3>业务有边界</h3><p>辅助查看碳数据与材料，不生成信用评级，不自动审批或建议放贷。</p></article></div></div></section>
      <section class="l196-final l196-reveal"><p class="l196-kicker">YOUR NEXT STEP</p><h2>选择企业，或核验已有报告</h2><p>选择企业探索数据，或带着已有报告直接进入核验。</p><div class="l196-actions"><button class="l196-btn l196-primary" data-l196-enter="1">进入企业工作台 ${arrow}</button><button class="l196-btn l196-light" data-l196-enter="4">已有报告，直接核验</button></div><aside class="l196-boundary"><b>使用前，请了解</b><p>本平台是研究演示与人工复核辅助工具，不是银行贷款批准、第三方认证或原始披露真实性证明。演示、附件及人工补充数字仍需回原报告核对。记录保存在本机，目前没有其他机构独立保管或验证；财务、征信、担保与合规审查另行开展。</p></aside></section>
      <footer class="l196-footer"><b>绿碳链证</b><span>© 2026 绿碳链证团队</span><span>看清数据，尊重边界。</span></footer>`;
    brand.insertAdjacentElement('afterend', landing);
    const brandMark = brand.querySelector('.identity img');
    if (brandMark) { brandMark.src = '/static/logo-shield-transparent.svg?v=leafshield2'; brandMark.alt = '白底深绿盾牌与相扣的叶形链环'; }
    const reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)');
    const orbit = landing.querySelector('.l196-orbit');
    const motionToggle = landing.querySelector('.l196-motion-toggle');
    const motionStatus = landing.querySelector('.l196-motion-status');
    // Prime dynamically inserted SMIL after layout; no per-frame JS positioning.
    if (orbit && typeof orbit.setCurrentTime === 'function') requestAnimationFrame(function () {
      orbit.setCurrentTime(2);
      orbit.style.overflow = 'hidden';
      syncOrbitMotion();
    });
    let userPaused = false;
    // Hero motion follows the in-page control; pause when hidden to save resources.
    function syncOrbitMotion() {
      const paused = userPaused || landing.hidden || document.hidden;
      landing.classList.toggle('l196-motion-paused', paused);
      if (orbit && typeof orbit.pauseAnimations === 'function') {
        if (paused) orbit.pauseAnimations();
        else if (orbit.animationsPaused()) orbit.unpauseAnimations();
      }
      motionToggle.disabled = false;
      motionToggle.setAttribute('aria-pressed', String(paused));
      motionToggle.textContent = userPaused ? '继续轨道动画' : '暂停轨道动画';
      motionStatus.textContent = userPaused ? '已暂停' : '三轨道运行中';
    }
    motionToggle.addEventListener('click', function () {
      userPaused = !userPaused;
      syncOrbitMotion();
    });
    if (reduced) {
      if (reduced.addEventListener) reduced.addEventListener('change', syncOrbitMotion);
      else if (reduced.addListener) reduced.addListener(syncOrbitMotion);
    }
    document.addEventListener('visibilitychange', syncOrbitMotion);
    // Also cover host code toggling hidden without going through our navigation.
    if ('MutationObserver' in window) new MutationObserver(syncOrbitMotion).observe(landing, {attributes:true, attributeFilter:['hidden']});
    const home = document.createElement('button');
    home.type = 'button'; home.id = 'landing196Home'; home.className = 'l196-home';
    home.textContent = '返回导引首页'; home.hidden = true;
    (brand.querySelector('.brand-inner') || brand).appendChild(home);
    function currentState() { try { return typeof state !== 'undefined' ? state : null; } catch (_) { return null; } }
    function showWorkspace(focus) {
      landing.hidden = true; workspace.hidden = false; home.hidden = false;
      syncOrbitMotion();
      document.body.classList.remove('l196-active');
      if (focus) { const target = document.getElementById('main'); if (target) target.focus({preventScroll:true}); }
    }
    // Only navigation metadata is stored; company/report/form state stays in memory.
    let route_applying = false;
    let history_index = history.state && Number.isInteger(history.state.l196_index) ? history.state.l196_index : 0;
    let restoring_history = false;
    let active_url = location.pathname + location.search + location.hash;
    function route_url(step) { return step === 0 ? '/' : step === 1 ? '/app' : '/app?step=' + step; }
    function sync_url(step, replace) {
      const url = route_url(step);
      const same_route = location.pathname + location.search === url;
      if (!replace && same_route && !location.hash) return;
      if (!replace) history_index += 1;
      const metadata = Object.assign({}, history.state, {l196_index:history_index});
      history[replace ? 'replaceState' : 'pushState'](metadata, '', url);
      active_url = url;
    }
    window.openLanding196 = function () {
      if (!landing.hidden) { if (!route_applying) sync_url(0, false); return true; }
      const s = currentState();
      if (s && s.dirty && !window.confirm('有未保存的补充输入，确定返回导引首页？输入会保留，尚未保存的内容不会进入报告。')) return false;
      workspace.hidden = true; landing.hidden = false; home.hidden = true;
      syncOrbitMotion();
      document.body.classList.add('l196-active');
      if (!route_applying) sync_url(0, false);
      window.scrollTo({top:0,behavior:'instant'}); landing.focus({preventScroll:true}); return true;
    };
    // Keep the original navigation's profile and unsaved-input guards authoritative.
    const originalGo = window.go;
    if (typeof originalGo === 'function') {
      window.go = function (step) {
        const n = Number(step);
        const result = originalGo.call(this, n);
        const s = currentState();
        if (!s || s.step === n) {
          showWorkspace(false);
          if (!route_applying) sync_url(n, false);
        }
        return result;
      };
    }
    window.enterWorkspace196 = function (step) {
      const n = [1,2,3,4].includes(Number(step)) ? Number(step) : 1;
      if (typeof window.go === 'function') window.go(n);
      else showWorkspace(false);
      const s = currentState();
      if (landing.hidden && (!s || s.step === n)) { showWorkspace(true); window.scrollTo({top:0,behavior:'instant'}); return true; }
      return false;
    };
    function apply_location() {
      const params = new URLSearchParams(location.search);
      let step = 0;
      if (location.pathname === '/app' || location.pathname === '/app/') {
        const values = params.getAll('step');
        step = values.length === 1 && /^[1-4]$/.test(values[0]) ? Number(values[0]) : 1;
        const s = currentState();
        if ((step === 2 || step === 3) && (!s || !s.profile)) step = 1;
      }
      route_applying = true;
      let accepted;
      try { accepted = step === 0 ? window.openLanding196() : window.enterWorkspace196(step); }
      finally { route_applying = false; }
      return {accepted:accepted, step:step};
    }
    window.addEventListener('popstate', function (event) {
      if (restoring_history) { restoring_history = false; return; }
      const target_index = event.state && event.state.l196_index;
      const result = apply_location();
      if (result.accepted) {
        if (Number.isInteger(target_index)) history_index = target_index;
        // Keep homepage anchor entries and their existing scroll animation intact.
        if (result.step === 0 && location.pathname === '/' && !location.search) {
          active_url = location.pathname + location.hash;
        } else sync_url(result.step, true);
      } else if (Number.isInteger(target_index) && target_index !== history_index) {
        // Undo the traversal, not a new push: Forward/Back remain usable after Cancel.
        restoring_history = true;
        history.go(history_index - target_index);
      } else {
        history.replaceState(Object.assign({}, history.state, {l196_index:history_index}), '', active_url);
      }
    });
    home.addEventListener('click', window.openLanding196);
    const identity = brand.querySelector('.identity');
    let chapter_scroll_frame = 0;
    const cancel_chapter_scroll = () => { cancelAnimationFrame(chapter_scroll_frame); chapter_scroll_frame = 0; };
    window.addEventListener('wheel', cancel_chapter_scroll, {passive:true});
    window.addEventListener('touchstart', cancel_chapter_scroll, {passive:true});
    window.addEventListener('keydown', event => {
      if (['ArrowUp','ArrowDown','PageUp','PageDown','Home','End','Escape',' '].includes(event.key)) cancel_chapter_scroll();
    });
    landing.querySelectorAll('.l196-progress a').forEach(link => {
      link.addEventListener('click', event => {
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.button !== 0) return;
        const target_section = document.getElementById(link.hash.slice(1));
        if (!target_section) return;
        event.preventDefault();
        cancel_chapter_scroll();
        const start_y = window.scrollY;
        const nav_height = landing.querySelector('.l196-progress').getBoundingClientRect().height;
        const max_y = Math.max(0, document.documentElement.scrollHeight - window.innerHeight);
        const target_transform = getComputedStyle(target_section).transform;
        const reveal_offset = target_transform === 'none' ? 0 : new DOMMatrixReadOnly(target_transform).m42;
        const end_y = Math.max(0, Math.min(max_y, start_y + target_section.getBoundingClientRect().top - reveal_offset - nav_height - 10));
        const start_time = performance.now();
        const duration_ms = 700;
        const animate_scroll = now => {
          const progress = Math.min(1, (now - start_time) / duration_ms);
          const eased = progress < .5 ? 4 * progress ** 3 : 1 - (-2 * progress + 2) ** 3 / 2;
          window.scrollTo({top:start_y + (end_y - start_y) * eased, behavior:'instant'});
          if (progress < 1) chapter_scroll_frame = requestAnimationFrame(animate_scroll);
          else chapter_scroll_frame = 0;
        };
        chapter_scroll_frame = requestAnimationFrame(animate_scroll);
        history.replaceState(history.state, '', link.hash);
        active_url = location.pathname + location.search + location.hash;
      });
    });
    if (identity) identity.addEventListener('click', function(e) { if (!e.ctrlKey && !e.metaKey && !e.shiftKey && e.button === 0) { e.preventDefault(); window.openLanding196(); } });
    landing.querySelectorAll('[data-l196-enter]').forEach(button => button.addEventListener('click', () => window.enterWorkspace196(button.dataset.l196Enter)));
    const skip = document.querySelector('a.skip');
    if (skip) skip.addEventListener('click', function(e) { if (!landing.hidden) { e.preventDefault(); landing.focus(); } });
    let revealObserver;
    if ('IntersectionObserver' in window && !(reduced && reduced.matches)) {
      try {
        revealObserver = new IntersectionObserver(entries => entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add('l196-visible'); revealObserver.unobserve(entry.target); } }), {threshold:0.08});
        landing.querySelectorAll('.l196-reveal').forEach((el, i) => { el.style.setProperty('--l196-delay', (i % 3) * 70 + 'ms'); revealObserver.observe(el); });
        landing.classList.add('l196-motion-ready');
      } catch (_) { landing.classList.remove('l196-motion-ready'); }
      if (reduced) { const revealAll = () => { if (reduced.matches) { landing.classList.remove('l196-motion-ready'); if (revealObserver) revealObserver.disconnect(); } }; if (reduced.addEventListener) reduced.addEventListener('change', revealAll); }
    }
    if ('IntersectionObserver' in window) {
      const chapters = new IntersectionObserver(entries => { entries.forEach(entry => { if (entry.isIntersecting) landing.querySelectorAll('.l196-progress a').forEach(link => { if (link.hash === '#' + entry.target.id) link.setAttribute('aria-current','step'); else link.removeAttribute('aria-current'); }); }); }, {rootMargin:'-15% 0px -45% 0px',threshold:0});
      landing.querySelectorAll('.l196-chapter').forEach(el => chapters.observe(el));
    }
    // Hide only after insertion and handlers are complete: without JS the original app remains usable.
    workspace.hidden = true; landing.hidden = false; document.body.classList.add('l196-active');
    const initial_route = apply_location();
    if (initial_route.step === 0 && location.pathname === '/' && !location.search) {
      history.replaceState(Object.assign({}, history.state, {l196_index:history_index}), '', location.href);
    } else sync_url(initial_route.step, true);
    syncOrbitMotion();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, {once:true}); else init();
})();
