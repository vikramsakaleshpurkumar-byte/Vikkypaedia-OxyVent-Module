from gen import *

part("B", "Measure and give oxygen", "Units 4&ndash;7 · ~5 hours",
     "Oxygen is the most commonly prescribed drug in paediatrics and the least often prescribed properly. This Part covers the measurement you rely on, the prescription you write, the supply chain behind it, and the breath you give when oxygen alone is not enough.")

# ------------------------------------------------------------------ UNIT 4
unit(4, "B", "Pulse oximetry: trust the child, check the signal",
  "The pulse oximeter is the most useful monitor in paediatric respiratory care, and it lies in predictable ways. Before you act on a number, make sure it belongs to the child.",
  [("e", "Check that a pulse-oximeter reading is valid: probe, site, waveform and pulse agreement."),
   ("e", "Name the common causes of a misleading reading, including poor perfusion, movement and skin pigmentation."),
   ("a", "State what SpO₂ does not measure, and choose the test that answers the question you actually have."),
   ("x", "Interpret a saturation trend together with the support the child was receiving.")],
  [
   roles({"ug": "Explain which parts of the reading are reliable before interpreting the number.",
          "nurse": "Use the right probe and site, compare pulses, reassess perfusion and document the response to correction.",
          "picu": "Integrate signal quality with gases and CO₂ trends; recognise changing device and physiological limits.",
          "pg": "Resolve discordance with clinical assessment and the right confirmatory test; never anchor on one reassuring number."}),
   sec(1, "Check that the signal belongs to the child", '''
  <ul>
    <li>Use a probe made for the child's size and site; align it and secure it without constriction.</li>
    <li>Look for a <b>stable waveform</b> (plethysmograph).</li>
    <li>Compare the displayed pulse with the clinical pulse or ECG. A displayed pulse of 45/min when the child's pulse is 150/min means the saturation cannot be trusted.</li>
  </ul>''' + danger('''<p>Assess and support the child <b>while</b> a colleague fixes the signal. Never spend minutes hunting for a perfect reading before treating danger signs.</p>''', "Treat the child, not the probe")),

   sec(2, "Why readings mislead", table(
     ["Cause", "Effect"],
     [["Movement, crying", "Erratic readings, poor waveform"],
      ["Cold skin, poor perfusion, shock", "Weak or absent signal; falsely low or unobtainable"],
      ["Wrong probe size, bright ambient light", "Unreliable values"],
      ["Darker skin pigmentation", "Pulse oximeters can <b>overestimate</b> saturation, so hypoxaemia may be missed"],
      ["Carbon monoxide, methaemoglobinaemia", "Standard oximetry can be misleading; laboratory co-oximetry is needed"]]) + evidence('''<p>Regulators including the US FDA have highlighted reduced accuracy of pulse oximeters in people with darker skin pigmentation, with a risk of <b>occult hypoxaemia</b> &mdash; a true saturation lower than displayed. Do not apply an invented numerical correction. When the examination and the number disagree, <b>believe the examination</b>, improve the measurement conditions, and seek additional assessment.</p>''', "Skin pigmentation and occult hypoxaemia")),

   sec(3, "What the monitor does not measure", '''
  <p>SpO₂ estimates arterial oxygen saturation. It does <b>not</b> measure CO₂, haemoglobin concentration or cardiac output. When ventilation is the question, assess effort, consciousness and CO₂ (blood gas or capnography). When perfusion is the concern, examine the circulation. Choose the test that answers your question rather than ordering everything.</p>''' + pearl('''<p><b>A trend needs its context.</b> A stable saturation on steadily increasing oxygen is a worsening child. Chart the support alongside every saturation so the next person can read the trend correctly.</p>''')),

   sec(4, "Across settings", tracks(
     ["Continuous oximetry with waveform on every child receiving respiratory support; capnography for ventilated children",
      "Blood gases available at the bedside"],
     ["A handheld paediatric pulse oximeter at every triage point and ward is the single most important monitoring purchase",
      "Spot-checks at defined intervals, with a written escalation threshold, when continuous monitoring is not available",
      "Keep neonatal and paediatric probes, spare batteries and a charging routine; broken probes are the commonest cause of &ldquo;no oximeter&rdquo;"]) + india('''<p>Studies in Indian primary-care settings have found hypoxaemia to be common among sick under-fives and often missed without oximetry. Integrating pulse oximetry into IMNCI assessment is feasible and acceptable to health workers when devices, probes and training are supplied. Hypoxaemia predicts death in childhood pneumonia more strongly than any single clinical sign.</p>''')),
  ],
  [Q("A shocked, cold toddler has SpO₂ 74% on the monitor, no clear waveform and a displayed pulse of 42/min while his palpable pulse is 150/min. He has fast breathing and recession. What should you do?",
     ["Ignore the reading as artefact and wait until a good signal is obtained before treating.",
      "Accept 74% as accurate and intubate immediately.",
      "Start oxygen and support breathing and circulation now, while a colleague improves the signal (warm the site, change probe or site) and reassess.",
      "Apply a correction of +10% for poor perfusion and document SpO₂ 84%."],
     2,
     "Is the number reliable? And does an unreliable number mean the child is well?",
     "The pulse mismatch tells you the signal is bad. His examination still shows shock and respiratory distress. What do you do with each?",
     "The <b>signal is unreliable</b> (no waveform, pulse mismatch), but the <b>child is clearly unwell</b>. Treat the child &mdash; oxygen, breathing and circulatory support &mdash; while someone improves the measurement. Then reassess with a valid signal.",
     "<b>A</b> &mdash; waiting for a good number delays treatment of an obviously sick child. <b>B</b> &mdash; an unreliable number is not a basis for intubation on its own. <b>D</b> &mdash; there is no valid correction factor; inventing one is dangerous.",
     "A bad signal changes how much you trust the number, not how sick the child is.",
     "section 1, ‘Check that the signal belongs to the child’", critical=True),
   Q("A 2-year-old with dark skin and pneumonia has SpO₂ 93% on room air with a good waveform, but she has marked recession, grunting and is less interactive than an hour ago. What is the best interpretation?",
     ["The saturation is normal, so her breathing is adequate; no change is needed.",
      "Her true saturation may be lower than displayed, and her examination shows worsening distress: give oxygen, review urgently and consider a blood gas.",
      "Add 4% to the reading to correct for skin pigmentation.",
      "The grunting is a habit and can be ignored."],
     1,
     "When the number and the child disagree, which do you believe?",
     "Oximeters can overestimate saturation in darker skin. Her examination is worsening. Which option acts on both facts without inventing a correction?",
     "Pulse oximeters can <b>overestimate</b> saturation in darker skin, and her <b>examination is worsening</b>. Believe the child: give oxygen, review urgently, and confirm with a blood gas where available.",
     "<b>A</b> &mdash; ignores both the device limitation and the clinical signs. <b>C</b> &mdash; no validated correction exists, and the direction of error would make things worse if applied the wrong way. <b>D</b> &mdash; grunting signals significant lung disease.",
     "The oximeter is an assistant. The examination is the senior.",
     "section 2, ‘Why readings mislead’")]
)

