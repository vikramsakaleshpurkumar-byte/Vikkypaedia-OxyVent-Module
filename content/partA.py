from gen import *

part("A", "Foundations: see the child, then the number", "Units 1&ndash;3 · ~4 hours",
     "Every device in this module exists to fix one of two problems: getting oxygen into the blood, or getting carbon dioxide out. Part A teaches you to tell them apart at the bedside &mdash; and to notice when a reassuring number is hiding a failing child. It is open from the first minute.")

# ------------------------------------------------------------------ UNIT 1
unit(1, "A", "Start with the child",
  "A deteriorating child needs support while the cause is found. The first skill in respiratory care is not choosing a device &mdash; it is describing what you see so clearly that the next person knows what to do.",
  [("e", "Describe a breathing child by alertness, effort, air entry, perfusion and the reliability of any monitor reading, before naming a diagnosis."),
   ("e", "Make a treatment plan testable: an action, an expected response, a named responder and a reassessment point."),
   ("a", "Call for help in a structure that gets the right person, with the right equipment, quickly."),
   ("x", "Explain what an online assessment can and cannot show about procedural competence.")],
  [
   roles({"ug": "Describe what you see before naming a diagnosis. State the next supervised action and why.",
          "nurse": "Communicate a change from baseline, the current support and the help you need; use closed-loop confirmation.",
          "picu": "Connect the patient trend to device delivery and team response. Identify which observation would change the plan.",
          "pg": "Make the physiological problem explicit, assign immediate actions and define when you will reassess."}),
   sec(1, "Begin with a description", '''
  <p>Before choosing a device, describe five things: <b>alertness</b>, <b>respiratory effort</b>, <b>air entry</b>, <b>pulse and perfusion</b>, and <b>how reliable the monitor reading is</b>. A diagnosis can guide treatment, but a child who is getting worse needs support while the cause is investigated.</p>
  <p>Compare &ldquo;the saturation is 96%&rdquo; with &ldquo;96% on 2 L/min, but he is drowsier and breathing more shallowly than an hour ago&rdquo;. The second sentence exposes a possible failure of ventilation that the first one hides.</p>''' + pearl('''<p><b>Always say what support the number was measured on.</b> 96% in room air and 96% on a non-rebreathing mask are different children.</p>''')),

   sec(2, "Make the plan testable", '''
  <p>State the concern, take an action within your role, then look for a specific response. &ldquo;Will reassess&rdquo; is weaker than &ldquo;I have started oxygen at 1 L/min by prongs; I expect SpO₂ at or above 92% and less recession within 15 minutes; if not, I will call the registrar.&rdquo; Any deterioration triggers review immediately, not at the planned time.</p>''' + algo("A testable plan", '''  CONCERN    what is threatened: oxygenation, ventilation, or both?
  ACTION     what you will do, within your role
  EXPECTED   what improvement should look like, and by when
  OWNER      who reassesses, and who responds if it fails
  FAILURE    the finding that makes you escalate NOW''')),

   sec(3, "Ask for help that arrives useful", '''
  <p>A ward nurse finds a previously alert child hard to rouse on oxygen. A useful call gives <b>who and where</b>, the <b>worsening trend</b>, <b>current support</b>, <b>what has been done</b> and <b>what help is needed</b>. The receiver repeats back the urgent action and says who is coming.</p>''' + tracks(
     ["A rapid response or PICU outreach team with a defined call number and a response time",
      "The caller stays with the child and continues support while help arrives"],
     ["Early escalation also buys time to arrange oxygen for the journey, monitoring, an escort and a receiving team",
      "The local clinician remains responsible for immediate stabilisation while transfer is organised",
      "Write the call-out number for the referral centre on the oxygen trolley, not in a drawer"])),

   sec(4, "What an online result means &mdash; and does not", '''
  <p>A correct first answer is evidence of what you could decide before feedback. A correct repeat after an explanation is evidence of learning with help. Both are useful; <b>neither demonstrates hands-on competence</b>. Bag-mask ventilation, CPAP set-up and airway skills need observation and feedback from a trained assessor on a mannequin and then at the bedside.</p>''' + evidence('''<p>Confidence matters here. Being very sure of a wrong decision is the most dangerous pattern in respiratory care, which is why this module asks how sure you are before every checkpoint and flags &ldquo;confident and wrong&rdquo;.</p>''', "Why you rate your confidence"), tier="good", lvl="a"),
  ],
  [Q("A 3-year-old with pneumonia has SpO₂ 95% on 2 L/min nasal prongs. An hour ago she was talking; now she is sleepy, her breathing is shallower and her respiratory rate has fallen from 52 to 30/min. The handover says &ldquo;sats fine on 2 litres&rdquo;. What is the most accurate description of her state?",
     ["Improving: the saturation is normal and the respiratory rate has come down.",
      "Possibly failing ventilation that the oxygen is hiding: she needs urgent senior review and a CO₂ or blood-gas assessment.",
      "Stable: sleepiness is expected after a tiring day.",
      "Hypoxaemic: the oxygen should be increased to 4 L/min and reviewed at the next observation round."],
     1,
     "What does oxygen do to the saturation of a child who is breathing less?",
     "Put the three changes together &mdash; sleepier, shallower, slower &mdash; and ask whether a normal SpO₂ on oxygen can exclude a rising CO₂.",
     "Drowsiness with shallower, slower breathing after a period of distress suggests <b>exhaustion and hypoventilation</b>. Supplemental oxygen can keep the saturation normal while CO₂ rises, so the number is falsely reassuring. She needs urgent senior review, airway and breathing support as needed, and a CO₂ or blood-gas assessment.",
     "<b>A</b> &mdash; a falling rate with falling consciousness is loss of compensation, not recovery. <b>C</b> &mdash; attributing a change in consciousness to tiredness is the classic error. <b>D</b> &mdash; she is not hypoxaemic; more oxygen treats the wrong problem and delays escalation.",
     "Always hand over the child's trend and the support she is on, not only the best number of the shift.",
     "section 1, ‘Begin with a description’", critical=True),
   Q("Which of these plans for a 10-month-old with bronchiolitis started on oxygen is the most testable?",
     ["&ldquo;Oxygen started, will reassess.&rdquo;",
      "&ldquo;Oxygen as needed to keep sats up.&rdquo;",
      "&ldquo;Oxygen 1 L/min by prongs; aim SpO₂ 92% or above; nurse to recheck effort, rate and SpO₂ in 15 minutes and call the registrar if SpO₂ stays below 92% or recession worsens.&rdquo;",
      "&ldquo;Oxygen at maximum flow until the morning ward round.&rdquo;"],
     2,
     "Which plan tells the next person exactly what success looks like and what to do if it does not happen?",
     "Look for four parts: an action, a target, a named person and time to reassess, and a failure trigger.",
     "A testable plan has an <b>action</b>, an <b>expected response</b>, an <b>owner and time</b> for reassessment, and a <b>failure trigger</b>. Only option C has all four.",
     "<b>A</b> &mdash; no target, no time, no failure plan. <b>B</b> &mdash; &ldquo;sats up&rdquo; has no number and no escalation. <b>D</b> &mdash; a fixed high flow without reassessment can hide deterioration and wastes oxygen.",
     "If the night nurse cannot tell from your plan when to call you, it is not a plan.",
     "section 2, ‘Make the plan testable’")]
)

