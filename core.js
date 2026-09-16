/* OxyVent learning engine. Shared logic is independent of the DOM. */
(function (root) {
  'use strict';
  const VERSION = 3;
  const KEY = 'vikkypaedia-oxyvent-v3';
  const ROLES = ['ug', 'nurse', 'picu', 'pg'];
  const DEPTHS = ['must', 'good', 'nice'];
  const object = v => v && typeof v === 'object' && !Array.isArray(v);
  const fresh = () => ({ version: VERSION, role: 'ug', depth: 'must', attempts: {}, active: {}, checks: {}, notes: {}, baseline: {}, cases: {}, legacy: null });
  const shuffle = (items, random = Math.random) => {
    const out = [...items];
    for (let i = out.length - 1; i > 0; i--) { const j = Math.floor(random() * (i + 1)); [out[i], out[j]] = [out[j], out[i]]; }
    return out;
  };
  const allQuestions = course => course.units.flatMap(u => u.questions.flatMap(q => q.variants));
  function validAttempt(a, unit) {
    if (!object(a) || !Array.isArray(a.responses) || a.responses.length !== unit.questions.length || !['a', 'b'].includes(a.form)) return false;
    const expected = new Set(unit.questions.map(q => q.variants.find(v => v.form === a.form).id));
    return a.responses.every(r => object(r) && expected.delete(r.id) && [1, 2, 3].includes(r.confidence) && unit.questions.some(q => q.variants.some(v => v.id === r.id && v.options.some(o => o.id === r.choice)))) && expected.size === 0;
  }
  function validateState(input, course) {
    const s = fresh();
    if (!object(input) || input.version !== VERSION) return s;
    if (ROLES.includes(input.role)) s.role = input.role;
    if (DEPTHS.includes(input.depth)) s.depth = input.depth;
    for (const unit of course.units) {
      if (Array.isArray(input.attempts?.[unit.id])) s.attempts[unit.id] = input.attempts[unit.id].filter(a => validAttempt(a, unit));
      const active = input.active?.[unit.id];
      if (object(active) && ['a', 'b'].includes(active.form) && Array.isArray(active.order) && active.order.length === unit.questions.length && new Set(active.order).size === unit.questions.length) {
        const expected = unit.questions.map(q => q.variants.find(v => v.form === active.form).id);
        if (active.order.every(id => expected.includes(id)) && (!unit.sequential || active.order.every((id, i) => id === expected[i]))) {
          const responses = [];
          for (const id of active.order) {
            const q = unit.questions.flatMap(c => c.variants).find(q => q.id === id), r = active.responses?.[responses.length];
            if (!r || r.id !== id || !q.options.some(o => o.id === r.choice) || ![1, 2, 3].includes(r.confidence)) break;
            responses.push(r);
          }
          s.active[unit.id] = { ...active, responses, feedback: responses.length === active.order.length || (responses.length > 0 && active.feedback === true), optionOrder: {} };
          for (const id of active.order) {
            const q = unit.questions.flatMap(c => c.variants).find(q => q.id === id), ids = q.options.map(o => o.id), old = active.optionOrder?.[id];
            s.active[unit.id].optionOrder[id] = Array.isArray(old) && old.length === ids.length && new Set(old).size === ids.length && old.every(id => ids.includes(id)) ? old : ids;
          }
        }
      }
      for (const section of unit.sections) if (input.checks?.[section.id] === true) s.checks[section.id] = true;
      if (typeof input.notes?.[unit.id] === 'string') s.notes[unit.id] = input.notes[unit.id].slice(0, 4000);
    }
    for (const q of [...course.baseline, ...course.cases.flatMap(c => c.steps)]) {
      const pool = course.baseline.includes(q) ? 'baseline' : 'cases', r = input[pool]?.[q.id];
      if (object(r) && q.options.some(o => o.id === r.choice) && [1, 2, 3].includes(r.confidence)) s[pool][q.id] = r;
    }
    if (object(input.legacy)) s.legacy = input.legacy;
    return s;
  }
  function load(storage, course) {
    let message = '', available = true, s = fresh();
    try {
      const raw = storage.getItem(KEY);
      if (raw) {
        try { const parsed = JSON.parse(raw); s = validateState(parsed, course); if (!object(parsed) || parsed.version !== VERSION) message = 'This saved record belongs to another edition. A fresh learning record is open; the original storage was not deleted.'; }
        catch { message = 'The saved record could not be read. You can continue with a fresh record; the original storage has not been deleted.'; }
      } else {
        try { const old = JSON.parse(storage.getItem('vikkypaedia-oxyvent-mastery-v2') || 'null'); if (object(old)) { s.legacy = { scores: object(old.scores) ? old.scores : {}, completed: Array.isArray(old.done) ? old.done.length : 0 }; message = 'Your previous-edition achievement is archived in My record. This substantially revised assessment starts a new record.'; } } catch { /* Old edition is optional. */ }
      }
    } catch { available = false; message = 'Browser storage is unavailable. Learning works for this session, but progress will not survive closing or refreshing. Export your record before leaving.'; }
    return { state: s, available, message };
  }
  function save(storage, state) { try { storage.setItem(KEY, JSON.stringify(state)); return true; } catch { return false; } }
  function summarize(unit, attempt) {
    if (!attempt) return null;
    const qs = unit.questions.flatMap(c => c.variants), responses = attempt.responses || [];
    let correct = 0, criticalMiss = false;
    const missed = [];
    for (const r of responses) { const q = qs.find(q => q.id === r.id); if (!q) continue; if (q.answer === r.choice) correct++; else { missed.push(q); if (q.critical) criticalMiss = true; } }
    const percent = Math.round(correct / unit.questions.length * 100);
    return { correct, total: unit.questions.length, percent, criticalMiss, passed: responses.length === unit.questions.length && percent >= 90 && !criticalMiss, missed };
  }
  const history = (state, unit) => state.attempts[unit.id] || [];
  const latest = (state, unit) => summarize(unit, history(state, unit).at(-1));
  const mastered = (state, unit) => latest(state, unit)?.passed === true;
  const unlocked = (state, course, unit) => course.units.slice(0, course.units.indexOf(unit)).every(u => mastered(state, u));
  const complete = (state, unit) => mastered(state, unit) && unit.sections.filter(s => s.depth === 'must').every(s => state.checks[s.id]);
  function start(state, course, unit) {
    if (!unlocked(state, course, unit)) return null;
    if (state.active[unit.id]) return state.active[unit.id];
    const form = history(state, unit).length % 2 === 0 ? 'a' : 'b';
    const ids = unit.questions.map(q => q.variants.find(v => v.form === form).id);
    const order = unit.sequential ? ids : shuffle(ids), optionOrder = {};
    for (const id of order) optionOrder[id] = shuffle(unit.questions.flatMap(q => q.variants).find(q => q.id === id).options.map(o => o.id));
    return state.active[unit.id] = { form, order, optionOrder, responses: [], started: new Date().toISOString(), feedback: false };
  }
  function submit(state, course, unit, choice, confidence) {
    const a = state.active[unit.id];
    if (!a || a.feedback || !unlocked(state, course, unit) || ![1, 2, 3].includes(confidence)) return false;
    const id = a.order[a.responses.length], q = unit.questions.flatMap(c => c.variants).find(q => q.id === id);
    if (!q || !q.options.some(o => o.id === choice)) return false;
    a.responses.push({ id, choice, confidence, time: new Date().toISOString() }); a.feedback = true; return true;
  }
  function advance(state, course, unit) {
    const a = state.active[unit.id];
    if (!a?.feedback || !unlocked(state, course, unit)) return false;
    if (a.responses.length === a.order.length) {
      (state.attempts[unit.id] ||= []).push({ form: a.form, responses: a.responses, started: a.started, finished: new Date().toISOString() });
      delete state.active[unit.id]; return 'finished';
    }
    a.feedback = false; return 'next';
  }
  root.OxyCore = { VERSION, KEY, ROLES, DEPTHS, fresh, shuffle, load, save, validateState, summarize, history, latest, mastered, unlocked, complete, start, submit, advance, allQuestions };
  if (typeof module !== 'undefined') module.exports = root.OxyCore;
})(typeof window !== 'undefined' ? window : globalThis);
