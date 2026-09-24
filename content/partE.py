from gen import *

part("E", "Ventilation and systems", "Units 17&ndash;20 · ~6 hours",
     "Once a child is on a ventilator, the questions change: is the machine delivering what we think, is the lung being protected, what do we do when things go wrong suddenly, and how do we move, wean and send the child home safely? The final unit follows one child from the ward to the PICU and back.")

# ------------------------------------------------------------------ UNIT 17
unit(17, "E", "Reading the ventilator through the child",
  "A ventilator shows numbers; the child shows whether they are working. This unit teaches you to read the settings, the delivered values and the waveforms together, and to keep every change inside lung-protective limits.",
  [("e", "Separate the controls that mainly affect oxygenation from those that mainly affect CO₂ clearance."),
   ("e", "Check what actually reaches the child: exhaled tidal volume, pressures, leak, alarms and the child's own response."),
   ("a", "Interpret peak versus plateau pressure and an expiratory flow that does not return to zero."),
   ("x", "Apply PALICC-2 lung-protective limits and know the exceptions to permissive hypercapnia.")],
  [
   roles({"ug": "Explain what each variable represents and why a setting is not a patient outcome.",
          "nurse": "Read back the prescribed settings, check delivered values and alarm limits each shift, and report concerning trends.",
          "picu": "Track delivered tidal volume, pressures, expiratory flow, synchrony and circulation; escalate changes within the agreed plan.",
          "pg": "Integrate mechanics and gas exchange before changing settings; justify a lung-protective strategy and state its exceptions."}),
   sec(1, "Which control does what", table(
     ["Mainly affects", "Controls", "Bedside check"],
     [["<b>Oxygenation</b>", "FiO₂, PEEP, mean airway pressure (inspiratory time, recruitment)", "SpO₂ against the target, work of breathing, perfusion"],
      ["<b>CO₂ clearance</b>", "Tidal volume and rate (minute ventilation), minus dead space", "Chest rise, EtCO₂ trend, blood gas"]]) + '''
  <p>Minute ventilation = tidal volume &times; rate. Example: 120 mL &times; 20 breaths/min = 2.4 L/min. The same number is less effective if dead space is larger (long connectors, rapid shallow breaths) or if there is a leak around the tube. Raising the rate in an obstructed child can shorten expiration and <b>worsen</b> air trapping.</p>'''),

   sec(2, "Look at what reaches the patient", '''
  <ul>
    <li><b>Set is not delivered.</b> Compare set and <b>exhaled</b> tidal volume. A large difference suggests a leak (uncuffed or displaced tube, circuit) or a measurement problem.</li>
    <li><b>Know the mode.</b> In a pressure-targeted mode the pressure is fixed and tidal volume changes with the lung; in a volume-targeted mode the volume is fixed and pressure changes. Watch the variable that is allowed to vary.</li>
    <li><b>Alarms are part of the prescription.</b> Set them to this child and this plan. Never silence and walk away.</li>
    <li><b>After every change</b>, look at the child, the delivered values and the trend within minutes, and again with a blood gas when needed.</li>
  </ul>'''),

   sec(3, "Peak, plateau and time", '''
  <p><b>Peak pressure</b> = resistance component + elastic component. <b>Plateau pressure</b>, measured during an inspiratory hold in a passive child, reflects the elastic component.</p>''' + table(
     ["Pattern", "Think of"],
     [["Peak rises, plateau unchanged", "<b>Resistance</b>: secretions, kinked or bitten tube, bronchospasm"],
      ["Peak and plateau both rise", "<b>Compliance</b> falls: worsening lung disease, pneumothorax, tube in a main bronchus, abdominal distension"],
      ["Expiratory flow does not return to zero before the next breath", "<b>Incomplete exhalation</b>: dynamic hyperinflation (auto-PEEP), especially in asthma and bronchiolitis"]]) + '''
  <p>Coughing, effort and a poor inspiratory hold all make these numbers unreliable. Ask whether the measurement conditions were right before you act on them.</p>''', lvl="a"),

   sec(4, "Lung protection is a set of limits (PALICC-2)", table(
     ["Variable", "PALICC-2 suggestion in paediatric ARDS"],
     [["Tidal volume", "Physiological range, about 6&ndash;8 mL/kg; below 6 mL/kg if needed to respect pressure limits, with caution below 4 mL/kg. Use the lesser of predicted and actual body weight"],
      ["Plateau pressure", "28 cm H₂O or less (29&ndash;32 cm H₂O allowed when chest-wall elastance is increased)"],
      ["Driving pressure", "15 cm H₂O or less, under static conditions"],
      ["SpO₂", "92&ndash;97% in mild and moderate disease; lower values (88&ndash;92%) may be accepted in severe disease after PEEP is optimised, with monitoring of oxygen delivery"],
      ["pH", "Permissive hypercapnia accepted down to pH 7.20 to stay within protective limits"]]) + danger('''<p><b>Exceptions to permissive hypercapnia:</b> raised intracranial pressure, severe pulmonary hypertension, selected congenital heart lesions, haemodynamic instability and significant ventricular dysfunction. Every lung-protective rule is applied to a whole child.</p>''') + evidence('''<p>These are qualified, disease-specific recommendations for paediatric ARDS (PALICC-2, 2023), not a universal first prescription for every ventilated child. In obstructive disease, the priority is time to breathe out, not the same targets.</p>'''), lvl="x"),

   sec(5, "Across settings", tracks(
     ["Microprocessor ventilators with measured exhaled volume, waveforms and inspiratory hold",
      "Continuous EtCO₂ and point-of-care blood gas"],
     ["Older or transport ventilators may not display exhaled volume or waveforms &mdash; chest rise, auscultation, EtCO₂ (if available) and SpO₂ trends become your main tools",
      "With no blood gas analyser, capillary gas or EtCO₂ trends and clinical signs (drowsiness, sweating, rising heart rate) guide CO₂ decisions",
      "Keep a written, laminated card of each child's settings and alarm limits at the bedside"]), tier="good"),
  ],
  [Q("A ventilated 4-year-old in volume-control mode has a sudden rise in peak pressure from 22 to 34 cm H₂O. On an inspiratory hold, the plateau pressure is unchanged at 18 cm H₂O. What is the most likely category of problem?",
     ["Worsening lung compliance from progression of pneumonia.",
      "Increased airway resistance, such as secretions, a kinked tube or bronchospasm.",
      "A large leak around the endotracheal tube.",
      "Pneumothorax."],
     1,
     "Peak pressure has two parts. Which part does the plateau measure?",
     "The plateau is unchanged, so the elastic part is the same. Which part must have risen?",
     "Peak pressure = resistive + elastic components. The plateau reflects the elastic part; it is <b>unchanged</b>. So the rise is <b>resistive</b>: check the tube for kinks, biting and secretions, and consider bronchospasm.",
     "<b>A</b> and <b>D</b> &mdash; reduced compliance or a pneumothorax would raise the plateau as well. <b>C</b> &mdash; a leak lowers pressures and exhaled volume; it does not raise the peak.",
     "Peak up, plateau same: think tube and airways. Both up: think lung and chest.",
     "section 3, ‘Peak, plateau and time’"),
   Q("A ventilated child with PARDS has a plateau pressure of 33 cm H₂O at a tidal volume of 8 mL/kg and PaCO₂ 60 mmHg with pH 7.26. There is no raised intracranial pressure and the circulation is stable. What does PALICC-2 support?",
     ["Increase tidal volume to 10 mL/kg to normalise the CO₂.",
      "Reduce tidal volume to bring plateau pressure to 28 cm H₂O or less, accepting the CO₂ while pH stays at or above 7.20.",
      "Keep settings unchanged, since pH is above 7.20.",
      "Double the respiratory rate without changing tidal volume."],
     1,
     "Which limit is being broken: pH or pressure?",
     "The plateau is above 28. What happens to CO₂ if you reduce the volume, and is that acceptable here?",
     "The plateau pressure (33) is above the PALICC-2 limit. Reduce tidal volume (towards 6 mL/kg, cautiously lower if needed) to protect the lung, and accept <b>permissive hypercapnia</b> while pH stays at or above 7.20 &mdash; this child has no listed exception.",
     "<b>A</b> &mdash; a bigger volume raises pressure further and injures the lung. <b>C</b> &mdash; pH is acceptable, but the pressure is not. <b>D</b> &mdash; doubling rate can shorten expiration and create air trapping; small rate increases are sometimes used, but a doubling does not address the pressure.",
     "Protect the lung first; accept the CO₂ within bounds.",
     "section 4, ‘Lung protection is a set of limits’", critical=True)]
)