# ------------------------------------------------------------------ UNIT 2
unit(2, "A", "Recognise distress and failure",
  "Respiratory distress is a child working hard and winning. Respiratory failure is a child working hard and losing &mdash; or no longer able to work at all. The difference is often quiet.",
  [("e", "Recognise signs of increased work of breathing and interpret the respiratory rate for age."),
   ("e", "Recognise the signs of respiratory failure, including the tiring child whose rate is falling."),
   ("a", "Localise the problem &mdash; upper airway, lower airway, lung tissue, or control of breathing &mdash; without letting it delay support."),
   ("x", "Recognise mixed failure: hypoxaemia, hypercapnia and circulatory failure together.")],
  [
   roles({"ug": "Describe the pattern and the physiological threat separately, and justify the urgency of your review.",
          "nurse": "Escalate falling consciousness, weaker effort or worse air entry even if an early-warning score looks reassuring.",
          "picu": "Compare support needs, waveform quality and examination; recognise deterioration before profound desaturation.",
          "pg": "State whether oxygenation, ventilation or both are threatened, and coordinate support with cause-directed evaluation."}),
   sec(1, "Distress can still be compensation", '''
  <p>Fast breathing, recession, nasal flaring, head bobbing and grunting show <b>increased work</b>. An alert child with good air entry may still be maintaining gas exchange &mdash; but distress can progress. Interpret the rate against age, temperature, pain and the child's own baseline.</p>''' + table(
     ["Age", "Fast breathing (WHO/IMNCI)"],
     [["Under 2 months", "60/min or more"], ["2&ndash;11 months", "50/min or more"], ["1&ndash;5 years", "40/min or more"]]) + '''
  <p>Do not reduce severity to one sign. Ask whether the effort is <b>effective</b>: is air moving, can the child interact or feed, is circulation maintained? Reassess after every intervention and record the direction of change.</p>'''),

   sec(2, "Less noise is not improvement", danger('''<p>A previously distressed child who becomes <b>quiet, weak, drowsy or apnoeic</b> may be exhausting. Poor air entry, reduced effort and bradycardia are dangerous findings. A normal saturation on oxygen cannot rule this out. Call skilled help and support breathing now &mdash; do not wait for a blood gas to prove failure.</p>''', "The tiring child") + '''
  <p>Contrast true recovery: easier breathing, <b>better</b> interaction and feeding, better air entry, stable circulation and <b>less</b> support needed.</p>'''),

   sec(3, "Locate the pattern without over-claiming", table(
     ["Pattern", "Clues", "Think of"],
     [["Upper airway", "Inspiratory stridor, hoarse voice, drooling, sniffing posture", "Croup, foreign body, anaphylaxis (Unit 15)"],
      ["Lower airway", "Wheeze, prolonged expiration", "Bronchiolitis (Unit 12), asthma (Unit 14)"],
      ["Lung tissue", "Crackles, grunting, hypoxaemia", "Pneumonia (Unit 13), PARDS (Unit 16)"],
      ["Control of breathing", "Irregular, shallow or absent breathing with little effort", "Raised intracranial pressure, poisoning, seizures, neuromuscular weakness"]]) + pitfall('''<p><b>The silent chest.</b> In severe asthma a nearly silent chest means very little air is moving &mdash; not that the bronchospasm has resolved. Grunting is an attempt to hold lung volume open. Read every sign in the whole-child picture, and never let localisation delay stabilisation.</p>''')),

   sec(4, "Mixed failure", '''
  <p>Hypoxaemia, hypercapnia and circulatory failure often coexist. A child can need oxygen, ventilation support and treatment of poor perfusion at the same time. When the response to one intervention is incomplete, ask which other mechanism is still unaddressed.</p>''', tier="good", lvl="a"),
  ],
  [Q("A 4-year-old with severe wheeze was alert with RR 48/min and marked recession. Thirty minutes later RR is 24/min, she is drowsy, her speech is weaker and air entry is reduced. SpO₂ is 93% on a non-rebreathing mask. What is happening?",
     ["She is responding to treatment: the rate has halved.",
      "She is exhausting: call experienced help, support breathing and prepare to escalate.",
      "She has fallen asleep from salbutamol; let her rest.",
      "Her wheeze is resolving, so the nebulisers can be reduced."],
     1,
     "What else changed at the same time as the respiratory rate?",
     "Recovery brings easier breathing and better interaction. Here consciousness and air entry fell with the rate. What does that combination mean?",
     "A falling rate with <b>falling consciousness, weaker speech and reduced air entry</b> is loss of compensation &mdash; exhaustion. Call for help, support breathing and prepare escalation. Hand over the paired observations so &ldquo;RR improved&rdquo; is not mistaken for recovery.",
     "<b>A</b> &mdash; the rate fell for the wrong reason. <b>C</b> &mdash; salbutamol causes tachycardia and tremor, not drowsiness with poor air entry. <b>D</b> &mdash; reduced air entry is a quieter chest, which in severe asthma is a danger sign.",
     "When a struggling child goes quiet, find out why before you relax.",
     "section 2, ‘Less noise is not improvement’", critical=True),
   Q("A 7-month-old has noisy breathing. Which finding most strongly suggests the problem is in the upper airway?",
     ["Crackles at the right base.",
      "Expiratory wheeze throughout both lungs.",
      "Inspiratory stridor with a hoarse cry.",
      "Irregular breathing with long pauses and little effort."],
     2,
     "Which phase of breathing makes noise when the narrowing is above the chest?",
     "Upper-airway narrowing is worst when the airway is sucked in during inspiration. Which option describes an inspiratory noise?",
     "<b>Inspiratory stridor with a hoarse cry</b> points to narrowing at or near the larynx &mdash; an upper-airway pattern.",
     "<b>A</b> &mdash; crackles suggest lung-tissue disease. <b>B</b> &mdash; expiratory wheeze suggests lower-airway obstruction. <b>D</b> &mdash; irregular breathing with little effort suggests a problem with the control of breathing.",
     "Localise, then support. The pattern tells you which device and which danger to expect.",
     "section 3, ‘Locate the pattern without over-claiming’")]
)

