# Vikkypaedia OxyVent

[Open the course](https://vikramsakaleshpurkumar-byte.github.io/Vikkypaedia-OxyVent-Module/) · [Offline edition](https://vikramsakaleshpurkumar-byte.github.io/Vikkypaedia-OxyVent-Module/offline.html)

A self-paced pediatric oxygenation and ventilation course for undergraduate medical students, nurses, PICU nurses and postgraduate trainees. Edition **2026.09.16**.

## Learning design

- Twelve connected units, 81 teaching sections and four role-specific responsibility lenses.
- Must / Good / Nice to Know depth: assessed teaching always remains in the core.
- Ten decisions per unit, two authored clinical forms (240 items), choice-specific feedback, confidence ratings and direct teaching links.
- Progression requires at least 90% and no safety-critical errors. The latest completed attempt determines current readiness; first and best performances remain visible. Later attempts repeat the two forms and are explicitly labelled practice.
- An optional clinical baseline, three guided patient journeys and an unfolding capstone.
- Local progress, reflection notes, exportable learning records and a generated single-file offline edition. No account, tracking or external runtime dependencies.

## Clinical scope

This is an **educational edition awaiting independent pediatric clinician review and learner-pilot testing**. It does not establish procedural competence or replace local protocols. Newborn resuscitation and drug prescribing are outside scope. The evidence library records the inspected scope, date and limitations of each source; institution-specific oxygen targets and HFNC protocols are labelled. Do not enter patient-identifying information.

## Maintain the course

Requires Node.js 22 or newer; no package installation is needed. Run **npm run build** and **npm test**.

Edit content/*.mjs for teaching, question pairs, cases and source provenance. core.js contains DOM-independent scoring, state validation and progression; app.js renders the interface and binds interactions; styles.css defines the responsive presentation. shell.html is the canonical page shell.

The build validates stable IDs, role coverage, source links, balanced answer positions, question variants and core-teaching mappings. It generates data.js, index.html, offline.html and build-report.json. Commit these outputs with source changes: GitHub Pages serves the repository root. The offline edition uses the same data, styles and engine. External references still require connectivity.

Tests cover score/safety rules, immutable first attempts, alternating forms, prerequisites, all-unit progression, refresh persistence and unavailable/corrupt storage. CI also checks that committed generated artifacts match their sources.

## Progress and accessibility

Progress stays in browser storage; file and online contexts may use separate storage. Legacy results are archived rather than credited against the revised question bank. Export a record before clearing browser data. The interface includes labelled controls, keyboard navigation, a focus-managed mobile drawer, reduced-motion support and print styles. Full assistive-technology testing remains part of the learner pilot.

## Completion certificate

The Certificate page is always visible and offers a clearly marked preview. All twelve current unit results must meet the score and safety standard to unlock a named completion certificate. Print / Save PDF uses the browser print dialog; Download SVG saves a scalable standalone certificate. It records self-directed educational completion, not accreditation or observed clinical competence. Names remain local.

The reference library filters by unit and links back to related teaching. Lesson checkpoints show core explain-back progress.