# ------------------------------------------------------------------ UNIT 18
unit(18, "E", "Sudden deterioration in a ventilated child (the DOPES check)",
  "A ventilated child who suddenly desaturates, loses chest movement or collapses needs help and a cause found in minutes. DOPES organises the search; treating while you search keeps the child alive.",
  [("e", "Call for help and support ventilation while you look for a cause."),
   ("e", "Work through Displacement, Obstruction, Pneumothorax, Equipment and Stacked breaths."),
   ("a", "Use pressure alarms, EtCO₂, air entry and hand-bagging to separate patient, tube and machine problems."),
   ("x", "Lead the response as a team drill and debrief the system afterwards.")],
  [
   roles({"ug": "Name the reversible causes and say which new finding separates them.",
          "nurse": "Call for help, check the child and the connections, prepare the self-inflating bag, suction and rescue equipment, and report changes aloud.",
          "picu": "Link pressure and flow changes to tube and circuit checks, hand-bagging findings and the examination.",
          "pg": "Coordinate stabilisation and diagnosis at the same time; act promptly on a suspected life-threatening cause within your training."}),
   sec(1, "Treat while you investigate", '''
  <p>Call for help. If the ventilator or circuit may be the problem, disconnect and <b>hand-ventilate</b> with a self-inflating bag and oxygen: this supports the child and separates machine problems from patient problems. Feel the resistance, watch chest movement, and avoid fast rates and high pressures.</p>''' + fig("dopes", "DOPES: find the cause while you keep the child oxygenated", '''  CALL FOR HELP · disconnect and hand-ventilate with oxygen
  D  Displacement     tube out, too deep (main bronchus) or dislodged
  O  Obstruction      kink, biting, secretions, blood, blocked filter
  P  Pneumothorax     sudden fall, asymmetric air entry, shock
  E  Equipment        gas source, circuit, connections, ventilator
  S  Stacked breaths  air trapping: breath in before breath out'''), lvl=None),

   sec(2, "Displacement and obstruction", table(
     ["Clue", "Points towards"],
     [["EtCO₂ waveform lost or falling suddenly", "<b>Displacement</b> out of the trachea, or cardiac arrest &mdash; also check the circulation"],
      ["EtCO₂ present but air entry only on one side (usually right)", "Tube in a main bronchus (too deep) &mdash; or pneumothorax"],
      ["Tube depth mark changed from the recorded value", "Displacement, especially after moving or turning"],
      ["Suction catheter will not pass", "<b>Obstruction</b> or kink &mdash; do not force it"]]) + '''
  <p>A tube in a main bronchus still produces CO₂; EtCO₂ confirms the tube is in the airway, not that it is at the right depth. Record the depth at the lips or gums every shift and after every move.</p>''' + danger('''<p>If the tube is displaced or blocked and cannot be cleared at once, the child needs <b>bag-mask ventilation</b> and a skilled person to replace the airway. A blocked tube should not be bagged harder.</p>'''), lvl=None),

   sec(3, "Pneumothorax and stacked breaths", '''
  <p><b>Pneumothorax</b> causes abrupt deterioration, asymmetric chest movement and air entry, rising pressures and, in tension, falling blood pressure. In a collapsing child it is a <b>clinical diagnosis</b>: a trained clinician should treat suspected tension promptly under the local pathway without waiting for an X-ray. Point-of-care ultrasound can help where there is a trained operator.</p>
  <p><b>Stacked breaths</b> (air trapping) happen when the next breath starts before the last one is out &mdash; typically in asthma or bronchiolitis, and often during fast hand-bagging. The chest becomes over-inflated, venous return falls and the child can arrest. Disconnect briefly to let the trapped air out (gentle chest pressure may help), then ventilate at a slower rate.</p>''', lvl="a"),

   sec(4, "Follow the gas path", '''
  <ul>
    <li><b>Low-pressure or low-volume alarm:</b> disconnection, leak, displaced tube.</li>
    <li><b>High-pressure alarm:</b> obstruction, biting, coughing, bronchospasm, falling compliance, pneumothorax.</li>
    <li><b>Check in order:</b> gas source (pipeline, cylinder level), connections, circuit, water in tubing, filters, valves, the ventilator itself.</li>
  </ul>
  <p>An alarm names what the machine detected, not the cause. If hand-bagging restores chest movement and SpO₂, suspect the machine or circuit &mdash; but reassess the child and tube anyway.</p>''' + india('''<p>In many Indian units, oxygen comes from a hospital PSA plant or manifold with shared pressure. A sudden drop in pipeline pressure can affect several ventilated children at once. Keep a full cylinder with a regulator and self-inflating bag at every ventilated bed, and know who to call about the oxygen supply at night.</p>''')),

   sec(5, "Debrief the near miss", '''
  <p>After stabilisation, record the sequence, suspected cause, what corrected it and the response. Ask whether fixation, a movement checklist, a handover or an alarm setting needs to change. A team drill &mdash; one person on the airway, one on the circuit, one preparing manual support, one leading &mdash; builds the reflex before it is needed.</p>''', tier="good"),
  ],
  [Q("A ventilated 2-year-old is turned for a chest X-ray. SpO₂ falls to 78%, the low-volume alarm sounds, and the EtCO₂ waveform has disappeared. The heart rate is 150/min with a good pulse. What is the first priority?",
     ["Increase FiO₂ to 1.0 and wait 2 minutes for improvement.",
      "Order an urgent chest X-ray.",
      "Call for help, check tube position and ventilate by hand or bag-mask; replace the airway if displaced.",
      "Increase the ventilator rate."],
     2,
     "What does loss of the EtCO₂ waveform mean when the circulation is still present?",
     "The child has just been moved. Which letter of DOPES does that point to, and what keeps the child oxygenated while you check?",
     "After a move, a lost EtCO₂ waveform with a pulse present strongly suggests <b>displacement</b>. Call for help, check the tube, and support oxygenation by hand-bagging or bag-mask ventilation; a skilled person replaces the airway.",
     "<b>A</b> &mdash; more oxygen through a displaced tube reaches no lung. <b>B</b> &mdash; an X-ray delays the rescue. <b>D</b> &mdash; a faster rate through a displaced tube does nothing.",
     "Moved, then lost CO₂: think the tube came out.",
     "section 2, ‘Displacement and obstruction’", critical=True),
   Q("A ventilated 6-year-old with severe asthma is being hand-bagged fast by an anxious team. His chest looks increasingly over-inflated, breath sounds are quiet on both sides, and his blood pressure is falling. What should be done first?",
     ["Bag faster to improve oxygenation.",
      "Briefly disconnect to allow the trapped air to escape, then ventilate at a slower rate.",
      "Give a fluid bolus and continue the same bagging rate.",
      "Increase PEEP on the ventilator."],
     1,
     "Which letter of DOPES fits an obstructed child being bagged fast?",
     "Each breath arrives before the last one is out. What does that do to the chest and to venous return?",
     "This is <b>stacked breaths</b> (dynamic hyperinflation): fast bagging in severe obstruction traps air, over-inflates the chest and reduces venous return. Disconnect briefly to let the air out, then ventilate at a slower rate with time to exhale. If the chest is asymmetric, pneumothorax must also be considered.",
     "<b>A</b> &mdash; faster bagging makes the trapping worse. <b>C</b> &mdash; fluid may help the circulation but does not remove the cause. <b>D</b> &mdash; adding pressure to a trapped chest can worsen it.",
     "In asthma, the life-saving move is often to stop bagging for a moment.",
     "section 3, ‘Pneumothorax and stacked breaths’", critical=True)]
)

