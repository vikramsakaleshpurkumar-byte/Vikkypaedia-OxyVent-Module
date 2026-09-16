import { roles } from './helpers.mjs';
import { sources } from './sources.mjs';
import { oxygen } from './oxygen.mjs';
import { foundations } from './foundations.mjs';
import { support } from './support.mjs';
import { advanced } from './advanced.mjs';
import { capstone,baseline,cases } from './capstone.mjs';
export const course={version:'2026.09.16.2',title:'Vikkypaedia OxyVent',roles,units:[...foundations,oxygen,...support,...advanced,capstone],sources,baseline,cases};