# ------------------------------------------------------------------ UNIT 5
unit(5, "B", "Prescribe and reassess oxygen",
  "&ldquo;Give oxygen&rdquo; is not a prescription. A prescription says why, to what target, by which device, starting where, reassessed when, and what happens if it fails.",
  [("e", "Write a complete oxygen prescription: indication, target, device, starting flow or FiO₂, reassessment and escalation."),
   ("e", "State WHO's threshold for giving oxygen and the condition-specific targets that differ from it."),
   ("a", "Choose a delivery device and flow to match the job, and know what each can and cannot do."),
   ("x", "Recognise when a rising oxygen requirement means the child needs a different kind of support.")],
  [
   roles({"ug": "Explain why flow and inspired oxygen concentration are different. Present your plan to a supervisor.",
          "nurse": "Check the prescribed target, source, tubing and interface; document the response and escalate rising needs.",
          "picu": "Track oxygen exposure, delivery performance and supply; recognise when oxygen alone is inadequate.",
          "pg": "Choose a condition-specific target, justify the support plan and agree escalation and transfer arrangements."}),
   sec(1, "When to give oxygen, and to what target", table(
     ["Situation", "Start oxygen when", "Target"],
     [["Any child with emergency signs (obstructed breathing, severe distress, central cyanosis, shock, coma, convulsions)", "Immediately, regardless of SpO₂ (WHO ETAT)", "Stabilise first; then titrate"],
      ["Sick child, general (WHO)", "SpO₂ below 90%", "Keep at or above 90%; stop when stable at or above 90% in room air"],
      ["Bronchiolitis (Australasian guideline 2025)", "Persistently below 90% from 6 weeks of age; below 92% if under 6 weeks or with underlying conditions", "Above the starting threshold; do not chase 100%"],
      ["Paediatric ARDS (PALICC-2)", "&mdash;", "SpO₂ 92&ndash;97% in mild/moderate disease; lower accepted in severe disease after PEEP optimisation"],
      ["Cyanotic heart disease, chronic lung disease", "Individual plan", "As set by the child's specialist team"]]) + pitfall('''<p><b>Transplanting a number.</b> A bronchiolitis threshold does not apply to a child in shock, and a PARDS target does not apply to a child with cyanotic heart disease. An apnoeic or exhausted child needs breathing support; no threshold calculation should delay it.</p>''')),

   sec(2, "Choose the device for the job", table(
     ["Device", "Typical flow", "What it delivers", "Limits"],
     [["Nasal prongs", "About 0.5 L/min in young infants; 1&ndash;2 L/min in older infants and children (WHO)", "Low, variable FiO₂; well tolerated; child can feed", "FiO₂ depends on breathing pattern and mouth-breathing"],
      ["Simple face mask", "At least the flow the manufacturer specifies (often 4&ndash;5 L/min or more)", "Moderate, variable FiO₂", "Too low a flow causes rebreathing of CO₂"],
      ["Non-rebreathing mask with reservoir", "10&ndash;15 L/min, reservoir kept inflated", "High FiO₂", "Does not ventilate an apnoeic child"],
      ["Venturi mask", "The flow printed on the adapter", "A set mixture", "Ports must stay clear"],
      ["High-flow nasal cannula", "Weight-based, heated and humidified (Unit 8)", "Titratable FiO₂ plus some distending pressure", "A system, not just a higher wall flow"]]) + '''
  <p><b>Flow is not FiO₂.</b> Flow is a volume of gas per minute; FiO₂ is the fraction of oxygen in what the child breathes. Turning up ordinary prongs does not make them a high-flow system.</p>'''),

   sec(3, "Better saturation, worse child", '''
  <p>An 18-month-old with pneumonia has SpO₂ 87% with a good signal and marked recession. Oxygen starts. Five minutes later SpO₂ is 94% &mdash; but she is drowsier and air entry is poorer. <b>The target has been reached and the child is deteriorating.</b> Call skilled help, reassess airway and ventilation, and check the device at the same time. Oxygen can hide ventilation failure on the display.</p>''' + pearl('''<p>Hand over the <b>trend, the intervention and the response</b>, never just the best saturation of the shift.</p>'''), lvl="a"),

   sec(4, "When oxygen is not enough", '''
  <p>A rising oxygen requirement, persistent severe recession, grunting, recurrent apnoea or falling consciousness mean the child needs <b>more than oxygen</b>: distending pressure (high-flow or CPAP, Units 8&ndash;9), assisted breaths, or an airway. Agree in advance the point at which you will escalate, and write it in the prescription.</p>''', tier="good", lvl="x"),
  ],
  [Q("Which oxygen prescription is complete?",
     ["&ldquo;O₂ PRN.&rdquo;",
      "&ldquo;O₂ 2 L/min.&rdquo;",
      "&ldquo;Keep sats 100%.&rdquo;",
      "&ldquo;Pneumonia with SpO₂ 86%. Nasal prongs 1 L/min; target SpO₂ 90&ndash;94%; recheck SpO₂, rate and effort in 15 minutes; call registrar if target not reached on 2 L/min or effort worsens.&rdquo;"],
     3,
     "A prescription must tell the nurse what to do when things go right and when they go wrong.",
     "Look for indication, device, starting flow, target, reassessment time and escalation trigger in one option.",
     "A complete oxygen prescription includes the <b>indication</b>, <b>device and starting flow</b>, a <b>target range</b>, the <b>reassessment interval</b> and an <b>escalation trigger</b>.",
     "<b>A</b> &mdash; no indication, target or device. <b>B</b> &mdash; a flow with no target or response plan. <b>C</b> &mdash; 100% is not a sensible target and encourages unnecessary oxygen.",
     "If the prescription could be copied onto any child's chart, it is not specific enough.",
     "section 1, ‘When to give oxygen, and to what target’"),
   Q("A 5-week-old with bronchiolitis (born at term, no other conditions) has a persistent SpO₂ of 91% in room air with a good signal. She is feeding reasonably. Using the Australasian 2025 bronchiolitis thresholds, what is correct?",
     ["No oxygen is needed because 91% is above 90%.",
      "Start oxygen: under 6 weeks of age the threshold is 92%.",
      "Start high-flow nasal cannula immediately.",
      "Oxygen is only needed below 85% in bronchiolitis."],
     1,
     "The guideline uses two thresholds. What decides which one applies?",
     "The lower threshold (90%) is for infants aged 6 weeks and over without underlying conditions. How old is this infant?",
     "Under 6 weeks of age (or with underlying conditions) the Australasian 2025 guideline starts oxygen when SpO₂ is <b>persistently below 92%</b>. At 5 weeks and 91%, she meets it.",
     "<b>A</b> &mdash; applies the threshold for older infants. <b>C</b> &mdash; high-flow is not first-line for a mildly hypoxaemic infant; low-flow oxygen comes first. <b>D</b> &mdash; no guideline uses 85%.",
     "Thresholds differ by age and risk. Always check which one applies before you decide.",
     "section 1, ‘When to give oxygen, and to what target’")]
)

