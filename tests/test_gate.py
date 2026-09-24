"""OxyVent safety gate: an attempt with any safety-critical miss does not count
towards the applied criterion, whatever its score."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = "file:///" + os.path.join(ROOT, "index.html").replace("\\", "/").lstrip("/")
KEY = "vkp.oxyvent.v4"
SKIP_ONB = ("try{var K='%s';var r=localStorage.getItem(K);"
  "var s=r?JSON.parse(r):{v:1,items:{},prefs:{pri:'all',lvl:'x',set:'both',fs:'m',theme:'system'},"
  "placement:null,lastUnit:null,exam:{attempts:[],lockUntil:0},settings:null,started:null,"
  "profile:null,plan:null,onboarded:false};s.onboarded=true;localStorage.setItem(K,JSON.stringify(s));}catch(e){}") % KEY
from playwright.sync_api import sync_playwright
fails = []
def check(n, c, x=""):
    print(("  OK   " if c else "  FAIL ") + n + ((" :: " + str(x)) if x and not c else ""))
    if not c: fails.append(n)
def seed_and_reload(page, mutate_js, expect_js, tries=4):
    for _ in range(tries):
        page.evaluate(mutate_js); page.wait_for_timeout(350); page.reload(); page.wait_for_timeout(1000)
        if page.evaluate(expect_js): return True
    raise AssertionError("state did not survive reload")
SEED = """(crit)=>{const K='%s';const s=JSON.parse(localStorage.getItem(K));
  const past=Date.now()-3*86400000; s.items=s.items||{};
  document.querySelectorAll('.q').forEach(q=>{s.items[q.getAttribute('data-q')]=
    {box:3,due:Date.now()+7*86400000,ok:true,firstPass:past,longest:2*86400000,retained:true,hint:0,tries:2};});
  s.exam={attempts:[{pct:96,right:48,n:50,critMiss:crit,at:Date.now()-86400000}],lockUntil:0};
  localStorage.setItem(K,JSON.stringify(s));}""" % KEY
with sync_playwright() as pw:
    b = pw.chromium.launch(); ctx = b.new_context(); ctx.add_init_script(SKIP_ONB)
    p = ctx.new_page(); errs = []; p.on("pageerror", lambda e: errs.append(str(e)))
    p.goto(U); p.wait_for_timeout(800)
    print("\n== MARKUP ==")
    n = p.evaluate("()=>document.querySelectorAll('.q[data-critical=\"1\"]').length")
    check("20 checkpoints flagged safety-critical", n == 20, n)
    fresh = p.evaluate("()=>(window.EXAM_ITEMS||[]).length")
    fc = p.evaluate("()=>(window.EXAM_ITEMS||[]).filter(i=>i.critical).length")
    check("30 fresh items, some safety-critical", fresh == 30 and 8 <= fc <= 15, (fresh, fc))
    check("assessment page states the rule", "safety-critical" in p.evaluate("()=>document.getElementById('assessment').textContent"))
    print("\n== GATE ==")
    p.evaluate("(c)=>{}", 1)
    for _ in range(4):
        p.evaluate(SEED, 1); p.wait_for_timeout(350); p.reload(); p.wait_for_timeout(1000)
        if p.evaluate("()=>JSON.parse(localStorage.getItem('%s')).exam.attempts.length===1" % KEY): break
    crit = p.evaluate("()=>[...document.querySelectorAll('.crit')].map(c=>({met:c.getAttribute('data-met'),v:c.querySelector('.cval').textContent,n:c.querySelector('.cnote').textContent}))")
    check("96% with a critical miss is not counted", crit[2]['met'] == '0', crit[2])
    check("criteria note explains the rule", "safety-critical" in crit[2]['n'])
    check("history marks the attempt not counted", "not counted" in p.evaluate("()=>document.getElementById('examHistory').textContent"))
    check("certificate stays locked", p.evaluate("()=>document.getElementById('certGate').hidden"))
    for _ in range(4):
        p.evaluate(SEED, 0); p.wait_for_timeout(350); p.reload(); p.wait_for_timeout(1000)
        if p.evaluate("()=>JSON.parse(localStorage.getItem('%s')).exam.attempts[0].critMiss===0" % KEY): break
    crit = p.evaluate("()=>[...document.querySelectorAll('.crit')].map(c=>c.getAttribute('data-met'))")
    check("96% with no critical miss counts", crit[2] == '1', crit)
    check("certificate unlocks", not p.evaluate("()=>document.getElementById('certGate').hidden"))
    check("no page errors", not errs, errs)
    b.close()
print("\nFAILURES:", fails if fails else "none")
raise SystemExit(1 if fails else 0)
