# OxyVent: Oxygen and Ventilation

**Live:** https://vikramsakaleshpurkumar-byte.github.io/Vikkypaedia-OxyVent-Module/
**All Vikkypaedia modules:** https://vikramsakaleshpurkumar-byte.github.io/

A mastery-based, self-paced module on oxygen, non-invasive support and ventilation for children, from the pulse oximeter to the ventilator. It is aligned to the **WHO manual *Oxygen therapy for children* (2016)**, **PALICC-2 (2023)**, **AHA/AAP PALS 2025**, the **WHO pneumonia and diarrhoea guideline (2024)**, the **Australasian bronchiolitis guideline (2025 update)** and **GINA**, and it is read across the resource gradient.

**Version 4.0.0** (built 2026-09-24) is a complete rebuild on the Vikkypaedia Standard engine (v2.1). It expands the earlier 12 units to 20 and adds the common diseases. Progress from the earlier edition is not carried over, because the units and questions have changed; learners who used it see a one-time notice.

## What it is

- One self-contained HTML file. No CDN, no framework, no network request. It works offline on a phone.
- 20 units in 5 Parts, about 26 notional hours. It has 40 checkpoint questions with two-tier hints and rationales that explain why the wrong options are wrong, plus 30 fresh integrative items for the final assessment.
- Parts: **A** Foundations (the child before the number; distress and failure; oxygenation is not ventilation) · **B** Measure and give oxygen (oximetry, prescription, oxygen systems, bag-mask) · **C** Respiratory support (high-flow, CPAP and bubble CPAP, NIV, safer intubation) · **D** The diseases (bronchiolitis, pneumonia, asthma, upper-airway obstruction, paediatric ARDS) · **E** Ventilation and systems (reading the ventilator, DOPES, transport, weaning, home oxygen, capstone).
- **Every unit opens with a "Your role" box** for the four audiences: student, ward nurse, PICU nurse and PG resident. It says what each should take from the unit and does not authorise any procedure beyond training and local policy.
- Every clinical unit has an **India lens**. Where management genuinely differs, it has **ideal and resource-constrained panels** side by side.
- Two diagrams: the **escalation ladder** and the **DOPES check**, each with a text version.

## Who it is for

| Learner | Default depth |
|---|---|
| Students, interns, ward nurses | Essentials: Parts A–C |
| PG residents, medical officers, PICU nurses | Advanced: Parts A–D |
| Paediatricians, intensivists, faculty | Expert: all 20 units and appendices |

## The safety rule (new in this module)

About a third of the assessment pool (20 checkpoints and 10 fresh items) is marked **safety-critical**: items where a wrong choice could kill a child, such as a displaced tube, a failing CPAP trial or running out of oxygen on the road. **An exam attempt with any safety-critical miss does not count towards the applied criterion, whatever its score.** The rule is switched on by `safetyGate: true` in `build/05_module.html`; other modules leave it off.

## What makes it different

- **Mastery, never completion.** A unit is mastered when both of its checkpoints are currently correct.
- **Part-by-Part unlocking**, and experienced clinicians can clear Parts by challenge.
- **Spaced retrieval** at 1, 3, 7, 21 and 60 days, with a review queue and a due badge.
- **Confidence-weighted answering**, with "confident and wrong" flagged and calibration shown.
- **A next-step card**, a study-days strip that never shames, and short notices when a unit or Part is earned. No points, badges or leaderboards.
- **The Vikkypaedia Passport**: one learner profile and one progress summary across every module on this site, with no server.
- **The drug, oxygen and equipment annex is never locked**, and any appendix can be printed.

## Certification

1. **Coverage:** all 40 checkpoints currently correct.
2. **Retention:** at least 15 of the 20 units evidenced by an item answered correctly 24 hours or more after first passing it.
3. **Applied performance:** a closed-book assessment of 50 items (from a pool of 70) in 75 minutes, 2 attempts, a 24-hour lock between attempts, a **provisional** 80% cut score, and the safety rule above.

