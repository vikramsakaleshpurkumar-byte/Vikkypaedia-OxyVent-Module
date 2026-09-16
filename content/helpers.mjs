export const roles = { ug: 'Undergraduate student', nurse: 'Ward / emergency nurse', picu: 'PICU nurse', pg: 'Postgraduate student' };
export function section(id, title, paragraphs, points = [], depth = 'must', sourceIds = []) { return { id, title, paragraphs, points, depth, sourceIds }; }
// A pair shares one decision construct but changes the clinical problem. IDs survive answer shuffling.
export function pair(unit, number, sectionId, stems, options, why, critical = false, sourceIds = []) {
  const concept = `${unit}-q${String(number).padStart(2, '0')}`;
  return { id: concept, sectionId, variants: stems.map((stem, index) => {
    const values = options.map((o, i) => ({ id: `${concept}-o${i}`, text: o[0], feedback: o[1] }));
    const shift = (number + index) % 4;
    const ordered = values.slice(shift).concat(values.slice(0, shift));
    return { id: `${concept}-${index ? 'b' : 'a'}`, form: index ? 'b' : 'a', stem, options: ordered, answer: values[0].id, why, critical, sourceIds, sectionId };
  }) };
}
export function single(id, stem, options, why, sourceIds, critical = false) {
  const opts = options.map((o, i) => ({ id: `${id}-o${i}`, text: o[0], feedback: o[1] }));
  const shift = [...id].reduce((n,c)=>n+c.charCodeAt(0),0)%4;
  return { id, stem, options: opts.slice(shift).concat(opts.slice(0,shift)), answer: opts[0].id, why, sourceIds, critical };
}
export function decisions(unit, rows) {
  return rows.map((r,i)=>pair(unit.id,i+1,`${unit.id}-${r[0]}`,[r[1],r[2]],r.slice(3,7).map(t=>t.split('~')),r[7],!!r[8],unit.sections.find(s=>s.id===`${unit.id}-${r[0]}`).sourceIds));
}