# ------------------------------------------------------------------ UNIT 6
unit(6, "B", "Oxygen as a system",
  "A child cannot breathe a prescription. Between the source and the nostril there are cylinders, concentrators, pipes, flowmeters, splitters, tubing, power and people &mdash; and any of them can fail silently.",
  [("e", "Name the oxygen sources in Indian facilities and the limits of each."),
   ("e", "Calculate how long a cylinder will last and plan oxygen for a transfer."),
   ("a", "Trace the oxygen path from source to child and find the likely failure points."),
   ("x", "Plan an oxygen-system improvement project for a ward, with measurable outcomes.")],
  [
   roles({"ug": "Trace the oxygen path from source to child and name one failure point at each step.",
          "nurse": "Check source, pressure, flowmeter, tubing and interface at every shift; report empty or failing supply before it runs out.",
          "picu": "Plan oxygen for transport with a reserve; know the backup when the plant or power fails.",
          "pg": "Own the oxygen plan for your patients, including transfer, and escalate system failures to the facility."}),
   sec(1, "Where the oxygen comes from", table(
     ["Source", "Strengths", "Limits"],
     [["Cylinder (D, B-type, jumbo)", "No power needed; portable", "Finite contents; needs a working regulator; heavy; must be refilled and transported"],
      ["Oxygen concentrator", "Continuous supply from room air; cheap to run", "Needs reliable power; typical output 5&ndash;10 L/min at up to about 90&ndash;95% purity; purity falls at high flows"],
      ["Pressure swing adsorption (PSA) plant with piped supply", "Large, continuous supply to many beds", "Needs maintenance, power and trained technicians; purity must be monitored"],
      ["Liquid oxygen tank", "Very large supply", "Supply-chain dependent; mostly larger hospitals"]]) + india('''<p>After 2021, India installed PSA plants in a large number of public hospitals, changing what district hospitals can deliver. The recurring problems now are maintenance, power backup, purity monitoring and the last few metres: flowmeters, splitters, paediatric prongs and masks. WHO and UNICEF publish technical specifications for oxygen therapy devices; MoHFW and NHSRC have issued guidance on oxygen management and audits.</p>''')),

   sec(2, "How long will the oxygen last?", algo("Cylinder arithmetic", '''  usable litres  ≈ (cylinder water capacity in L) × (gauge pressure in bar)
                   − a safety reserve
  minutes        = usable litres ÷ total flow (L/min)

  Example: a cylinder with 240 usable litres at 8 L/min
           240 ÷ 8 = 30 minutes — before any reserve or delay

  For transport: plan for AT LEAST TWICE the expected
  journey time (traffic, breakdowns, a slow handover).
  High-flow and CPAP systems may draw more gas than the
  oxygen flow shown — use the device's actual consumption.''') + danger('''<p>&ldquo;There is a cylinder&rdquo; is not a transfer plan. Check the regulator, the gauge, the calculation, a spare, and who will change it. If the support the child needs cannot be sustained on the journey, escalate the transport arrangements before departure.</p>''', "The empty cylinder")),

   sec(3, "Follow the gas from source to child", '''
  <p>Walk the path: <b>source</b> (plant pressure, concentrator power, cylinder contents) &rarr; <b>regulator or outlet</b> &rarr; <b>flowmeter</b> (reading at the ball's centre) &rarr; <b>splitter</b> (if one concentrator serves several children, is each getting the prescribed flow?) &rarr; <b>tubing</b> (kinked, disconnected, crushed under a bed) &rarr; <b>humidifier</b> &rarr; <b>interface</b> (prongs in the nose? mask on the face?) &rarr; <b>child</b>.</p>''' + pearl('''<p>When a child on oxygen deteriorates, check the child and the whole gas path at the same time. An unnoticed disconnection is a recurring cause of &ldquo;unexplained&rdquo; desaturation.</p>''') + '''
  <ul>
    <li>Secure cylinders upright in holders. Keep oxygen away from flames, oils and grease; no smoking near oxygen.</li>
    <li>Humidify when high flows are used for long periods or when the nose is bypassed.</li>
  </ul>'''),

   sec(4, "An oxygen improvement project", table(
     ["Element", "Example"],
     [["Aim", "Every child with SpO₂ below 90% on the paediatric ward receives oxygen within 15 minutes, 24 hours a day"],
      ["Measures", "Proportion of hypoxaemic children receiving oxygen; minutes without supply per month; proportion of beds with a working oximeter"],
      ["Changes", "Daily oxygen checklist; paediatric interface kit at every bed; spare cylinder with a full gauge; named person for concentrator maintenance"]]) + '''
  <p>Auditing whether oxygen was actually available and correctly delivered is often a higher-yield project in a district hospital than any change to a clinical protocol.</p>''', tier="good", lvl="x"),
  ],
  [Q("A child on 8 L/min of oxygen by non-rebreathing mask needs a 40-minute road transfer. The only cylinder has about 240 usable litres. What is the correct action?",
     ["Leave now; 240 litres is plenty for 40 minutes.",
      "Reduce the flow to 2 L/min for the journey to save oxygen.",
      "Do not depart until enough oxygen for the journey plus a reserve (and a spare cylinder or a larger one) is on board.",
      "Send the child without oxygen, since the journey is short."],
     2,
     "How many minutes will 240 litres last at 8 L/min?",
     "240 &divide; 8 = 30 minutes, which is less than the journey &mdash; and there is no reserve for delays. What must happen before departure?",
     "At 8 L/min, 240 litres lasts <b>30 minutes</b> &mdash; less than a 40-minute journey, with no reserve. Arrange enough oxygen for at least twice the journey time (80 minutes, 640 litres), and a spare, before leaving.",
     "<b>A</b> &mdash; the arithmetic shows the cylinder runs out on the road. <b>B</b> &mdash; reducing below the support the child needs is dangerous. <b>D</b> &mdash; a child needing 8 L/min will desaturate without it.",
     "Do the cylinder sum out loud before every transfer. It takes ten seconds and prevents deaths on the road.",
     "section 2, ‘How long will the oxygen last?’", critical=True),
   Q("One oxygen concentrator on a ward feeds three children through a flow-splitter. Each is prescribed 1 L/min, but one child's saturation keeps falling. The concentrator is on and its flowmeter reads 3 L/min. What is the most useful first check?",
     ["Increase the concentrator to 10 L/min for all three children.",
      "Follow the gas path to that child: check the splitter outlet flow, the tubing and whether the prongs are in the nose &mdash; while assessing the child.",
      "Assume the child's pneumonia is worsening and start antibiotics again.",
      "Switch off the concentrator and restart it."],
     1,
     "Where in the path could the flow to just one child be lost?",
     "The source seems to be working. The fault affects one child. Walk the path from the splitter to that child's nose.",
     "A problem affecting <b>one child on a shared source</b> points to that child's branch: splitter outlet, tubing (kinked or disconnected) or interface (prongs out of the nose). Check it while assessing the child.",
     "<b>A</b> &mdash; raising the total flow without finding the fault may still leave that child without oxygen, and wastes it for the others. <b>C</b> &mdash; the child may be worsening, but first exclude a delivery failure. <b>D</b> &mdash; restarting interrupts oxygen for all three children.",
     "When one child on a shared supply desaturates, suspect the branch before the disease.",
     "section 3, ‘Follow the gas from source to child’")]
)

