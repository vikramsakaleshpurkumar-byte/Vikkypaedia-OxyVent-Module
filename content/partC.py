from gen import *

part("C", "Respiratory support", "Units 8&ndash;11 · ~5 hours",
     "When oxygen is not enough, the next step is distending pressure &mdash; then assisted breaths &mdash; then an airway. Each step helps the right child and harms the wrong one. The trials of the last decade (PARIS, PARIS 2, the bubble-CPAP trials) are the reason this Part is as much about <i>who not to treat</i> as about how.")

# ------------------------------------------------------------------ UNIT 8
unit(8, "C", "High-flow nasal cannula",
  "High-flow is a genuinely useful tool that has become a reflex. The trials show it helps some children who fail standard oxygen, and does nothing but lengthen the stay when started early in mildly hypoxaemic ones.",
  [("e", "Explain what high-flow nasal cannula does: heated, humidified flow that meets inspiratory demand, washes out dead space and gives modest distending pressure."),
   ("e", "Set up and monitor a high-flow trial with explicit success and failure criteria."),
   ("a", "Use the PARIS and PARIS 2 trials to decide when high-flow is and is not indicated."),
   ("x", "Plan weaning, feeding and transport for a child on high-flow.")],
  [
   roles({"ug": "Explain what flow and FiO₂ are each meant to change, and how you would judge the response.",
          "nurse": "Check the prescription, circuit, fit, humidification and observations; report failure signs promptly.",
          "picu": "Trend effort, gas exchange, interface and supply performance; plan safe transport and monitoring.",
          "pg": "Select a suitable, monitored patient; state targets and failure criteria; escalate before deterioration is prolonged."}),
   sec(1, "High-flow is a system, not a higher wall flow", '''
  <p>High-flow nasal cannula (HFNC) delivers <b>heated, humidified gas at high flow</b> through a designed circuit and cannula. The flow meets the child's inspiratory demand, washes CO₂ out of the nasopharynx and gives a modest, variable distending pressure. FiO₂ is titrated separately to the oxygenation target. Ordinary prongs turned up on a wall flowmeter are <b>not</b> high-flow &mdash; dry, cold gas at high flow damages the nose and is poorly tolerated.</p>
  <p>The cannula should occupy about half the nostril, leaving a leak. Neither the flow display nor a comfortable child proves that ventilation is adequate.</p>'''),

   sec(2, "What the trials show", evidence('''<p><b>PARIS</b> (Franklin et al., <i>NEJM</i> 2018): in infants under 12 months with bronchiolitis and hypoxaemia on general wards, high-flow reduced the need for <b>escalation of care</b> compared with standard oxygen, without reducing ICU length of stay or ventilation. A common reading: high-flow is a useful <b>rescue</b> for infants failing standard oxygen.</p>
  <p><b>PARIS 2</b> (Franklin et al., <i>JAMA</i> 2023): in 1,567 children aged 1&ndash;4 years with acute hypoxaemic respiratory failure, <b>early</b> high-flow compared with standard oxygen <b>lengthened hospital stay</b> (median about 1.8 vs 1.5 days), prolonged oxygen therapy, and was associated with more ICU admissions (about 13% vs 7%).</p>
  <p><b>The Australasian bronchiolitis guideline (2025)</b>: do not use high-flow routinely in infants with mild or moderate bronchiolitis who are not hypoxaemic; reserve it for infants who fail low-flow oxygen or who have severe disease, before CPAP.</p>''', "Read the trials before you reach for the device") + pitfall('''<p><b>Indication creep.</b> Starting high-flow in a mildly hypoxaemic child because it is available &mdash; and then keeping them on it, in hospital, longer. Start with standard oxygen; move to high-flow when standard oxygen is failing.</p>''')),

   sec(3, "Setting up a monitored trial", '''
  <p>Before starting, agree the <b>indication</b>, <b>target</b>, <b>responsible clinician</b>, <b>observations</b> and <b>failure plan</b>. Check airway protection, apnoea and circulation. A failing or unstable child needs senior review, not an unmonitored trial that postpones definitive support.</p>''' + table(
     ["Weight", "One published example flow (Royal Children's Hospital, Melbourne)"],
     [["Up to 12 kg", "2 L/kg/min"],
      ["Over 12 kg", "24 L/min for the first 12 kg, plus 0.5 L/kg/min for each kg above 12, up to 50 L/min"]]) + '''
  <p class="dash-status">These are one hospital's teaching values, not a universal prescription. Use your local protocol and the device limits. Example: a 6 kg infant &rarr; 12 L/min; a 16 kg child &rarr; 24 + (4 &times; 0.5) = 26 L/min.</p>''' + algo("Success or failure: decide from the trajectory", '''  SUCCESS within 1–2 hours:  heart rate and respiratory rate falling
                             less recession · better interaction
                             FiO2 requirement falling
  FAILURE:  rising FiO2 (e.g. above 0.5–0.6) · worsening effort
            recurrent apnoea · drowsiness · rising CO2
            haemodynamic instability
  → escalate NOW (CPAP, senior review, PICU) — do not wait for
    the end of the planned observation window''')),

   sec(4, "Care, weaning and transport", '''
  <ul>
    <li>Check nares and skin, circuit position, humidifier water, secretions and abdominal distension.</li>
    <li>Feeding depends on stability; many units allow cautious oral or nasogastric feeds on high-flow. Do not assume a nasal interface makes feeding safe during deterioration.</li>
    <li>Wean when improvement is sustained, not because a bed is needed. Protocols differ (step-down flows versus stopping directly) &mdash; name the protocol you follow.</li>
    <li>For transport: confirm power, gas consumption and a backup. High-flow systems can use a lot of oxygen (Unit 6).</li>
  </ul>''', tier="good", lvl="a"),

   sec(5, "Across settings", tracks(
     ["Dedicated high-flow devices with integrated humidification and blenders; ward protocols with PICU outreach",
      "Continuous oximetry and trained nursing ratios for high-flow patients"],
     ["High-flow needs a blender or a device that can deliver air and oxygen mixtures, reliable power and a large oxygen supply &mdash; many district hospitals will do better with bubble CPAP (Unit 9)",
      "If you have high-flow but no rapid escalation, treat any sign of failure as a trigger for early transfer",
      "Never improvise high-flow with ordinary prongs and wall oxygen at high flow"])),
  ],
  [Q("A 2-year-old with pneumonia is on the ward with SpO₂ 91% in room air, mild recession and good feeding. The unit has a new high-flow device. What does the evidence support?",
     ["Start high-flow now because it is available and prevents deterioration.",
      "Start standard low-flow oxygen; reserve high-flow for failure of standard oxygen.",
      "No oxygen, because 91% is normal.",
      "Start CPAP immediately."],
     1,
     "What happened in PARIS 2 when high-flow was started early in children of this age?",
     "Early high-flow in 1&ndash;4-year-olds lengthened hospital stay and was associated with more ICU admission. What is the sensible first step for a mildly hypoxaemic child?",
     "PARIS 2 found that <b>early high-flow</b> in children aged 1&ndash;4 with hypoxaemic respiratory failure lengthened hospital stay without benefit. Start <b>standard oxygen</b> and keep high-flow for children who fail it.",
     "<b>A</b> &mdash; availability is not an indication. <b>C</b> &mdash; many clinicians would give oxygen at 91% with distress; the point is which device, not whether. <b>D</b> &mdash; CPAP is for more severe disease or high-flow failure.",
     "The newest device on the ward is not the first-line treatment.",
     "section 2, ‘What the trials show’"),
   Q("A 7-month-old with bronchiolitis has been on high-flow at 2 L/kg/min for 90 minutes. FiO₂ has risen from 0.35 to 0.6, recession is worse, and she has had two apnoeas. What should happen now?",
     ["Continue high-flow and review at the end of the 4-hour trial window.",
      "Increase flow to 4 L/kg/min and wait.",
      "Recognise high-flow failure: call senior help now and escalate to CPAP or ventilation, with PICU involvement.",
      "Stop high-flow and return to 1 L/min prongs."],
     2,
     "Which way are FiO₂, effort and apnoea moving?",
     "Rising oxygen need, worsening effort and apnoeas are failure criteria. Should they wait for the end of a planned window?",
     "Rising FiO₂, worsening recession and apnoeas are <b>failure criteria</b>. Escalate now &mdash; CPAP or ventilation with senior and PICU involvement. Clinical deterioration overrides the planned trial duration.",
     "<b>A</b> &mdash; waiting prolongs failure. <b>B</b> &mdash; doubling the flow beyond protocol is not a substitute for escalation and is poorly tolerated. <b>D</b> &mdash; stepping down support in a failing infant is dangerous.",
     "Write the failure criteria before you start. Then act on them when they appear.",
     "section 3, ‘Setting up a monitored trial’", critical=True)]
)

