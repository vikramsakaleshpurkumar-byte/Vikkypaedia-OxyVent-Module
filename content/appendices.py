"""Appendices A–G for OxyVent: Oxygen and Ventilation. Reuses the Standard's generic
faculty material (C3–C6, PEARLS, G) and adds topic-specific content."""
import os, re
from gen import table, box
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "build", "80_appendices.html")
STD = os.path.join(HERE, "_standard_appendix_source.html")   # NRP-2025 v1.5 appendices — source of the shared faculty and design blocks
std = open(STD, encoding="utf-8").read().split("\n")
pearls = "\n".join(std[242:266]).replace("where the blender was", "where the oxygen cylinder and the self-inflating bag were")
appC_generic = "\n".join(std[271 - 1 + 32:271 - 1 + 111 - 4])   # C3 … C6, without closing divs
appG = "\n".join(std[597:666])

def app(letter, title, body):
    return '''
<!-- ===================================================== APPENDIX %s -->
<div class="appendix" id="app%s">
  <h3><span class="caret">▸</span>%s · %s</h3>
  <div class="app-body">
%s
  </div>
</div>
''' % (letter, letter, letter, title, body)

# ------------------------------------------------------------------ A
A = """    <h4>A1 · Blueprint against Miller's pyramid</h4>
    <p>No single instrument samples all four levels. This is what each part of the programme can honestly claim.</p>
""" + table(["Miller level", "What it means", "Instrument here", "Weight"],
  [["<b>Knows</b>", "Recalls thresholds, targets, formulae", "Unit checkpoints; final assessment", "~25%"],
   ["<b>Knows how</b>", "Applies knowledge to a clinical problem", "Case-vignette checkpoints; integrative items; key-feature problems", "~45%"],
   ["<b>Shows how</b>", "Demonstrates in simulation", "OSCE stations (A3); scenarios (Appendix B); DOPS", "~20%"],
   ["<b>Does</b>", "Performs in real practice", "Mini-CEX, CBD, MSF, entrustment (A4)", "~10%"]]) + box("pitfall", "What the written assessment cannot do", "<p>The certificate covers only the top two rows. Bag-mask ventilation, CPAP set-up and ventilator checks are physical skills: anyone using this module for a consequential decision must add observed practice on a manikin and at the bedside.</p>") + """
    <h4>A2 · Key-feature problems</h4>
    <p>Short answers, no options. They test only the decisions on which the case turns. Use them in remediation clinics and vivas.</p>
    <h5 class="sub">KF1 — The quiet child on oxygen</h5>
    <p><i>A 6-year-old after a prolonged seizure is on a face mask at 8 L/min. SpO₂ 99%. Respiratory rate 8/min, responds only to pain.</i></p>
    <ol>
      <li><b>What is threatened, and how will you know?</b><br><small>Model: ventilation, not oxygenation; oxygen is hiding it. Check airway, chest movement, EtCO₂ or a blood gas.</small></li>
      <li><b>What do you do now?</b><br><small>Model: open the airway, support breaths with bag-mask if inadequate, call for help; do not rely on SpO₂.</small></li>
    </ol>
    <h5 class="sub">KF2 — The infant on high-flow</h5>
    <p><i>A 4-month-old with bronchiolitis on high-flow for 2 hours: heart rate 180 → 190/min, respiratory rate 70 → 76/min, FiO₂ 0.4 → 0.6, one apnoea.</i></p>
    <ol>
      <li><b>Success or failure?</b><br><small>Model: failure &mdash; rising rates, rising FiO₂, apnoea.</small></li>
      <li><b>Next step?</b><br><small>Model: escalate to CPAP or intubation per local plan; call PICU or arrange transfer now.</small></li>
    </ol>
    <h5 class="sub">KF3 — The transfer</h5>
    <p><i>A child on 5 L/min needs a 2-hour road transfer. One 680 L cylinder, full.</i></p>
    <ol>
      <li><b>How long will it last, and what do you need?</b><br><small>Model: 680 ÷ 5 = 136 min; plan for 240 min (1200 L), so at least one more full cylinder.</small></li>
      <li><b>What else must travel with the child?</b><br><small>Model: self-inflating bag and mask, suction, oximeter, trained escort, written handover, accepting team informed.</small></li>
    </ol>
    <h5 class="sub">KF4 — The ventilated child who worsens</h5>
    <p><i>A ventilated 3-year-old is turned; SpO₂ falls to 75%, high-pressure alarm, suction catheter will not pass.</i></p>
    <ol>
      <li><b>Most likely cause?</b><br><small>Model: obstruction of the tube (DOPES: O).</small></li>
      <li><b>What do you do?</b><br><small>Model: call for help, hand-ventilate; if it cannot be cleared, remove the tube, bag-mask ventilate, reintubate by the most skilled person.</small></li>
    </ol>

    <h4>A3 · OSCE stations</h4>
    <p>Twelve stations, 6&ndash;8 minutes each, on a manikin with printed vital-sign cards. Score with the six-domain rubric in Appendix C.</p>
""" + table(["#", "Station", "Tests", "Critical failure"],
  [["1", "Recognise distress versus failure from a video or actor", "Category and first move", "Calls a drowsy child with slow breathing &lsquo;settled&rsquo;"],
   ["2", "Pulse oximetry: probe, waveform, interpretation", "Signal quality, target, action", "Acts on a number from a poor waveform"],
   ["3", "Write an oxygen prescription", "Device, flow, target, reassessment, failure trigger", "No target or no reassessment"],
   ["4", "Oxygen system check: cylinder, regulator, concentrator", "Contents calculation, leaks, backup", "Cannot calculate cylinder duration"],
   ["5", "Bag-mask ventilation, one- and two-person", "Position, seal, rate, chest rise", "No chest rise, not corrected"],
   ["6", "Set up and start high-flow", "Flow by weight, humidification, success and failure signs", "No failure plan"],
   ["7", "Assemble and start bubble CPAP", "Prongs, bubbling, pressure, monitoring", "No bubbling, not noticed"],
   ["8", "Prepare for intubation", "Checklist, physiology, roles, rescue plan", "No resuscitation of the shocked child before induction"],
   ["9", "Acute asthma: first hour", "Bronchodilator, steroid, magnesium dose, escalation", "Misses a silent chest"],
   ["10", "Read the ventilator: peak, plateau, flow curve", "Resistance vs compliance, air trapping", "Raises the rate in air trapping"],
   ["11", "DOPES drill", "Hand-bag, systematic check, team roles", "Keeps ventilating through a blocked tube"],
   ["12", "Home-oxygen teaching, with an actor parent", "Target, fire safety, power backup, when to return", "No fire safety"]]) + """
    <h4>A4 · Workplace-based assessment</h4>
""" + table(["Tool", "Use it for", "Frequency", "Note"],
  [["<b>Mini-CEX</b>", "An observed respiratory assessment and oxygen decision", "2&ndash;4 per learner per year", "The feedback is the intervention"],
   ["<b>DOPS</b>", "Bag-mask ventilation, bubble CPAP set-up, high-flow set-up, ventilator safety check", "Until entrustment, then annually", "Score the procedure, not the person"],
   ["<b>CBD</b>", "Reasoning behind an escalation decision the learner made", "2&ndash;3 per year", "Ask &ldquo;what would have made you escalate earlier?&rdquo;"],
   ["<b>MSF</b>", "Teamwork and communication, from nurses and peers", "Annual", "Detects the behaviours that cause harm"]]) + """
    <h5 class="sub">Entrustment scale for the core EPA</h5>
    <p><b>EPA:</b> <i>Assess a child with respiratory distress, start and monitor appropriate oxygen or non-invasive support, recognise failure and escalate safely.</i></p>
""" + table(["Level", "Descriptor"],
  [["1", "Observes only"], ["2", "Performs with direct supervision"], ["3", "Performs with indirect supervision, supervisor reachable within minutes"],
   ["4", "Performs unsupervised; supervisor available for the unexpected"], ["5", "Supervises and teaches others"]]) + """
    <p><b>Suggested minimum for a doctor or nurse covering a paediatric ward alone at night:</b> level 4 for oximetry, oxygen prescription and bag-mask ventilation; level 3 or above for high-flow and bubble CPAP. Intubation and ventilator management remain supervised unless your institution has credentialed you.</p>"""

