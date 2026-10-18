/* One primary action; read-only memory demos, never writes the ledger. */
(function(){let stage=0,busy=false,chosen=null;
const button=$('simpleDemoAction'),result=$('simpleDemoResult');
function track(n){[1,2,3].forEach(i=>$('demoTrack'+i).classList.toggle('current',i===n));}
async function choose(){if(!state.chain?.blocks?.length)await loadChain();const list=state.chain?.blocks||[];const b=list.find(x=>x.digest===$('digest').value)||[...list].reverse().find(x=>x.type==='carbon-profile')||list.at(-1);if(!b)throw Error('还没有报告记录。请先到第三步生成一份参考报告，再回来体验。');chosen=b;selectBlock(b);return b;}
// 具体案例卡片：让演示每一步都能看到真实登记内容，而不是抽象描述。
function caseCard(b,extra){return '<div class="demo-case"><small>本次演示案例</small><b>'+E(b.company_name||'登记记录')+(b.version?' · 版本 V'+E(b.version):'')+' · 节点 #'+E(b.index)+'</b><code>'+E((b.digest||'').slice(0,16))+'…</code>'+(extra||'')+'</div>';}
async function extra(mode){if(busy)return;busy=true;try{const b=await choose();const r=await api('/api/evidence/chain-demo',{digest:b.digest,mode});result.innerHTML=mode==='recompute_all'?'<b>整本重算后，内部检查可能再次一致。</b><p>这说明：如果一个人能控制本机所有记录，仅靠本地检查仍不够。外部独立保管或检查点才有助于发现整本被重写。</p>':'<b class="demo-bad">记录之间的链接断了。</b><p>这条记录不再能正确连到前一条。检查会指出链接异常；真实账本没有改变。</p>';result.innerHTML+='<p>副本检查结果：'+integrity(r.after_integrity)+'</p>';}finally{busy=false;}}
button.onclick=()=>work(button,async()=>{if(busy)return;busy=true;try{
 if(stage===0){const b=await choose();result.innerHTML=caseCard(b)+'<b class="demo-good">原记录已选好。</b><p>这份登记内容有完整的记录摘要和链上链接。下面会把它的<b>副本</b>改掉一个具体数值，保留原来的摘要和链接不变，看看检查能不能发现。</p>';stage=1;track(2);button.textContent='下一步：改动副本中的一处内容';}
 else if(stage===1){const r=await api('/api/evidence/chain-demo',{digest:chosen.digest,mode:'edit_payload'});result.innerHTML=caseCard(chosen,'<span class="demo-bad">副本已改动一处内容（原摘要未同步）</span>')+'<b class="demo-bad">改过的内容，对不上原来的记录。</b><p>副本内容改变，但原摘要没有一起变，所以检查出现异常。下面列出受到影响的节点。</p><div class="demo-blocks">'+(r.blocks||[]).map(b=>'<span class="badge '+(['OK','ok','valid','unchanged'].includes(b.status)?'green':'amber')+'">#'+E(b.index)+' '+(['OK','ok','valid','unchanged'].includes(b.status)?'未发现异常':'需要复核')+'</span>').join('')+'</div><p><b>你刚才看到的是内容一致性检查，不是对企业数据真实性的认证。</b>真实账本未修改。</p>';stage=2;track(3);button.textContent='完成体验：恢复原记录视图';}
 else{await loadChain();result.innerHTML=(chosen?caseCard(chosen):'')+'<b class="demo-good">已恢复原记录视图。</b><p>刚才改动的副本已丢弃，已保存报告保持原样。</p>';stage=0;chosen=null;track(1);button.textContent='再体验一次';}
 }finally{busy=false;}});
$('simpleBreak').onclick=()=>work($('simpleBreak'),()=>extra('break_link'));$('simpleRecompute').onclick=()=>work($('simpleRecompute'),()=>extra('recompute_all'));
})();
