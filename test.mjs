import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {course as C} from './content/course.mjs';
const require=createRequire(import.meta.url),K=require('./core.js');
const memory=(initial={})=>({values:{...initial},getItem(k){return this.values[k]||null;},setItem(k,v){this.values[k]=v;}});
const u=C.units[0];
function finish(s,unit,miss=-1){const a=K.start(s,C,unit);assert.ok(a);for(let i=0;i<a.order.length;i++){const q=unit.questions.flatMap(p=>p.variants).find(q=>q.id===a.order[i]);const choice=i===miss?q.options.find(o=>o.id!==q.answer).id:q.answer;assert.equal(K.submit(s,C,unit,choice,3),true);assert.equal(K.submit(s,C,unit,choice,3),false,'cannot double submit');K.advance(s,C,unit);}return K.latest(s,unit);}
let s=K.fresh();assert.equal(K.submit(s,C,u,'bad',3),false);K.start(s,C,u);assert.equal(K.submit(s,C,u,'bad',3),false);assert.equal(K.submit(s,C,u,u.questions[0].variants[0].answer,0),false);
assert.equal(finish(s,u).passed,true);const first=JSON.stringify(K.history(s,u)[0]);assert.equal(K.start(s,C,u).form,'b');assert.equal(K.mastered(s,u),true,'unfinished retry keeps previous status');delete s.active[u.id];
const second=K.start(s,C,u);const crit=second.order.findIndex(id=>u.questions.flatMap(p=>p.variants).find(q=>q.id===id).critical);assert.ok(crit>=0);assert.equal(finish(s,u,crit).passed,false);assert.equal(K.latest(s,u).percent,90);assert.equal(K.latest(s,u).criticalMiss,true);assert.equal(JSON.stringify(K.history(s,u)[0]),first);
for(const raw of ['{','null','[]','{}',JSON.stringify({version:3,attempts:{[u.id]:[{}]},active:{},role:'evil'})]){const out=K.load(memory({[K.KEY]:raw}),C);assert.equal(out.state.role,'ug');assert.equal(K.mastered(out.state,u),false);}
const denied={getItem(){throw Error('denied');},setItem(){throw Error('denied');}};assert.equal(K.load(denied,C).available,false);assert.equal(K.save(denied,s),false);
s=K.fresh();const active=K.start(s,C,u),q=u.questions.flatMap(p=>p.variants).find(q=>q.id===active.order[0]);K.submit(s,C,u,q.answer,2);const m=memory();K.save(m,s);const restored=K.load(m,C).state;assert.equal(restored.active[u.id].responses.length,1);assert.equal(restored.active[u.id].feedback,true);assert.deepEqual(restored.active[u.id].optionOrder,active.optionOrder);
if(C.units.length>1){s=K.fresh();assert.equal(K.unlocked(s,C,C.units[1]),false);assert.equal(K.start(s,C,C.units[1]),null);finish(s,u);assert.equal(K.unlocked(s,C,C.units[1]),true);}
console.log('PASS: score/safety, immutable first attempt, alternating forms, duplicate submission, validation, persistence, corruption/denial and prerequisite checks.');
for (const role of K.ROLES) {
  s=K.fresh();s.role=role;
  for (const unit of C.units) {
    assert.equal(K.unlocked(s,C,unit),true);
    assert.equal(finish(s,unit).passed,true);
    assert.equal(K.latest(s,unit).percent,100);
    assert.equal(finish(s,unit).passed,true);
    assert.equal(K.history(s,unit)[1].form,'b');
  }
  const restored=K.validateState(JSON.parse(JSON.stringify(s)),C);
  assert.ok(C.units.every(unit=>K.mastered(restored,unit)));
  finish(s,u,0);
  const retry=K.start(s,C,u);
  const critical=retry.order.findIndex(id=>K.allQuestions(C).find(q=>q.id===id).critical);
  finish(s,u,critical);
  assert.equal(K.unlocked(s,C,C.units.at(-1)),false,'failed prerequisite relocks later assessments');
}
console.log('PASS: complete twelve-unit journey, both forms, all four roles, round-trip persistence and prerequisite regression.');