# ------------------------------------------------------------------ UNIT 19
unit(19, "E", "Transport, weaning and home oxygen",
  "The support a child needs does not stop at the door. Moving a ventilated child, taking the tube out and sending a child home on oxygen are three points where plans fail through lack of preparation rather than lack of skill.",
  [("e", "Calculate how long an oxygen cylinder will last and plan a margin for transport."),
   ("e", "Prepare a child and team for transfer with monitoring, escort, backup and an accepting team."),
   ("a", "Screen for extubation readiness and recognise children at high risk of extubation failure."),
   ("x", "Plan safe home oxygen: equipment, targets, fire safety, power backup and follow-up.")],
  [
   roles({"ug": "Do the cylinder calculation and list what a transfer checklist must contain.",
          "nurse": "Check oxygen, power and equipment before transfer; teach families home-oxygen safety and escalation.",
          "picu": "Screen daily for extubation readiness, monitor after extubation and recognise post-extubation stridor early.",
          "pg": "Decide when a child is safe to move, to extubate and to go home, and write a plan that survives handover."}),
   sec(1, "How long will the cylinder last?", '''
  <p>Remaining oxygen (litres) &asymp; cylinder capacity (litres when full) &times; current pressure &divide; full pressure. (Unit 6 gives the equivalent: water capacity in litres &times; gauge pressure in bar.) Minutes available = remaining litres &divide; flow (L/min). A transport ventilator also uses gas to drive itself &mdash; check its consumption in the manual.</p>''' + algo("Worked example", '''  Cylinder capacity when full   680 L
  Gauge shows half full         680 × 0.5 = 340 L
  Child needs 4 L/min           340 ÷ 4  = 85 minutes
  Journey expected 60 minutes   plan for DOUBLE = 120 minutes
  85 < 120  →  take a second cylinder''') + pearl('''<p>Plan for <b>at least twice</b> the expected journey time. Roads, traffic, breakdowns and a delayed handover all happen. Check the cylinder size and labelled capacity in your own hospital; they differ between suppliers.</p>''')),

   sec(2, "Transfer: a plan that survives the journey", table(
     ["Before leaving, confirm"],
     [["The child is as stable as possible: airway secured if it may be lost on the way; circulation supported"],
      ["Oxygen (with margin), power or batteries, suction, self-inflating bag and mask, drugs and fluids"],
      ["Monitoring: SpO₂, heart rate and, for a ventilated child, EtCO₂"],
      ["A trained escort who can manage the airway, and a named accepting team who has agreed to receive the child"],
      ["Written handover: diagnosis, trend, support, response, drugs given, family contact"]]) + danger('''<p>Do not reduce the support a child needs so that the oxygen will last or so that the child fits the ambulance. If the support cannot travel, the plan must change.</p>''') + india('''<p>Inter-facility transfers in India often use 108/102 ambulances with limited equipment. Phone ahead, send the referral note and cylinder calculation, and ask what oxygen and suction the ambulance carries before the child leaves.</p>''')),

   sec(3, "Weaning and extubation", '''
  <ul>
    <li><b>Screen every day</b> for readiness: the cause is improving, oxygenation is acceptable on modest FiO₂ and PEEP, the child has a cough and an adequate drive, and the circulation is stable.</li>
    <li><b>Spontaneous breathing trial</b> on low support, with a planned duration and clear failure signs (rising rate and heart rate, falling SpO₂, sweating, distress).</li>
    <li><b>High-risk children</b> (prolonged ventilation, previous failure, neuromuscular disease, suspected upper-airway oedema): plan post-extubation support such as high-flow or non-invasive ventilation; corticosteroids before extubation may be used in those at high risk of stridor.</li>
    <li><b>After extubation</b>, watch for stridor, rising work of breathing and fatigue over the next 24&ndash;48 hours; know who reintubates and have the equipment ready.</li>
  </ul>''' + evidence('''<p>The international paediatric ventilator liberation guideline (PALISI Network, 2023) supports daily screening, a spontaneous breathing trial, steroids for children at high risk of post-extubation upper-airway obstruction, and post-extubation non-invasive support in selected high-risk children. The certainty of evidence for most recommendations is low; follow local protocols.</p>'''), lvl="a"),

   sec(4, "Home oxygen", '''
  <p>Children with bronchopulmonary dysplasia, some congenital heart disease, interstitial lung disease or neuromuscular disease may go home on oxygen. A safe discharge needs:</p>
  <ul>
    <li>A <b>written SpO₂ target</b> and flow from the treating team, and a plan for when to seek help.</li>
    <li><b>Equipment:</b> a concentrator for home, cylinders for travel and power cuts, and a home oximeter if the team recommends it.</li>
    <li><b>Fire safety:</b> no smoking; keep oxygen away from cooking fires, stoves, lamps, candles and diyas; no oil-based creams on the face.</li>
    <li><b>Power:</b> a backup cylinder or inverter for concentrators, and registration with the electricity supplier where that is possible.</li>
    <li><b>Follow-up:</b> regular review to reduce and stop oxygen when the child is ready.</li>
  </ul>''' + india('''<p>Power cuts are common in many areas. Families need a full backup cylinder and a clear plan for what to do when the concentrator stops. Some state programmes and NGOs provide concentrators on loan; check what is available locally before discharge.</p>'''), tier="must", lvl="x"),
  ],
  [Q("A child on 4 L/min oxygen needs a 90-minute road transfer. The cylinder holds 680 L when full and the gauge reads one-quarter full. What should the team do?",
     ["Go, as 170 L at 4 L/min lasts over 40 minutes.",
      "Reduce the flow to 2 L/min so the cylinder lasts the journey.",
      "Take additional full cylinders to cover at least 180 minutes (twice the journey) at 4 L/min.",
      "Go, and ask the ambulance to stop for oxygen on the way."],
     2,
     "How many litres are left, and how long do they last at 4 L/min?",
     "170 L lasts about 42 minutes. How long should you plan for?",
     "One-quarter of 680 L is 170 L; at 4 L/min that is about 42 minutes, far less than the 90-minute journey. Plan for <b>twice</b> the journey time (180 minutes = 720 L): take enough full cylinders.",
     "<b>A</b> &mdash; 42 minutes runs out halfway. <b>B</b> &mdash; never reduce the support the child needs to fit the supply. <b>D</b> &mdash; there is no guaranteed supply on the road.",
     "Capacity × fraction ÷ flow, then double the journey.",
     "section 1, ‘How long will the cylinder last?’", critical=True),
   Q("A 9-month-old with bronchopulmonary dysplasia is being discharged on home oxygen by concentrator. Which advice is most important for safety at home?",
     ["Turn the oxygen off at night to prevent dependence.",
      "Keep oxygen away from cooking fires, lamps and diyas, and have a full backup cylinder for power cuts.",
      "Increase the flow whenever the baby cries.",
      "Use petroleum jelly on the face to prevent dryness from the prongs."],
     1,
     "What are the two commonest ways home oxygen becomes dangerous?",
     "Oxygen feeds fire, and a concentrator needs electricity. Which answer deals with both?",
     "Oxygen makes things burn fiercely: keep it away from flames, including cooking fires, lamps and diyas, and never smoke nearby. Concentrators stop in a power cut, so a <b>full backup cylinder</b> is essential.",
     "<b>A</b> &mdash; oxygen should follow the written prescription; turning it off can cause hypoxaemia during sleep. <b>C</b> &mdash; changes should follow the written plan, not crying. <b>D</b> &mdash; oil-based products near oxygen are a fire risk; use water-based products.",
     "Home oxygen needs two backups: no flames, and no dependence on the mains alone.",
     "section 4, ‘Home oxygen’")]
)