# ------------------------------------------------------------------ UNIT 9
unit(9, "C", "CPAP and bubble CPAP",
  "Bubble CPAP can be made from a length of tubing and a bottle of water, and in the right hands it keeps children off ventilators. In the wrong system, one trial found more children died. The difference is the system, not the bubbles.",
  [("e", "Explain how CPAP helps: it holds alveoli and the upper airway open and reduces work of breathing."),
   ("e", "Set up and monitor bubble CPAP safely, including the checks that show it is working."),
   ("a", "Interpret the bubble CPAP trials from Bangladesh and Malawi, and the 2024 Ethiopian trial, and decide what they mean for your unit."),
   ("x", "Recognise when CPAP is failing and plan escalation where no ventilator is available.")],
  [
   roles({"ug": "Explain why continuous pressure keeps collapsing alveoli open, and how you would know it is working.",
          "nurse": "Check bubbling, water level, prong position, nasal skin and gastric distension; escalate worsening effort or apnoea.",
          "picu": "Relate pressure delivery to leak, interface and the child's effort; recognise failure early.",
          "pg": "Select children who will benefit, define failure criteria and plan escalation or transfer before they are needed."}),
   sec(1, "What CPAP does", '''
  <p>Continuous positive airway pressure (CPAP) keeps a set pressure in the airway throughout the breath. It <b>holds collapsing alveoli open</b> (improving oxygenation in pneumonia and bronchiolitis), <b>splints the upper airway</b> and <b>reduces work of breathing</b>. It does not deliver breaths: a child who is apnoeic or cannot breathe needs assisted ventilation.</p>''' + algo("How bubble CPAP works", '''  oxygen / air blend ──► humidifier ──► nasal prongs ──► child
                                                  │
                          expiratory limb ◄────────┘
                                │
                        submerged in water
                        depth in cm = CPAP in cmH2O
                        (tube 5 cm under water ≈ 5 cmH2O)
  CONTINUOUS BUBBLING = the circuit is sealed and pressurised
  NO BUBBLING = leak (mouth open, prongs out, disconnection)''')),

   sec(2, "Setting it up and keeping it working", '''
  <ul>
    <li><b>Start</b> at about 5 cmH₂O; increase in steps (commonly to 7&ndash;8 cmH₂O in children) per local protocol, watching effort and oxygenation.</li>
    <li><b>Flow</b> must be enough to produce continuous bubbling (often 5&ndash;10 L/min depending on the system and size).</li>
    <li><b>Prongs</b> sized to fill the nostrils without blanching; a chin strap or pacifier reduces mouth leak.</li>
    <li><b>Checks every hour:</b> continuous bubbling, water level at the set depth, prong position, nasal septum skin, gastric tube venting air, abdominal distension, SpO₂, respiratory rate, effort and consciousness.</li>
  </ul>''' + pearl('''<p><b>No bubbles means no CPAP.</b> The commonest reason is an open mouth or displaced prongs. Fix the seal before increasing the pressure.</p>''')),

   sec(3, "What the trials show", evidence('''<p><b>Bangladesh</b> (Chisti et al., <i>Lancet</i> 2015): in children under five with severe pneumonia and hypoxaemia in a hospital with close physician monitoring, bubble CPAP reduced treatment failure and deaths compared with standard low-flow oxygen.</p>
  <p><b>Malawi</b> (McCollum et al., <i>Lancet Respiratory Medicine</i> 2019): in district hospitals where CPAP was run mostly by non-physician staff with limited monitoring, children with severe pneumonia given bubble CPAP had <b>higher</b> mortality than those given standard oxygen (the difference was not conventionally significant, but the direction was harmful), and the trial was stopped.</p>
  <p><b>Ethiopia</b> (<i>Lancet Global Health</i> 2024): Gebre et al. randomised 12 general hospitals (1240 children aged 1&ndash;59 months with severe pneumonia and hypoxaemia) to locally made bubble CPAP or low-flow oxygen. Care was given in a dedicated corner in front of the nursing station, supervised by general practitioners and paediatricians. Treatment failure was lower with bubble CPAP (0.8% vs 3.4%; adjusted RR 0.24), and all six deaths occurred in the low-flow group. The authors call for implementation research in higher-mortality settings.</p>
  <p><b>How to reconcile them.</b> Bubble CPAP is not a device; it is a device plus trained staff, close monitoring, reliable oxygen, and a plan when it fails. Where those exist it can prevent intubation and death. Where they do not, it can delay recognition of a child who needs more &mdash; with fatal results.</p>''', "Read the positive and negative trials together") + india('''<p>Bubble CPAP is widely used in Indian SNCUs for newborns and increasingly in paediatric wards for bronchiolitis and pneumonia. Before extending it to older children on a general ward, check the conditions that made it work in Bangladesh: <b>trained nurses on every shift, hourly monitoring, a doctor who can respond within minutes, and a transfer route</b>. If those are missing, fix them first.</p>''')),

   sec(4, "When CPAP is failing", danger('''<p>Rising oxygen requirement despite adequate pressure, worsening effort, recurrent apnoea, falling consciousness, rising CO₂, vomiting with poor airway protection, or shock &mdash; any of these means CPAP is failing. Escalate now: senior review, ventilation or urgent transfer. Do not keep a failing child on CPAP to avoid a difficult decision.</p>''', "Failure criteria") + tracks(
     ["Transition from CPAP to non-invasive or invasive ventilation in PICU",
      "Blood gases to track CO₂"],
     ["Agree the transfer trigger before starting CPAP, and phone the receiving unit early",
      "Keep CPAP running during transfer if the equipment allows; otherwise be ready to bag-mask ventilate",
      "A child who has failed CPAP in a hospital without a ventilator needs bag-mask support and transfer, not more pressure"]), lvl="a"),
  ],
  [Q("A 10-month-old on bubble CPAP at 6 cmH₂O suddenly desaturates. The water bottle is quiet &mdash; no bubbles &mdash; and the infant is crying with his mouth open. What is the first action?",
     ["Increase the CPAP to 10 cmH₂O.",
      "Restore the seal: reposition the prongs, close the mouth (chin strap or pacifier) and confirm bubbling returns &mdash; while assessing the infant.",
      "Stop CPAP and switch to nasal prongs at 1 L/min.",
      "Intubate immediately."],
     1,
     "What does silence in the water bottle mean?",
     "No bubbling means pressure is escaping somewhere before it reaches the bottle. Where is the commonest leak?",
     "No bubbling means <b>no pressure</b> &mdash; the circuit has a leak. The commonest leak is an <b>open mouth or displaced prongs</b>. Restore the seal and confirm bubbling returns, while assessing and supporting the infant.",
     "<b>A</b> &mdash; increasing the set pressure does nothing if gas is escaping. <b>C</b> &mdash; removes support from a hypoxaemic infant. <b>D</b> &mdash; a correctable leak should be fixed first; intubation is for failure.",
     "Look at the bottle first. The bubbles tell you whether CPAP is reaching the child.",
     "section 2, ‘Setting it up and keeping it working’"),
   Q("A district hospital wants to start bubble CPAP for children with severe pneumonia on its general ward, which has one nurse for 20 children at night and no doctor on site after 8 p.m. What is the most evidence-informed advice?",
     ["Start immediately: bubble CPAP reduced deaths in Bangladesh.",
      "Never use bubble CPAP: it increased deaths in Malawi.",
      "Bubble CPAP works where there are trained staff, close monitoring and a rapid response; build those first, and start in a monitored area.",
      "Use bubble CPAP only in children who are not hypoxaemic."],
     2,
     "What was different about the hospitals in the positive and the negative trials?",
     "The same device gave opposite results in two settings. What did the setting with better results have that the other lacked?",
     "The Bangladesh trial had <b>close physician monitoring</b>; the Malawi trial ran CPAP with limited monitoring and non-physician staff and saw more deaths. Bubble CPAP is a <b>system</b>: build trained staffing, monitoring and a response plan first, and start in a monitored area.",
     "<b>A</b> &mdash; ignores the conditions that made the Bangladesh result possible. <b>B</b> &mdash; ignores that it worked where the system was right. <b>D</b> &mdash; CPAP is for children with significant disease; non-hypoxaemic children do not need it.",
     "Read positive and negative trials across the resource gradient. The difference is usually the system, not the device.",
     "section 3, ‘What the trials show’", critical=True)]
)