# ------------------------------------------------------------------ UNIT 3
unit(3, "A", "Oxygenation is not ventilation",
  "Oxygenation puts oxygen into blood; ventilation takes carbon dioxide out. They fail for different reasons, respond to different treatments, and &mdash; most dangerously &mdash; a pulse oximeter only watches one of them.",
  [("e", "Explain the difference between oxygenation and ventilation, and why supplemental oxygen can hide hypoventilation."),
   ("e", "Explain why saturation is a proportion, and why an anaemic or shocked child can be well saturated but poorly oxygenated."),
   ("a", "Name the four mechanisms of hypoxaemia and predict which respond to oxygen."),
   ("x", "Use minute and alveolar ventilation to explain why rapid shallow breathing clears little CO₂.")],
  [
   roles({"ug": "Explain the oxygen-delivery chain from lungs to haemoglobin to cardiac output.",
          "nurse": "Recognise when a satisfactory saturation does not match the child's state, and request review.",
          "picu": "Integrate blood-gas and CO₂ trends with support, perfusion and oxygenation.",
          "pg": "Identify the mechanism limiting delivery or ventilation and choose the next investigation without delaying support."}),
   sec(1, "Two different jobs", '''
  <p><b>Oxygenation</b> transfers oxygen into blood. <b>Ventilation</b> clears carbon dioxide. Alveolar ventilation depends on useful gas reaching gas-exchanging lung, not on the number of breaths. Rapid shallow breaths waste much of each breath in dead space.</p>
  <p>Supplemental oxygen can maintain SpO₂ despite falling ventilation. If breathing is shallow or consciousness worsens, ask about CO₂ clearance: a normal saturation cannot answer that question.</p>''' + algo("Minute and alveolar ventilation", '''  minute ventilation   = tidal volume × rate
  alveolar ventilation = (tidal volume − dead space) × rate

  Child A: 150 mL × 20/min = 3.0 L/min   dead space 50 mL
           alveolar = (150 − 50) × 20 = 2.0 L/min
  Child B:  75 mL × 40/min = 3.0 L/min   dead space 50 mL
           alveolar = (75 − 50) × 40 = 1.0 L/min
  Same minute ventilation. Child B clears half the CO2.''')),

   sec(2, "Saturation is a proportion, not a quantity", '''
  <p>Most oxygen in blood is carried on haemoglobin. <b>Saturation</b> is the proportion of that carrier which is occupied. A severely anaemic child can have 98% saturation and still too little oxygen content. Tissue delivery also depends on <b>cardiac output</b>: well-saturated blood that does not flow does not oxygenate organs.</p>''' + table(
     ["Three children, all SpO₂ 98%", "What is really happening"],
     [["Comfortable, in room air", "Well"],
      ["Severe anaemia (Hb 4 g/dL), poor perfusion", "Low oxygen content and delivery &mdash; needs blood and circulatory support"],
      ["Drowsy, shallow breathing, on oxygen", "Possible hypoventilation masked by oxygen &mdash; needs CO₂ assessment and breathing support"]])),

   sec(3, "Why the same oxygen has different effects", table(
     ["Mechanism", "Example", "Responds to more oxygen?"],
     [["Low inspired oxygen", "Altitude", "Yes"],
      ["Hypoventilation", "Opioid, exhaustion, neuromuscular weakness", "Saturation improves, but CO₂ keeps rising &mdash; the real treatment is ventilation"],
      ["Ventilation/perfusion mismatch", "Pneumonia, bronchiolitis, asthma", "Usually yes"],
      ["Shunt", "Collapsed or flooded lung, cyanotic heart disease", "Poorly &mdash; needs recruitment (PEEP/CPAP) or treatment of the cause"]]) + pearl('''<p>If a child needs more and more oxygen for less and less effect, think <b>shunt</b>: the lung needs opening (CPAP, PEEP), not just a higher FiO₂.</p>'''), lvl="a"),

   sec(4, "The curve is a warning about reserve", '''
  <p>The oxyhaemoglobin dissociation curve is flat at high oxygen tensions and steep lower down. Once a child reaches the steep part, a small fall in oxygen tension produces a fast fall in saturation. That is why a child &ldquo;holding&rdquo; at 90&ndash;92% can desaturate abruptly &mdash; watch trends and reserve, not a single number. The curve's position shifts with temperature, pH and CO₂; it is not a calculator for converting an unreliable SpO₂ reading.</p>''', tier="good"),
  ],
  [Q("Three children each have SpO₂ 98%. Which one is most likely to have inadequate oxygen delivery to the tissues despite this reading?",
     ["A comfortable child with bronchiolitis in room air.",
      "A child with haemoglobin 4 g/dL, cold peripheries and capillary refill of 5 seconds.",
      "A child with a cough who is playing.",
      "A child recovering from asthma, breathing comfortably on 1 L/min."],
     1,
     "What else, apart from saturation, determines how much oxygen reaches the organs?",
     "Oxygen delivery depends on saturation, haemoglobin and cardiac output. Which child is short of the other two?",
     "Oxygen delivery depends on <b>saturation × haemoglobin × cardiac output</b>. The child with Hb 4 g/dL and poor perfusion has a normal saturation but little carrier and little flow &mdash; tissue oxygen delivery is poor.",
     "<b>A</b>, <b>C</b> and <b>D</b> &mdash; each has adequate haemoglobin and circulation; the saturation reflects their state reasonably.",
     "A saturation tells you how full the lorries are, not how many lorries there are or whether they are moving.",
     "section 2, ‘Saturation is a proportion, not a quantity’"),
   Q("A 9-year-old with Guillain&ndash;Barr&eacute; syndrome has shallow breathing. On 2 L/min oxygen his SpO₂ is 97%, but he is becoming drowsy. What is the main danger the saturation is not showing?",
     ["Hypoxaemia from pneumonia.",
      "Rising carbon dioxide from hypoventilation.",
      "Anaemia.",
      "Oxygen toxicity."],
     1,
     "Which respiratory job fails first when the muscles are weak?",
     "Oxygen can keep the saturation normal. What gas builds up when breathing is shallow, and what does it do to consciousness?",
     "Weak, shallow breathing causes <b>hypoventilation</b>: CO₂ rises and consciousness falls, while supplemental oxygen keeps the saturation normal. He needs CO₂ assessment and ventilatory support, not reassurance from the oximeter.",
     "<b>A</b> &mdash; his saturation is normal on oxygen; hypoxaemia is not the problem shown. <b>C</b> &mdash; nothing suggests anaemia. <b>D</b> &mdash; 2 L/min is not toxic; the danger is what the oxygen hides.",
     "In neuromuscular weakness, watch the effort and the CO₂, not the saturation.",
     "section 1, ‘Two different jobs’", critical=True)]
)