**Set your own cut score** with the Angoff, Ebel and Hofstee worksheets in Appendix C before any consequential use. The certificate carries a default signature for Dr Vikram Sakaleshpur Kumar (Great Vibes script, SIL Open Font License), replaceable in Faculty settings.

## About the earlier question bank

The earlier edition had 120 multiple-choice questions. They were **not** carried over: in 83 of them the correct answer was the longest option, a cue that lets test-wise learners score without knowing the content, and many distractors were implausible. The checkpoints and the 30 fresh integrative items were written new, and option order is shuffled on every attempt.

## Enrolment and completion records

A four-step first run collects the learner's name and plan, stored in the browser only. The learner can download a JSON **completion record**, and `verify.html` checks it offline. **Records are self-attested:** a checksum match shows the record was not casually altered, not that the learner sat the assessment.

## Faculty adoption

1. Final assessment → Faculty settings: set the signatory, signature image, cut score and retention bar, then **Export a configured copy** and publish it as `index.html`.
2. Appendix A: blueprint, four key-feature problems, 12 OSCE stations (oximetry, oxygen prescription, cylinder check, bag-mask, high-flow, bubble CPAP, intubation preparation, asthma, ventilator reading, DOPES drill, home-oxygen teaching), WPBA tools and an entrustment scale.
3. Appendix B: four branching scenarios on a manikin with printed vital-sign cards (pneumonia at a district hospital, the infant on high-flow, life-threatening asthma, the ventilated child who worsens).
4. Appendix C: delivery models, a worked flipped session on Part C and the standard-setting worksheets.

## Rebuilding and testing it

```bash
python content/build_content.py   # units 1–20 from content/*.py → build/20_…60_*.html
python content/appendices.py      # Appendices A–G → build/80_appendices.html
python build.py                   # assemble index.html with structural assertions
python tests/test_full.py; python tests/test_ui.py; python tests/test_enrol.py
python tests/test_search.py; python tests/test_sig.py; python tests/test_loops.py
python tests/test_gate.py         # the safety rule
python tests/contrast.py; python tests/offline_test.py; python tests/print_test.py
```

`build/05_module.html` holds every module-specific engine value. `build/85_examitems.html` holds the fresh items; `C(...)` marks a safety-critical one. `content/balance.py` balances the checkpoint answer key (10 A, 10 B, 10 C, 10 D).

## Privacy

Everything is stored in the learner's browser. There is no account, no server, no analytics and no telemetry.

## Known limitations

- Reading this module does not make anyone competent to ventilate a child. Every practical skill needs supervised practice.
- Fixed Leitner intervals, not fitted forgetting curves. Two checkpoints per unit is thin sampling.
- The safety rule is strict by design; faculty may find it too strict for formative use and can switch it off.
- The assessment is unproctored, completion records are self-attested and the cut score is provisional.
- High-flow rates, CPAP pressures and oxygen targets vary by hospital and device; the module gives named examples, not universal prescriptions.
- Oximeter accuracy across skin tones is still being addressed by regulators; the module teaches caution, not a correction factor.
- Kirkpatrick levels 3 and 4 are unmeasured. Accessibility targets WCAG 2.2 AA but has not been independently audited. The clinical content has not been externally peer reviewed.
- NMC CBME codes are deliberately left blank in Appendix D.

## Contributing, licence and citation

See `CONTRIBUTING.md`: clinical corrections come first and need primary sources. Licensed CC BY-NC-SA 4.0, **excluding** the Vikkypaedia name, the name and likeness of Dr Vikram Sakaleshpur Kumar, and the certificate signature block (see `LICENSE.md`).

> Sakaleshpur Kumar V. *OxyVent: Oxygen and Ventilation — an evidence-governed, mastery-based digital module for children's respiratory support.* Vikkypaedia; 2026. Available from: https://vikramsakaleshpurkumar-byte.github.io/Vikkypaedia-OxyVent-Module/

## Disclaimer

This module is education, not a clinical protocol, and not certification to practise. Verify every dose and device setting against your institution's protocol, a current formulary and the manufacturer's instructions.