# ------------------------------------------------------------------ B
def scenario(n, title, setup, stages, points):
    rows = "".join("<tr><td class='num'>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % s for s in stages)
    return '''    <h4>Scenario %d — %s</h4>
    <p>%s</p>
    <div class="tw"><table class="reflow"><thead><tr><th class="num">Stage</th><th>Vital-sign card</th><th>Expected actions</th><th>Facilitator trigger</th></tr></thead><tbody>%s</tbody></table></div>
    <p><b>Debrief points:</b> %s</p>
''' % (n, title, setup, rows, points)

B = """    <p>Four branching scenarios that run on a manikin and printed vital-sign cards &mdash; no simulator needed. Show the next card only when the team has done, or clearly failed to do, the expected actions.</p>
""" + scenario(1, "Pneumonia at a district hospital",
  "District hospital, 11 p.m. A 14-month-old, 9 kg, cough and fever 3 days. One doctor, two nurses. Concentrator and cylinders; bubble CPAP kit; no ventilator.",
  [("1", "RR 58, recession, SpO₂ 86% in air, alert", "Oxygen by prongs to target; antibiotics; reassess in 30&ndash;60 min", "If no target written: &ldquo;The nurse asks what saturation she should aim for.&rdquo;"),
   ("2", "SpO₂ 89% on 2 L/min, RR 64, grunting", "Start bubble CPAP with monitoring and a failure plan", "If oxygen flow is simply increased: next card, SpO₂ 88%, drowsy"),
   ("3", "Drowsy, shallow breathing, one apnoea", "Recognise failure; bag-mask if needed; call referral PICU; transfer with oxygen calculation", "Power cut: concentrator stops &mdash; is the backup cylinder ready?")],
  "a target and failure trigger for every support; the power cut as a system test; transfer as a treatment.") + scenario(2, "The infant on high-flow",
  "Paediatric ward. A 3-month-old, 5.5 kg, bronchiolitis day 3, on high-flow 11 L/min, FiO₂ 0.4.",
  [("1", "HR 175, RR 66, SpO₂ 93%", "Check flow for weight, humidification, nasal suction; reassess in 1 h", "Parent asks for &ldquo;the nebuliser&rdquo;"),
   ("2", "HR 190, RR 76, FiO₂ 0.6, apnoea 20 s", "Recognise failure; stimulate, bag-mask if needed; escalate (CPAP or PICU)", "If the team waits for the next scheduled review: second apnoea with bradycardia"),
   ("3", "On CPAP or awaiting PICU", "Handover with trend, support, response", "PICU asks: &ldquo;What was the FiO₂ trend over the last hour?&rdquo;")],
  "trajectory, not snapshot; bronchodilators not indicated; clear escalation.") + scenario(3, "Life-threatening asthma",
  "Emergency room. A 9-year-old, 28 kg, known asthma, 2 days of wheeze.",
  [("1", "Speaks in words, SpO₂ 90%, wheeze", "Oxygen, back-to-back salbutamol, ipratropium, systemic steroid", "If steroid delayed: next card unchanged at 20 min"),
   ("2", "Quiet chest, drowsy, SpO₂ 88%", "IV magnesium 40&ndash;50 mg/kg (max 2 g); senior help; prepare for intubation", "If magnesium dose is wrong: facilitator asks for the calculation"),
   ("3", "Intubated; hand-bagged fast; BP falling", "Recognise stacked breaths; disconnect, slower rate", "If the rate is increased: pulse becomes impalpable")],
  "the silent chest; magnesium dose; the danger of fast bagging.") + scenario(4, "The ventilated child who worsens",
  "PICU. A 2-year-old, 12 kg, PARDS on day 2, pressure-control ventilation. Moved for a chest X-ray.",
  [("1", "SpO₂ 74%, EtCO₂ waveform present, air entry louder on the right, tube at 14 cm (recorded 12 cm)", "Call help; hand-ventilate; recognise tube too deep; withdraw to recorded depth", "If the team increases FiO₂ only: SpO₂ 72%"),
   ("2", "SpO₂ 90% after correction", "Recheck air entry, secure tube, document", "Plateau pressure 32 cm H₂O: does the team lower the tidal volume?"),
   ("3", "Stable", "Debrief: movement checklist, fixation, depth recording", "&mdash;")],
  "EtCO₂ confirms the airway, not the depth; lung-protective limits; system learning.") + pearls

# ------------------------------------------------------------------ C
C = '''    <h4>C1 · Three delivery models</h4>
''' + table(["Model", "Shape", "Best for", "Watch out for"],
  [["<b>Fully self-paced</b>", "Learners work through alone; one skills session at the end", "Large cohorts, interns, CME", "The skills session becoming a demonstration. Cap at 6 learners per manikin."],
   ["<b>Flipped, Part by Part</b>", "Learners master a Part before each session; sessions are simulation and discussion", "PG residents, nursing cohorts", "Verify mastery first, or you end up teaching content"],
   ["<b>Intensive, 2 days</b>", "Parts A&ndash;C day one with simulation; D&ndash;E day two", "District outreach, visiting faculty", "Retention: schedule the review checks and a 6-week follow-up"]]) + '''
    <h4>C2 · A worked flipped-classroom session &mdash; Part C, non-invasive support</h4>
    <p>90 minutes, 8&ndash;12 learners, 2 manikins, 1 bubble CPAP kit, 1 high-flow device, 2 facilitators. Prerequisite: Units 8&ndash;11 mastered.</p>
''' + table(["Time", "Activity", "Purpose"],
  [["0&ndash;5", "Learning contract: &ldquo;Nobody here is being examined.&rdquo;", "Psychological safety"],
   ["5&ndash;15", "Rapid retrieval: high-flow success and failure signs; what the bubble CPAP trials showed; who is unsuitable for NIV", "Retrieval practice; shows where the cohort is"],
   ["15&ndash;35", "Deliberate practice: assemble bubble CPAP and set up high-flow by weight, in pairs, against the DOPS checklist", "The highest-yield practical skills in Part C"],
   ["35&ndash;55", "Scenarios 1 and 2 (Appendix B)", "Recognising failure of non-invasive support under time pressure"],
   ["55&ndash;75", "Debrief both runs, PEARLS, two points maximum", "Consolidation"],
   ["75&ndash;85", "The cylinder calculation on three cards, against the clock", "Makes the transfer calculation a habit"],
   ["85&ndash;90", "&ldquo;One thing to keep, one thing to change.&rdquo;", "Commitment to change"]]) + "\n" + appC_generic

C = C.replace("A cut score chosen by preference — including the 90%", "A cut score chosen by preference — including the 80%")
C = C.replace("&ldquo;a labour-room nurse who would reliably ventilate a flat baby within 60 seconds and recognise when it was not working, but would hesitate over an unfamiliar drug dose.&rdquo;",
              "&ldquo;a first-year resident or ward nurse who would reliably recognise respiratory failure, start oxygen to a target and give effective bag-mask breaths, but would hesitate over ventilator settings or lung-protective limits.&rdquo;")
C = re.sub(r"Delivery-room audit: time to PPV, DCC rate, routine suction rate, admission temperature", "Oxygen audit: oximetry on arrival, written SpO₂ targets, cylinder and concentrator checks, CPAP and high-flow failure plans", C)
C = C.replace("with a labour-room audit", "with an oxygen audit")
C = re.sub(r"Admission hypothermia, early neonatal mortality, HIE referrals within window", "Deaths in children with hypoxaemia, unplanned intubations, oxygen supply failures, unplanned extubations", C)

# ------------------------------------------------------------------ D
D = """    <p>Map each unit to the <b>competency descriptors</b> of the NMC CBME curriculum and to your nursing curriculum. The code column is deliberately blank: codes were revised in the September 2024 guidelines, and Volume II is the only authority. <b>Do not invent codes</b>; fill them in from the current document.</p>
""" + table(["Unit", "Competency descriptor (paraphrased)", "NMC code (verify)", "Domain", "Teaching method", "Assessment"],
  [["1&ndash;3", "Assess a child with respiratory distress; explain oxygenation and ventilation", "", "K, S", "Self-paced module; case discussion", "Checkpoints; CBD"],
   ["4&ndash;6", "Use pulse oximetry; prescribe, deliver and monitor oxygen safely", "", "K, S", "Skills lab; ward practice", "OSCE 2&ndash;4; DOPS"],
   ["7", "Give effective bag-mask ventilation", "", "S", "Skills lab", "OSCE 5; DOPS"],
   ["8&ndash;10", "Start and monitor high-flow, CPAP and non-invasive ventilation", "", "K, S", "Flipped session (C2)", "OSCE 6&ndash;7; DOPS"],
   ["11", "Prepare for safe intubation as a team member", "", "K, S, A", "Simulation", "OSCE 8"],
   ["12&ndash;16", "Manage bronchiolitis, pneumonia, asthma, upper-airway obstruction and PARDS", "", "K, S", "Case-based; simulation", "OSCE 9; KF1&ndash;2"],
   ["17&ndash;18", "Monitor a ventilated child; respond to sudden deterioration", "", "K, S", "Simulation; PICU attachment", "OSCE 10&ndash;11; KF4"],
   ["19", "Plan transfer, weaning and home oxygen; teach families", "", "S, A, C", "Role play", "OSCE 12; KF3"],
   ["20", "Integrate recognition, support and escalation across a case", "", "K, S, A", "Capstone case", "CBD; MSF"]]) + box("pitfall", "Why the code column is empty", "<p>Invented or outdated competency codes are worse than none &mdash; they propagate into curriculum documents and audits. Fill the column from NMC CBME Volume II (2024) and your nursing curriculum at your institution.</p>")

# ------------------------------------------------------------------ E
E = box("danger", "Verify before every use", "<p>Doses and settings here are drawn from the cited guidelines for learning. Check every dose against your institution's protocol, a current formulary and the child in front of you, and every device setting against the manufacturer's instructions. Where local protocol differs, follow local protocol. This annex is never locked.</p>") + """
    <h4>E1 · Oxygen and respiratory support</h4>
""" + table(["Item", "Guide", "Notes"],
  [["SpO₂ to start oxygen (WHO, sick child)", "Below 90%", "Higher (below 94%) if emergency signs; follow local targets"],
   ["SpO₂ to start oxygen (bronchiolitis, Australasian 2025)", "Persistently below 90% from 6 weeks; below 92% under 6 weeks or with underlying conditions", ""],
   ["Nasal prongs", "About 0.5 L/min in young infants; 1&ndash;2 L/min in older infants and children (WHO)", "Higher flows need humidification"],
   ["High-flow (one hospital's example)", "2 L/kg/min for the first 12 kg, plus 0.5 L/kg/min for each kg above", "Use your local protocol and device limits"],
   ["Bubble CPAP", "Start about 5 cm H₂O; titrate per local protocol", "Continuous bubbling confirms pressure"],
   ["Cylinder duration", "Litres left ÷ flow (L/min) = minutes", "Plan for twice the journey time"]]) + """
    <h4>E2 · Drugs</h4>
""" + table(["Drug", "Indication", "Dose", "Notes"],
  [["Salbutamol (MDI + spacer)", "Acute asthma", "Follow GINA or local protocol; one common regimen is 6 puffs (&lt;6 y) or 12 puffs (&ge;6 y) of 100 microgram every 20 min in the first hour", "Not for bronchiolitis in infants"],
   ["Ipratropium (nebulised)", "Severe acute asthma", "250 microgram (&lt;6 y) or 500 microgram, with salbutamol in the first hour", ""],
   ["Prednisolone / dexamethasone", "Acute asthma", "Prednisolone 1&ndash;2 mg/kg (max 40 mg) daily", "Early, oral if tolerated"],
   ["Magnesium sulphate IV", "Severe acute asthma", "40&ndash;50 mg/kg over 20 min, max 2 g", "Watch blood pressure"],
   ["Dexamethasone", "Croup", "0.15&ndash;0.6 mg/kg oral or parenteral", "Single dose"],
   ["Adrenaline 1 mg/mL, nebulised", "Moderate to severe croup", "0.5 mL/kg, max 5 mL", "Observe after &mdash; effect wears off in about 2 h"],
   ["Adrenaline 1 mg/mL IM", "Anaphylaxis", "0.01 mg/kg (0.01 mL/kg), max 0.5 mg", "Anterolateral thigh; repeat after 5 min"],
   ["Amoxicillin (oral)", "Pneumonia with chest indrawing, no danger signs (WHO 2024)", "Per WHO/national dosing", "Follow-up required"]]) + """
    <h4>E3 · Airway and ventilation</h4>
""" + table(["", "Formula or guide"],
  [["Tracheal tube (cuffed)", "(age/4) + 3.5 mm; oral depth ~3 &times; internal diameter (cm)"],
   ["Breaths with a pulse (AHA/AAP 2025)", "1 breath every 2&ndash;3 s (20&ndash;30/min)"],
   ["PARDS tidal volume (PALICC-2)", "About 6&ndash;8 mL/kg; below 6 if needed for pressure limits; caution below 4"],
   ["PARDS plateau / driving pressure", "&le;28 cm H₂O (29&ndash;32 with stiff chest wall) / &le;15 cm H₂O"],
   ["PARDS SpO₂ (mild&ndash;moderate)", "92&ndash;97%"],
   ["Permissive hypercapnia", "pH &ge;7.20, unless an exception applies (raised ICP, pulmonary hypertension, selected heart disease, instability)"]])

# ------------------------------------------------------------------ F
F = """    <h4>Primary guidelines &mdash; the sources this module is written to</h4>
    <ul>
      <li>World Health Organization. <b>Oxygen therapy for children: a manual for health workers.</b> Geneva: WHO; 2016.</li>
      <li>World Health Organization. <b>Guideline on management of pneumonia and diarrhoea in children up to 10 years of age.</b> Geneva: WHO; 2024.</li>
      <li>Emeriaud G, L&oacute;pez-Fern&aacute;ndez YM, Iyer NP, et&nbsp;al. <b>Executive summary of the second international guidelines for the diagnosis and management of pediatric acute respiratory distress syndrome (PALICC-2).</b> Pediatr Crit Care Med 2023;24(2):143&ndash;168.</li>
      <li><b>Part 8: Pediatric Advanced Life Support.</b> 2025 AHA/AAP Guidelines for CPR and ECC. Pediatrics 2026;157(1):e2025074351.</li>
      <li>Paediatric Research in Emergency Departments International Collaborative (PREDICT). <b>Australasian bronchiolitis guideline, 2025 update.</b></li>
      <li>Global Initiative for Asthma. <b>Global Strategy for Asthma Management and Prevention</b>, current report.</li>
      <li>Abu-Sultaneh S, Iyer NP, Fern&aacute;ndez A, et&nbsp;al. <b>Executive summary: international clinical practice guidelines for pediatric ventilator liberation, a PALISI Network document.</b> Am J Respir Crit Care Med 2023;207(1):17&ndash;28.</li>
      <li>Hayes D Jr, et&nbsp;al. <b>Home oxygen therapy for children: an official American Thoracic Society clinical practice guideline.</b> Am J Respir Crit Care Med 2019;199(3):e5&ndash;e23.</li>
      <li>World Health Organization. <b>Pocket book of hospital care for children</b>, 2nd edition. Geneva: WHO; 2013.</li>
    </ul>
    <h4>Key trials and studies worth reading in full</h4>
    <ul>
      <li>Franklin D, et&nbsp;al. <b>A randomized trial of high-flow oxygen therapy in infants with bronchiolitis (PARIS).</b> N Engl J Med 2018;378:1121&ndash;31.</li>
      <li>Franklin D, et&nbsp;al. <b>Effect of early high-flow nasal oxygen vs standard oxygen therapy on length of hospital stay in hospitalized children with acute hypoxemic respiratory failure (PARIS 2).</b> JAMA 2023;329(3):224&ndash;234.</li>
      <li>Chisti MJ, et&nbsp;al. <b>Bubble continuous positive airway pressure for children with severe pneumonia and hypoxaemia in Bangladesh.</b> Lancet 2015;386:1057&ndash;65.</li>
      <li>McCollum ED, et&nbsp;al. <b>Bubble continuous positive airway pressure for children with high-risk conditions and severe pneumonia in Malawi.</b> Lancet Respir Med 2019;7(11):964&ndash;974.</li>
      <li>Gebre M, et&nbsp;al. <b>Effectiveness of bubble CPAP for treatment of children aged 1&ndash;59 months with severe pneumonia and hypoxaemia in Ethiopia: a pragmatic cluster-randomised controlled trial.</b> Lancet Glob Health 2024. <a href="https://doi.org/10.1016/S2214-109X(24)00032-9">doi</a></li>
      <li>Sjoding MW, et&nbsp;al. <b>Racial bias in pulse oximetry measurement.</b> N Engl J Med 2020;383:2477&ndash;78.</li>
    </ul>
    <h4>Indian national and professional sources</h4>
    <ul>
      <li>Ministry of Health and Family Welfare. <b>National guidelines and technical specifications for medical oxygen</b>, including PSA plant operation and maintenance guidance.</li>
      <li>Indian Academy of Pediatrics. <b>Standard Treatment Guidelines</b>, including pneumonia, bronchiolitis and asthma.</li>
      <li>National Medical Commission. <b>Competency-Based Medical Education curriculum</b>, 2024 guidelines (Volume II for competencies).</li>
    </ul>
    <h4>Educational evidence base</h4>
    <ul>
      <li>Larsen DP, Butler AC, Roediger HL (2009) &mdash; test-enhanced learning in medical education. Cepeda NJ, et&nbsp;al. (2006) &mdash; distributed practice. Butterfield B, Metcalfe J (2001) &mdash; the hypercorrection effect.</li>
      <li>Stojan J, et&nbsp;al. <b>BEME Guide No. 69</b> &mdash; technology-enhanced learning in health professions education.</li>
      <li><b>Ottawa 2020 Consensus Statements</b> on programmatic assessment. McKinley RK, Norcini JJ. <b>AMEE Guide No. 85</b> &mdash; standard setting.</li>
    </ul>
""" + box("danger", "Check the edition before you teach from anything", "<p>Respiratory guidance changes often: bronchiolitis in 2025, resuscitation in 2025, pneumonia in 2024, paediatric ARDS in 2023, and asthma every year. Before using any figure from this module in teaching or a protocol, confirm it against the current edition of the primary source. If you are reading this more than three years after the build date in the footer, assume something here is out of date and check.</p>")

# ------------------------------------------------------------------ G (generic, adapted)
G = appG
G = G.replace("sample 50 items from a pool of 78", "sample 50 items from a pool of 70")
G = G.replace("This module has no evidence that it changes delivery-room behaviour or neonatal outcomes.", "This module has no evidence yet that it changes bedside respiratory care or child outcomes.")
G = G.replace("WHO guidance on newborn care", "WHO oxygen-therapy and hospital care guidance for children")
G = G.replace("Part D is unintelligible without Part C", "Part C's escalation decisions make no sense without Part A's difference between oxygenation and ventilation")
# strip wrapper lines from the NRP block so we can re-wrap consistently
G = G[G.index('<div class="app-body">') + len('<div class="app-body">'):]
G = G[:G.rindex("</div>\n</div>")] if "</div>\n</div>" in G else G

head = '''<section class="part" id="appendices">
  <div class="part-head">
    <div>
      <span class="pk">Appendices</span>
      <h2>Appendices A&ndash;G</h2>
    </div>
    <span class="part-meta"><span class="app-open-note">Never locked</span></span>
  </div>
  <p class="part-lede">Open from the first minute, whatever your progress. Appendix E (drugs, oxygen and equipment) and Appendix F (references) are clinical safety material, and clinical safety material behind a quiz is a patient-safety problem. Every appendix can be printed on its own.</p>
'''
html = head + app("A", "Assessment bank", A) + app("B", "Simulation library", B) + app("C", "Faculty guide", C) + \
       app("D", "Curriculum mapping", D) + app("E", "Drug, oxygen and equipment annex", E) + app("F", "References", F) + \
       app("G", "Evidence-governed design", G) + "\n</section>\n"
open(OUT, "w", encoding="utf-8").write(html)
print("wrote", OUT, len(html) // 1024, "KB")
for bad in ["neonat", "NRP", "newborn", "PPV", "labour"]:
    n = len(re.findall(bad, html, re.I))
    if n: print("  check:", bad, n)
