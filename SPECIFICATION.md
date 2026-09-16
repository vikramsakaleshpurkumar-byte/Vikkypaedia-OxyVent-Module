# OxyVent revision specification

## Approved direction

Implement the 15 September 2026 review in the existing static GitHub Pages module. Preserve the OxyVent identity, twelve-unit sequence, four audiences (UG, ward/emergency nurse, PICU nurse, PG), and 90% plus no safety-critical error pass policy. This specification resolves routine choices from the user's approval of the review.

## Learning and evidence

- Each unit: 3–5 observable outcomes, at least four substantive core sections, a worked example, role application, reflection and ten assessed decisions.
- Common core is visible for every role/depth. Role cards change responsibilities and application; deeper material is optional and never a prerequisite for core assessment.
- Each assessed concept has two authored clinical variants, ten decisions per form. Form A/B alternate on retries; subsequent use is explicitly labelled repeat practice. Capstone forms are sequential unfolding cases.
- Baseline: three clinical questions, optional, does not change unit gates.
- Confidence required before submission. First complete attempt, latest result, best score and historical pass are separately recorded. Latest complete attempt determines current mastery; a new unfinished attempt does not erase the previous result.
- Unit N requires every previous unit's current mastery. Required explain-back checks describe study completion separately from assessment mastery. They do not pretend to validate a practical skill.
- Source provenance includes inspected scope and review limitations. Clinical material is educational, awaiting independent clinician review; device examples are labelled by source and setting. No institutional approval or accreditation is implied.
- Sources verified during this revision: AHA/AAP 2025 pediatric BLS/ALS, NICE NG9 oxygen recommendation, RCH oxygen and HFNP guidance, PALICC-2 executive recommendations and FDA oximetry limitations. The original WHO book landing page is a further-reading reference, not a claim that the whole book was inspected.

## Architecture and release

Root entry point retained for existing GitHub Pages configuration. Canonical content in content/*.mjs; build generates data.js and offline.html. app.js owns accessible render/navigation, core.js owns testable state and scoring. Reuse the saved Module Builder patterns for safe rendering, source IDs, hash navigation, confidence, explain-back, progress and offline generation; adapt them to OxyVent's ten-question/safety-critical policy.

No framework, backend, analytics or accounts. No patient-identifying input. Progress remains in this browser; offline storage behavior depends on the browser. Legacy v2 completion stays archived as a previous-edition record and does not silently certify the revised bank. No old state key is deleted.

## Definition of done

Validate schema/IDs/source links/answer position distribution/core teaching coverage. Test first/latest/best, critical failures, direct-route guards, role/depth changes, resume, malformed/denied storage, baseline independence and capstone progression. Verify phone/tablet/desktop, keyboard focus, drawer, reduced-motion CSS, print rules and parity of offline assets. Provide the tested revision and reviewable delivery; name independent clinical review as outstanding.