# ------------------------------------------------------------------ UNIT 10
unit(10, "C", "Non-invasive ventilation",
  "Non-invasive ventilation adds a push on every breath to the continuous pressure of CPAP. It can spare a child intubation &mdash; or make intubation later and more dangerous. The difference is choosing the child and knowing when to stop.",
  [("e", "Distinguish CPAP from bilevel non-invasive ventilation, and what each treats."),
   ("e", "Select a child who is safe for a non-invasive trial, and name the contraindications."),
   ("a", "Troubleshoot leak, fit and patient&ndash;ventilator synchrony."),
   ("x", "Recognise non-invasive ventilation failure and avoid dangerous persistence.")],
  [
   roles({"ug": "Explain the difference between continuous pressure and added inspiratory support.",
          "nurse": "Monitor comfort, skin, leaks, secretions and response; escalate altered consciousness, vomiting or instability.",
          "picu": "Relate leak and timing to effective delivery; report physiological changes before adjusting settings under the agreed plan.",
          "pg": "Select a suitable patient, prescribe a bounded trial, and decide when physiology requires a different strategy."}),
   sec(1, "CPAP and bilevel do different jobs", '''
  <p><b>CPAP</b> gives one continuous pressure. <b>Bilevel</b> NIV gives a higher inspiratory pressure (IPAP) and a lower expiratory pressure (EPAP); the difference between them assists each breath and helps clear CO₂. CPAP treats collapse; bilevel adds help for <b>inadequate ventilation</b> &mdash; tiring, hypercapnic children, neuromuscular weakness.</p>''' + pearl('''<p>Raising EPAP without raising IPAP <b>reduces</b> the support per breath. Keep an eye on the difference, not just the two numbers.</p>''')),

   sec(2, "Choose a child who is safe to trial", table(
     ["Suitable", "Not suitable (intubate or escalate instead)"],
     [["Alert enough to protect the airway", "Unprotected airway, coma, uncontrolled vomiting"],
      ["Manageable secretions", "Copious secretions the child cannot clear"],
      ["Haemodynamically stable", "Shock, arrhythmia"],
      ["Tolerates the interface", "Facial trauma or a mask that cannot fit"],
      ["A team that can watch and escalate", "No one available to respond to failure"]]) + '''
  <p>Agree who reviews, what improvement is expected (effort, rate, CO₂, oxygenation, interaction) and which findings stop the trial. Clinical deterioration overrides the planned duration.</p>'''),

   sec(3, "Leak, fit and timing", '''
  <p>Unintended leak reduces the effective pressure and disturbs triggering. Check mask or interface size and position, circuit connections, and the designed exhalation port &mdash; do not block it or overtighten straps to remove every leak. <b>Synchrony</b> means the support arrives when the child breathes in. Watch effort, chest movement and comfort together; a distressed child needs assessment before more pressure or more sedation.</p>''', lvl="a"),

   sec(4, "Useful trial or dangerous persistence?", '''
  <p>One child on NIV: effort decreases, interaction improves, CO₂ falls &mdash; continue and watch. Mild early anxiety or a correctable leak can be fixed while monitoring. Another child becomes hypotensive, obtunded and more acidotic &mdash; that is <b>physiological failure</b>, not a mask problem.</p>''' + danger('''<p>Prolonged NIV in a failing child makes eventual intubation more dangerous: the child arrives exhausted, acidotic and hypoxaemic. Set a review time (often within 1&ndash;2 hours) and a clear failure definition before you start.</p>''', "Failure is a decision, not a surprise") + '''
  <p>Protect the skin at pressure points, manage secretions, vent the stomach, and make a feeding plan. Agree how the child can signal discomfort.</p>''', lvl="x"),
  ],
  [Q("A 12-year-old with muscular dystrophy and a chest infection is drowsy with a PaCO₂ of 72 mmHg and pH 7.24. He protects his airway and is haemodynamically stable. Which non-invasive support best addresses his main problem?",
     ["Nasal prongs at 4 L/min.",
      "CPAP at 5 cmH₂O.",
      "Bilevel NIV, which adds inspiratory support to increase ventilation, with close monitoring and a failure plan.",
      "High-flow nasal cannula at 2 L/kg/min."],
     2,
     "Is his main problem oxygenation or ventilation?",
     "Weak muscles and a high CO₂ mean each breath is too small. Which device adds a push on every breath?",
     "His main problem is <b>hypoventilation</b> (high CO₂, acidosis) from weak muscles. <b>Bilevel NIV</b> adds inspiratory support to increase each breath. He is suitable for a trial because he protects his airway and is stable &mdash; with close monitoring and failure criteria.",
     "<b>A</b> &mdash; oxygen may raise the saturation while CO₂ keeps rising. <b>B</b> &mdash; CPAP holds the airway open but does not add inspiratory support. <b>D</b> &mdash; high-flow gives little ventilatory assistance for this problem.",
     "Match the device to the failing job: collapse needs pressure; weak breathing needs a push.",
     "section 1, ‘CPAP and bilevel do different jobs’"),
   Q("A child on bilevel NIV for pneumonia becomes more drowsy, her blood pressure falls, and her pH drops from 7.28 to 7.18 over an hour. The mask fits well with minimal leak. What should happen?",
     ["Increase IPAP and continue for another two hours.",
      "Add sedation to improve tolerance.",
      "Recognise NIV failure: call experienced help, support circulation and prepare for intubation.",
      "Switch to high-flow nasal cannula."],
     2,
     "Is this a mask problem or a physiology problem?",
     "The mask fits and there is little leak. Drowsiness, hypotension and worsening acidosis are signs that the child needs something NIV cannot give. What is the next step?",
     "Worsening consciousness, hypotension and acidosis with a good fit are <b>physiological failure</b>. Call experienced help, support circulation and prepare for intubation. Persistence makes the eventual intubation more dangerous.",
     "<b>A</b> &mdash; more pressure does not fix failing physiology and delays definitive support. <b>B</b> &mdash; sedating a drowsy, failing child worsens ventilation. <b>D</b> &mdash; high-flow provides less support than the NIV that is already failing.",
     "When NIV fails, the next device is an airway, not a different mask.",
     "section 4, ‘Useful trial or dangerous persistence?’", critical=True)]
)