# ------------------------------------------------------------------ UNIT 20
unit(20, "E", "Capstone: follow the deteriorating child",
  "One fictional child, Meera, from the ward to the PICU and back. At each stage, name the threat, choose the support, and say how you will know if it is failing. Then look at where the field is moving.",
  [("e", "Name the physiological threat before choosing a device, at each stage of an evolving case."),
   ("e", "State a target, a reassessment time and a failure trigger for every support you start."),
   ("a", "Escalate on the trajectory, not on a fixed trial endpoint; prepare physiology before intubation."),
   ("x", "Discuss current developments in oxygen systems, oximetry and respiratory support.")],
  [
   roles({"ug": "At each stage, explain the mechanism and the next supervised action; never name a device without its purpose.",
          "nurse": "Identify and communicate deterioration, check delivery and prepare the requested rescue support.",
          "picu": "Track the child&ndash;airway&ndash;device relationship as the case moves; say which change needs immediate review.",
          "pg": "Lead escalation with explicit failure criteria, physiological preparation and a handover that someone else can act on."}),
   sec(1, "Stage 1: the ward", fig("ladder", "The escalation ladder: every rung has a target and a failure trigger", '''  NAME THE THREAT: oxygenation, ventilation or both?
  1  Low-flow oxygen (prongs, mask) → titrate to a written SpO₂ target, reassess in 15–60 min
  2  Target not met or work rising → bubble CPAP or high-flow, with trained monitoring and a failure plan
  3  Drowsy, apnoea, rising CO₂ or shock → intubate and ventilate (resuscitate first)
     NIV only if the child is alert and can protect the airway''') + '''
  <p><b>Meera, 14 months, 9 kg</b>, day 3 of fever and cough. Respiratory rate 58/min, subcostal recession, crackles on the right, SpO₂ 86% in room air, alert, capillary refill 2 seconds.</p>
  <p><b>Threat:</b> hypoxaemia from pneumonia (oxygenation). <b>Support:</b> oxygen by nasal prongs, titrated to the local target (Unit 5), plus antibiotics per WHO 2024 (Unit 13). <b>Reassess</b> within 30&ndash;60 minutes. <b>Failure trigger:</b> SpO₂ below target despite 2 L/min by prongs, or increasing work of breathing.</p>'''),

   sec(2, "Stage 2: not enough", '''
  <p>Two hours later: SpO₂ 89% on 2 L/min, respiratory rate 64/min, grunting.</p>
  <p><b>Threat:</b> worsening oxygenation with rising work. <b>Support:</b> bubble CPAP (Unit 9) or high-flow (Unit 8), depending on what your unit has and staff can monitor. <b>Reassess</b> at 1 hour: heart rate and respiratory rate should fall and SpO₂ reach target. <b>Failure trigger:</b> no improvement, drowsiness, apnoea or rising CO₂.</p>'''),

   sec(3, "Stage 3: failing non-invasive support", '''
  <p>At 3 hours on CPAP: Meera is drowsy, her breathing is shallower, and SpO₂ is 91%. A capillary gas shows pH 7.18, PCO₂ 72 mmHg.</p>
  <p><b>Threat:</b> <b>ventilatory failure</b> &mdash; a reassuring saturation on oxygen is hiding it (Unit 3). Do not wait for the planned trial endpoint. <b>Action:</b> call the most experienced airway team, prepare physiology (oxygenation, circulation, fluids and vasoactive plan) and equipment (Unit 11); confirm the tube with EtCO₂ and examination; start lung-protective ventilation (Unit 17).</p>''' + danger('''<p>Drowsiness in a child on CPAP is a failure sign, not a sign of rest.</p>''')),

   sec(4, "Stage 4: sudden deterioration, then transfer", '''
  <p>During a line insertion Meera is repositioned. SpO₂ falls to 70%, the low-volume alarm sounds and air entry is louder on the right. EtCO₂ is still present.</p>
  <p><b>Threat:</b> displacement, most likely <b>too deep</b> (right main bronchus), or pneumothorax (Unit 18). Hand-ventilate, check the depth mark, withdraw to the recorded depth if it has moved, and reassess air entry. Then plan the transfer to a tertiary PICU with an oxygen calculation, escort and accepting team (Unit 19).</p>'''),

   sec(5, "Stage 5: the way home", '''
  <p>Five days later Meera passes a spontaneous breathing trial, is extubated to high-flow, and is weaned to room air. Before discharge: vaccination review, feeding, and a safety-net plan for the family.</p>
  <p><b>Debrief:</b> what was the earliest warning, and when did the team escalate? Was there an earlier moment to recognise failure? Name one finding that changed your decision and one tempting option you rejected.</p>''', tier="good"),

   sec(6, "Future directions", '''
  <ul>
    <li><b>Oximetry and skin pigmentation.</b> Pulse oximeters can overestimate saturation in people with darker skin, which may hide hypoxaemia. Regulators, including the US FDA (draft guidance, 2025), are tightening the evidence required across skin tones. Until then, treat borderline readings with more caution (Unit 4).</li>
    <li><b>Oxygen systems.</b> Many Indian district hospitals gained pressure-swing adsorption (PSA) plants during COVID-19. Whether they still work depends on maintenance, spare parts and trained technicians; solar-powered oxygen and concentrator programmes are extending supply to small facilities.</li>
    <li><b>Bubble CPAP in low-resource settings.</b> Trials differ: benefit in a Bangladeshi hospital with close physician monitoring, a signal of possible harm in Malawian district hospitals without it, and benefit again in Ethiopian general hospitals (2024) with a dedicated bed space and supervision. Current work focuses on who benefits and what supervision makes it safe (Unit 9).</li>
    <li><b>Personalised ventilation.</b> Closed-loop oxygen control, driving-pressure-guided and oesophageal-pressure-guided ventilation, and lung ultrasound are being studied in children; most are not yet standard care.</li>
  </ul>''', tier="nice"),
  ],
  [Q("Meera (Stage 3) is on bubble CPAP. Her SpO₂ is 91% but she is drowsy with shallow breathing, and her gas shows pH 7.18 and PCO₂ 72 mmHg. The planned CPAP trial has one more hour to run. What should happen?",
     ["Continue CPAP for the remaining hour, as SpO₂ is acceptable.",
      "Increase the oxygen and recheck the gas in 2 hours.",
      "Treat this as failure of non-invasive support: call the airway team and prepare for intubation and ventilation.",
      "Give a sedative to help her tolerate the CPAP interface."],
     2,
     "Which failure is present: oxygenation or ventilation?",
     "Drowsiness, shallow breathing and a high CO₂ mean she is not clearing CO₂. Does a planned endpoint matter now?",
     "Drowsiness with rising CO₂ and acidosis is <b>ventilatory failure</b>, and a reasonable SpO₂ on oxygen is hiding it. Escalate now: call the most experienced airway team and prepare physiology and equipment for intubation.",
     "<b>A</b> &mdash; escalate on the trajectory, not on the timetable. <b>B</b> &mdash; more oxygen does not fix CO₂ retention and can hide it further. <b>D</b> &mdash; sedating a child with ventilatory failure on non-invasive support can cause respiratory arrest.",
     "A good number on a drowsy child is a warning, not reassurance.",
     "section 3, ‘Stage 3: failing non-invasive support’", critical=True),
   Q("After Meera is repositioned (Stage 4), SpO₂ falls, air entry is louder on the right, and the EtCO₂ waveform is still present. The depth mark has moved from 12 cm to 14 cm at the gums. What is the most likely cause and first step?",
     ["Oesophageal intubation: remove the tube immediately.",
      "Tube in the right main bronchus: withdraw to the recorded depth and reassess air entry.",
      "Ventilator failure: change the ventilator.",
      "Worsening pneumonia: increase PEEP."],
     1,
     "What does EtCO₂ confirm, and what does it not confirm?",
     "The tube has moved 2 cm deeper and air entry is louder on the right. Where is the tip likely to be?",
     "EtCO₂ confirms the tube is in the airway, not its depth. A tube that has moved deeper with right-sided air entry is most likely in the <b>right main bronchus</b>. Withdraw to the recorded depth, reassess air entry and SpO₂, and keep pneumothorax in mind if it does not correct.",
     "<b>A</b> &mdash; an oesophageal tube does not produce a sustained EtCO₂ waveform. <b>C</b> &mdash; the finding is asymmetric air entry after a move, not a machine fault. <b>D</b> &mdash; increasing PEEP does not fix a misplaced tube.",
     "CO₂ says ‘in the airway’; only the depth mark and air entry say ‘in the right place’.",
     "section 4, ‘Stage 4: sudden deterioration, then transfer’")]
)