# ------------------------------------------------------------------ UNIT 7
unit(7, "B", "Effective bag-mask breaths",
  "Bag-mask ventilation is the most important airway skill in paediatrics and the most often done badly. The aim is not a squeeze; it is a visible rise of the chest and an improving child.",
  [("e", "Prepare for bag-mask ventilation: help, equipment, mask size and airway position for age."),
   ("e", "Deliver breaths that produce visible chest rise, at the right rate for a child with a pulse."),
   ("a", "Troubleshoot absent chest rise systematically, and use the two-person technique."),
   ("x", "Recognise and avoid overventilation, especially in obstructive disease.")],
  [
   roles({"ug": "Talk through the sequence on a mannequin and ask an assessor to watch your actual technique.",
          "nurse": "Prepare the equipment, call for help and assist ventilation within your training; report chest rise and response.",
          "picu": "Coordinate two-person ventilation, watch chest movement and haemodynamics, and notice rising resistance or a failing seal.",
          "pg": "Lead airway and ventilation assessment, allocate roles and choose a rescue plan when basic corrections fail."}),
   sec(1, "Start with airway, equipment and help", '''
  <ul>
    <li><b>Call for help</b> and check breathing and pulse.</li>
    <li><b>Mask:</b> covers nose and mouth, not the eyes, not over the chin.</li>
    <li><b>Position:</b> neutral in infants (avoid over-extension; a small roll under the shoulders), sniffing in older children. In suspected trauma, jaw thrust with in-line stabilisation.</li>
    <li><b>Bag:</b> self-inflating bag of appropriate size (about 450&ndash;500 mL for infants and small children; larger for older children), connected to oxygen with the reservoir attached.</li>
    <li><b>Suction</b> ready.</li>
  </ul>'''),

   sec(2, "Give only the breath that is needed", '''
  <p>Deliver a breath just enough to make the chest rise, then let it fall. Watch the <b>chest</b>, not the bag. A leaking mask gives poor chest movement despite large squeezes; excessive pressure inflates the stomach and injures the lung.</p>''' + evidence('''<p>For an infant or child <b>with a pulse</b> but absent or inadequate breathing, current AHA/AAP guidance is <b>one breath every 2&ndash;3 seconds (20&ndash;30 breaths/min)</b>. This is not the newborn delivery-room pathway. A child without a pulse needs the paediatric CPR sequence with compressions (see the Vikkypaedia PALS module).</p>''', "Rate: breathing support with a pulse") + pearl('''<p><b>The two-person technique</b> &mdash; one person holds the mask with both hands (thumbs on the mask, fingers lifting the jaw), the other squeezes &mdash; gives a far better seal than one tired hand. Use it whenever there are two of you.</p>''')),

   sec(3, "No chest rise: a sequence, not harder squeezing", algo("Troubleshooting absent chest rise", '''  1  REPOSITION   the head and neck for age
  2  RESEAL       the mask; switch to two-person technique
  3  CLEAR        look in the mouth; suction secretions
  4  ADJUNCT      oropharyngeal airway if unconscious with no gag
  5  CHECK        oxygen connected? valve working? bag leaking?
  6  ESCALATE     skilled airway help; consider a supraglottic
                  airway or intubation
  Squeezing harder or faster fills the stomach, not the lungs.''')),

   sec(4, "Avoid overventilation", '''
  <p>Too fast a rate shortens exhalation and causes air trapping, especially in asthma and bronchiolitis. Too much pressure or volume raises intrathoracic pressure, reduces venous return and can drop the blood pressure. Effective ventilation is adequate support with reassessment &mdash; not the fastest possible bagging. Pass a gastric tube if the stomach distends.</p>''' + tracks(
     ["Manometer on the bag circuit; waveform capnography to confirm ventilation",
      "Regular simulation with feedback mannequins"],
     ["A self-inflating bag with a working pop-off valve and a reservoir, checked every shift",
      "Masks in every size on the resuscitation trolley, not in a store room",
      "Bag-mask ventilation done well is a legitimate destination during transfer, not a failure"]), lvl="a"),
  ],
  [Q("You are bagging an unconscious 3-year-old who is breathing inadequately but has a pulse. The chest is not rising. What is your first step?",
     ["Squeeze harder and faster until the chest rises.",
      "Reposition the head and reseal the mask, using a two-person technique if help is available.",
      "Start chest compressions.",
      "Stop ventilating and wait for an anaesthetist."],
     1,
     "What are the two commonest reasons a well-intended breath does not reach the lungs?",
     "Before you blame the lungs, check the path: position and seal. Which option fixes those?",
     "No chest rise is usually a <b>position or seal</b> problem. Reposition the airway and reseal the mask &mdash; ideally with two people &mdash; then suction and use an adjunct if needed.",
     "<b>A</b> &mdash; harder, faster squeezing inflates the stomach and risks lung injury. <b>C</b> &mdash; the child has a pulse; compressions are not indicated. <b>D</b> &mdash; stopping ventilation is dangerous; continue while troubleshooting and calling for help.",
     "Fix the airway before you blame the lungs.",
     "section 3, ‘No chest rise: a sequence, not harder squeezing’", critical=True),
   Q("A 6-year-old with a pulse but only occasional gasps is being bag-mask ventilated. What breathing rate matches current AHA/AAP guidance?",
     ["One breath every 6 seconds (10/min).",
      "One breath every 2&ndash;3 seconds (20&ndash;30/min).",
      "40&ndash;60 breaths/min, as in newborns.",
      "As fast as possible until the saturation reaches 100%."],
     1,
     "Paediatric arrests and near-arrests are mostly respiratory. Did the guidance for children move faster or slower than the adult rate?",
     "For a child with a pulse who is not breathing adequately, current guidance gives one breath every few seconds. Which range is it?",
     "Current AHA/AAP guidance: <b>one breath every 2&ndash;3 seconds (20&ndash;30/min)</b> for an infant or child with a pulse and inadequate breathing.",
     "<b>A</b> &mdash; the older adult-derived rate, too slow for children. <b>C</b> &mdash; the newborn delivery-room rate, not for a 6-year-old. <b>D</b> &mdash; overventilation causes air trapping and hypotension.",
     "Count the rate out loud while you bag. It keeps you from drifting too fast.",
     "section 2, ‘Give only the breath that is needed’")]
)