# ------------------------------------------------------------------ UNIT 11
unit(11, "C", "Preparing for safer intubation",
  "The view is rarely what kills a sick child during intubation. The physiology does: a hypoxaemic, shocked or acidotic child can arrest in the minute between their own breathing stopping and yours starting.",
  [("e", "Name the physiological risks of intubating a critically ill child and how a team prepares for them."),
   ("e", "Confirm tracheal tube placement with capnography and clinical assessment, and know the limits of each."),
   ("a", "Make a primary and a rescue airway plan explicit, including a stop point."),
   ("x", "Plan the first minutes after intubation: ventilation, sedation, haemodynamics and fixation.")],
  [
   roles({"ug": "Name the physiological risks and explain how the team prepares. Drug prescribing is outside this module.",
          "nurse": "Prepare checked equipment, monitoring and suction; confirm roles; assist drug double-checks under local policy.",
          "picu": "Anticipate peri-intubation instability; confirm monitoring and circuit readiness; track fixation and depth after movement.",
          "pg": "Lead a primary and rescue strategy, optimise physiology with senior help, set stop points and plan post-intubation care."}),
   sec(1, "Prepare the people and the physiology", '''
  <p>An easy-looking airway can still be dangerous in a severely hypoxaemic, shocked or acidotic child. Call experienced help early. <b>Resuscitate before you intubate</b> where you can: treat shock, pre-oxygenate (consider apnoeic oxygenation by nasal cannula), and have a vasopressor ready. Assign an airway operator, an assistant, someone for drugs and monitoring, and a leader who does not do procedures.</p>''' + algo("Before induction — check aloud", '''  PEOPLE     leader · operator · assistant · drugs/monitoring
  PHYSIOLOGY oxygenation optimised · shock treated · push-dose
             vasopressor ready
  EQUIPMENT  suction ×2 · bag-mask · oropharyngeal airway
             tubes: chosen size, half-size above and below
             laryngoscope (video if available) · bougie/stylet
             supraglottic airway (rescue) · tape/holder
             capnography connected and switched on
  PLAN       plan A, plan B, plan C said aloud
             STOP POINT: after an agreed number of attempts or
             a fall in SpO2 — stop, reoxygenate, change plan''')),

   sec(2, "Confirm placement, then depth", '''
  <p>Use <b>waveform capnography</b> (sustained exhaled CO₂) together with chest movement, bilateral air entry and oxygenation. Tube misting or colour improvement alone is not confirmation. Record the depth at the lips and secure the tube.</p>''' + pitfall('''<p><b>Two capnography traps.</b> In cardiac arrest or very low pulmonary blood flow, exhaled CO₂ can be absent even with a correctly placed tube. And a positive CO₂ trace does <b>not</b> prove the right depth: a tube in the right main bronchus still shows CO₂. Listen to both sides.</p>''')),

   sec(3, "The procedure continues after the tube is in", '''
  <p>Connect the ventilator with checked settings and alarms, keep monitoring oxygenation and CO₂, give sedation and analgesia under the clinical plan, and support the circulation &mdash; hypotension after intubation is common. After any move, recheck fixation, depth, chest movement, air entry and gas exchange: earlier confirmation does not survive transport (Unit 18).</p>''' + evidence('''<p>Current AHA/AAP paediatric guidance: cuffed tubes are acceptable in infants and children with cuff pressure monitored; routine cricoid pressure is not recommended; waveform capnography should be used to confirm placement where available. This module does not provide induction drug doses &mdash; use your local prescribing and double-check process.</p>''', "Current guidance")),

   sec(4, "Across settings", tracks(
     ["Video laryngoscopy, capnography and an anaesthetist or intensivist present",
      "Post-intubation care in PICU"],
     ["Intubate only if you can then ventilate, monitor and transfer the child safely; otherwise good bag-mask ventilation or a supraglottic airway is the safer bridge",
      "Colorimetric CO₂ detectors are cheap and far better than no confirmation",
      "Agree with the referral centre, by phone, whether to intubate before transfer"]), tier="good", lvl="a"),
  ],
  [Q("A 4-year-old with severe pneumonia is exhausted, hypotensive (BP 70/40 mmHg) and on high FiO₂. The team predicts an easy view. What is the most important preparation before induction?",
     ["Proceed quickly because the view will be easy.",
      "Treat the shock, pre-oxygenate, prepare a vasopressor and a rescue plan, and assign roles before induction.",
      "Give a sedative dose and see how the child responds.",
      "Wait until the child is less hypoxaemic on its own."],
     1,
     "What is more likely to cause harm here &mdash; the anatomy or the physiology?",
     "A shocked, hypoxaemic child can arrest during induction even when the view is easy. What must be addressed first?",
     "The danger is <b>physiological</b>: hypotension and hypoxaemia can turn induction into arrest. Resuscitate before intubating &mdash; treat shock, pre-oxygenate, have a vasopressor ready, agree primary and rescue plans and roles.",
     "<b>A</b> &mdash; an easy view does not protect against physiological collapse. <b>C</b> &mdash; a trial of sedation in this child risks arrest without a plan. <b>D</b> &mdash; she will not improve on her own; delay also worsens exhaustion.",
     "Prepare for the physiology, not just the laryngoscopy.",
     "section 1, ‘Prepare the people and the physiology’", critical=True),
   Q("After intubation, a 6-year-old shows a good capnography waveform, but air entry is clearly louder on the right and the saturation is 88%. What is the most likely problem?",
     ["The tube is in the oesophagus.",
      "The tube is in the right main bronchus; withdraw it to the correct depth while listening.",
      "The capnograph is faulty.",
      "Normal after intubation; no action needed."],
     1,
     "Does a CO₂ trace tell you how deep the tube is?",
     "The tube is in the airway (there is CO₂), but only one lung sounds ventilated. Where is the tip?",
     "CO₂ confirms the tube is in the <b>airway</b>, not its depth. Unilateral air entry on the right with desaturation suggests <b>right main bronchus intubation</b>. Withdraw the tube carefully to the correct depth while listening to both sides, then re-secure and record.",
     "<b>A</b> &mdash; an oesophageal tube would not give a sustained CO₂ waveform. <b>C</b> &mdash; the clinical signs agree with a real problem. <b>D</b> &mdash; asymmetric air entry with desaturation is never normal.",
     "CO₂ says &lsquo;airway&rsquo;. Your stethoscope says &lsquo;how deep&rsquo;.",
     "section 2, ‘Confirm placement, then depth’")]
)
