from gen import *

part("D", "The diseases", "Units 12&ndash;16 · ~7 hours",
     "Most children who need oxygen or breathing support have one of five problems: bronchiolitis, pneumonia, asthma, upper-airway obstruction or paediatric ARDS. Each has its own current guideline, its own tempting over-treatment, and its own sign of danger. This Part puts the devices of Parts B and C into the hands of the disease.")

# ------------------------------------------------------------------ UNIT 12
unit(12, "D", "Bronchiolitis",
  "Bronchiolitis is the commonest reason infants need oxygen, and the commonest place where treatments that do not work are still given. The 2025 Australasian guideline is short on what to give and long on what not to.",
  [("e", "Diagnose bronchiolitis clinically and identify infants at higher risk of severe disease."),
   ("e", "Apply the 2025 oxygen thresholds and the stepwise use of low-flow oxygen, high-flow and CPAP."),
   ("a", "Name the treatments that are not recommended, and explain to a family why."),
   ("x", "Plan hydration, monitoring and discharge, and recognise the infant who needs intensive care.")],
  [
   roles({"ug": "Recognise the typical illness and state why bronchodilators and steroids are not routinely used.",
          "nurse": "Monitor feeding, work of breathing, apnoea and SpO₂; support nasal suction and feeding; escalate apnoea or rising oxygen needs.",
          "picu": "Recognise high-flow and CPAP failure early; manage apnoea and fatigue in young infants.",
          "pg": "Apply the thresholds and stepwise support, resist non-evidence-based treatment, and decide on escalation and discharge."}),
   sec(1, "Diagnosis and risk", '''
  <p>A viral lower-respiratory infection of infants (typically under 12 months, peak 2&ndash;6 months), often RSV: coryza for a few days, then cough, fast breathing, recession, crackles and/or wheeze. It is a <b>clinical diagnosis</b>; routine chest X-ray and blood tests are not needed. The illness typically worsens over days 3&ndash;5 before improving.</p>''' + table(
     ["Higher risk of severe disease"],
     [["Age under 6&ndash;12 weeks, prematurity"], ["Chronic lung disease, haemodynamically significant heart disease"], ["Neuromuscular disease, immunodeficiency, trisomy 21"], ["Economic disadvantage, and presentation early in the illness"]]) + danger('''<p><b>Apnoea</b> can be the presenting feature in young infants, especially preterm infants under 2 months, and may occur before significant respiratory distress.</p>''')),

   sec(2, "Oxygen and respiratory support, step by step", table(
     ["Step", "2025 Australasian guideline"],
     [["Start oxygen", "SpO₂ persistently below 90% from 6 weeks of age; below 92% if under 6 weeks or with underlying conditions"],
      ["High-flow", "Not routinely in infants with mild or moderate disease who are not hypoxaemic; for those who fail low-flow oxygen or have severe disease, before CPAP"],
      ["CPAP", "Consider in impending or severe respiratory failure"],
      ["Intensive care", "CPAP failure, recurrent apnoea, exhaustion, rising CO₂"]]) + '''
  <p>Do not chase 100%. Short dips below the threshold during sleep or feeding in an otherwise improving infant do not by themselves require oxygen.</p>'''),

   sec(3, "What not to give", table(
     ["Treatment", "Position (2025 Australasian guideline)"],
     [["Salbutamol and other beta-2 agonists", "<b>Strongly against</b> in infants under 12 months"],
      ["Glucocorticoids", "<b>Strongly against</b> routine use"],
      ["Antibiotics", "Not routinely"],
      ["Nebulised hypertonic saline", "Not routinely"],
      ["Adrenaline (nebulised)", "Not routinely; combination steroid plus inhaled adrenaline may be considered in severe disease needing intensive care"],
      ["Chest physiotherapy", "Not recommended"]]) + pitfall('''<p>&ldquo;Just try a nebuliser&rdquo;. In infants with bronchiolitis, bronchodilators do not change the course, cause tachycardia and distress, and delay recognition of the infant who needs support. Say to the family: &ldquo;The medicine that helps asthma does not help this virus; what helps is oxygen if she needs it, feeding support, and watching her closely.&rdquo;</p>''')),

   sec(4, "Feeding, hydration and discharge", '''
  <ul>
    <li><b>Hydration:</b> if oral feeding is inadequate, use nasogastric or intravenous fluids; the guideline prefers nasogastric first in moderate bronchiolitis. Infants with bronchiolitis can retain water (SIADH): many protocols restrict to 50&ndash;75% of maintenance and use isotonic fluids.</li>
    <li><b>Nasal suction:</b> gentle superficial suction before feeds can help; avoid routine deep suction.</li>
    <li><b>Discharge:</b> when clinically stable, taking enough feeds, and maintaining SpO₂ above the threshold in room air &mdash; with clear safety-net advice.</li>
  </ul>''' + india('''<p>RSV is a major cause of infant hospitalisation in India. Newer prevention &mdash; long-acting monoclonal antibodies for infants and maternal RSV vaccination &mdash; is recommended in several countries; check its current approval and availability in India before advising families. In Indian settings, overcrowded wards and shared equipment make hand hygiene and cohorting the most effective infection-control measures you control.</p>'''), tier="must", lvl="a"),
  ],
  [Q("A 4-month-old with bronchiolitis has SpO₂ 93% in room air, moderate recession and is feeding half her usual volume. Her parents ask for &ldquo;the nebuliser that worked for her cousin's asthma&rdquo;. What is the best plan?",
     ["Give nebulised salbutamol and review the response.",
      "Give oral prednisolone for 3 days.",
      "Support feeding (nasogastric if needed), monitor closely, no bronchodilator or steroid, and explain why to the parents.",
      "Start high-flow nasal cannula now."],
     2,
     "Which treatments does the 2025 guideline strongly recommend against in infants?",
     "She is not hypoxaemic (93% is above the threshold for her age). Her main problem is feeding. What helps, and what does not?",
     "Bronchodilators and steroids are <b>strongly recommended against</b> in infants with bronchiolitis. She is above the oxygen threshold; her problem is feeding. Support hydration (nasogastric first), monitor, and explain to the family.",
     "<b>A</b> &mdash; salbutamol does not help bronchiolitis and is strongly recommended against in infants under 12 months. <b>B</b> &mdash; steroids are strongly recommended against. <b>D</b> &mdash; high-flow is not for infants who are not hypoxaemic with moderate disease.",
     "In bronchiolitis, the most powerful treatment is often the one you decide not to give.",
     "section 3, ‘What not to give’"),
   Q("A 6-week-old former 32-week preterm baby with day 2 of bronchiolitis has a 20-second apnoea with brief desaturation, then recovers with stimulation. SpO₂ is now 94% in room air. What should happen?",
     ["Discharge home, as the saturation is normal.",
      "Admit with continuous cardiorespiratory monitoring and a plan for escalation (including CPAP) if apnoeas recur.",
      "Give caffeine and discharge.",
      "Start antibiotics for sepsis and discharge on oral treatment."],
     1,
     "Which infants with bronchiolitis are at risk of apnoea, and what does an apnoea predict?",
     "A young, formerly preterm infant with an apnoea early in the illness is at high risk. What level of monitoring does that need?",
     "A young, formerly preterm infant with <b>apnoea</b> is at high risk of further apnoeas and deterioration, particularly as the illness peaks over the next days. Admit with <b>continuous monitoring</b> and an escalation plan, including CPAP if apnoeas recur.",
     "<b>A</b> &mdash; a normal saturation now does not protect against the next apnoea. <b>C</b> &mdash; caffeine is not standard for bronchiolitis apnoea and does not replace monitoring. <b>D</b> &mdash; discharging an infant who has had apnoea is unsafe; antibiotics are not routinely needed.",
     "In young infants with bronchiolitis, apnoea is the warning sign that comes before distress.",
     "section 1, ‘Diagnosis and risk’", critical=True)]
)

# ------------------------------------------------------------------ UNIT 13
unit(13, "D", "Pneumonia",
  "Pneumonia remains the single largest infectious killer of children under five, and hypoxaemia is its most dangerous companion. The 2024 WHO guideline simplified antibiotics; oxygen is still the intervention most often missing.",
  [("e", "Classify pneumonia using WHO signs, including fast breathing, chest indrawing and danger signs."),
   ("e", "Apply the 2024 WHO antibiotic recommendations for children aged 2&ndash;59 months."),
   ("a", "Detect hypoxaemia with pulse oximetry, and use clinical signs when oximetry is unavailable."),
   ("x", "Escalate from oxygen to bubble CPAP or ventilation, and recognise complications: empyema, effusion, sepsis.")],
  [
   roles({"ug": "Classify pneumonia by WHO signs and explain why every child with pneumonia needs a saturation check.",
          "nurse": "Check SpO₂ at triage and during admission; start and titrate oxygen to the prescribed target; escalate rising needs.",
          "picu": "Recognise pneumonia with respiratory failure or sepsis; prepare for CPAP, NIV or intubation.",
          "pg": "Choose antibiotics by WHO category and local resistance; decide oxygen, CPAP and referral; look for complications."}),
   sec(1, "Classify by WHO signs", table(
     ["Signs (children 2&ndash;59 months)", "Classification", "Management (WHO 2024)"],
     [["Fast breathing only", "Pneumonia", "Oral amoxicillin for <b>3 or 5 days</b> (strong recommendation), at home"],
      ["Chest indrawing, no danger signs", "Pneumonia with chest indrawing", "Oral amoxicillin for <b>5 days</b> in the outpatient setting rather than injectable antibiotics (strong)"],
      ["Any danger sign (unable to drink, convulsions, lethargy or unconsciousness, stridor in a calm child, severe malnutrition) or SpO₂ below 90%", "Severe pneumonia", "Admit; injectable antibiotics (commonly ampicillin or penicillin plus gentamicin, per WHO hospital guidance); oxygen; supportive care"]]) + evidence('''<p>WHO. <i>Guideline on management of pneumonia and diarrhoea in children up to 10 years of age.</i> Geneva: WHO; 2024. Other new points: where pulse oximetry is unavailable, a combination of respiratory-distress signs may help identify hypoxaemia (conditional, very-low-certainty evidence); community health workers with oral amoxicillin and follow-up are an option where referral is difficult; there was insufficient evidence to recommend lung ultrasound or digital auscultation routinely.</p>''', "Source")),

   sec(2, "Hypoxaemia: find it, treat it", '''
  <p>Hypoxaemia is the strongest predictor of death in childhood pneumonia, and clinical signs miss a large proportion of it. <b>Every child with pneumonia needs a saturation check</b>, at triage and repeatedly. Give oxygen for SpO₂ below 90% (Unit 5), titrate, and wean when stable above 90% in room air.</p>''' + pitfall('''<p>Treating a child with chest indrawing as &ldquo;severe&rdquo; by reflex and admitting for injections &mdash; while never measuring the saturation. The 2024 guideline moved chest indrawing without danger signs to <b>outpatient oral amoxicillin</b>; the decision that matters more is whether the child is hypoxaemic.</p>''')),

   sec(3, "When oxygen is not enough", '''
  <p>Persistent severe distress, grunting and rising oxygen needs mean the child may benefit from <b>bubble CPAP</b> (Unit 9) where a monitored system exists, or from ventilation. Look for complications that change the plan: <b>pleural effusion or empyema</b> (dull percussion, reduced air entry, persisting fever &mdash; ultrasound and drainage), <b>septic shock</b> (Sick Child module), <b>pneumothorax</b>, and heart failure (big liver, gallop &mdash; consider congenital heart disease).</p>''' + tracks(
     ["Chest X-ray and ultrasound for complications; blood culture; PICU for respiratory failure",
      "Staphylococcal pneumonia or necrotising pneumonia recognised and treated early"],
     ["Pulse oximetry and oxygen are the two interventions that most change mortality: make sure both exist at every point of care",
      "Oral amoxicillin for non-severe pneumonia reduces unnecessary admission and injections",
      "Refer early for complications or failure of oxygen, with oxygen for the journey"]), lvl="a"),

   sec(4, "Prevention", india('''<p>India introduced pneumococcal conjugate vaccine into the Universal Immunization Programme in phases from 2017, reaching national coverage later; Hib vaccine is part of the pentavalent vaccine. Pneumonia also tracks malnutrition, indoor air pollution (solid-fuel cooking) and poor access to care. The national <b>SAANS</b> campaign (Social Awareness and Action to Neutralise Pneumonia Successfully) focuses on early recognition, pulse oximetry and oxygen at facilities.</p>'''), tier="good"),
  ],
  [Q("A 2-year-old has cough and fever for 3 days. Respiratory rate 46/min, lower chest wall indrawing, no danger signs, able to drink. SpO₂ 95% in room air. According to WHO 2024, what is the recommended management?",
     ["Admit for IV ampicillin and gentamicin.",
      "Oral amoxicillin for 5 days as an outpatient, with a follow-up plan.",
      "No antibiotics; this is viral.",
      "Oral amoxicillin for 10 days."],
     1,
     "What changed in the 2024 guideline for chest indrawing without danger signs?",
     "Chest indrawing, no danger signs, normal saturation. Which setting and route does WHO now recommend?",
     "WHO 2024 recommends <b>oral amoxicillin for 5 days in the outpatient setting</b> for children with chest indrawing and no danger signs (strong recommendation), with follow-up. Her saturation is normal.",
     "<b>A</b> &mdash; injectable antibiotics are for severe pneumonia (danger signs or hypoxaemia). <b>C</b> &mdash; WHO recommends antibiotics for this classification. <b>D</b> &mdash; 10 days is longer than recommended.",
     "Classification sets the antibiotic. The oximeter decides whether the child needs oxygen and admission.",
     "section 1, ‘Classify by WHO signs’"),
   Q("At a PHC with no pulse oximeter, a 14-month-old with pneumonia has fast breathing, chest indrawing, head nodding and grunting, and is too breathless to feed. What should you do?",
     ["Treat as non-severe pneumonia with oral amoxicillin at home.",
      "Treat as severe pneumonia with probable hypoxaemia: give oxygen if available, the first dose of antibiotics, and refer urgently with oxygen for the journey.",
      "Wait until a pulse oximeter is available before deciding.",
      "Give salbutamol and send home if the breathing improves."],
     1,
     "Is he able to drink? Which signs suggest hypoxaemia when no oximeter is available?",
     "Inability to feed is a danger sign. Head nodding and grunting are signs of severe distress often associated with hypoxaemia. What category is this?",
     "Inability to feed is a <b>danger sign</b>, so this is <b>severe pneumonia</b>; head nodding and grunting suggest hypoxaemia. Give oxygen if available, the first antibiotic dose, and refer urgently with oxygen for the journey.",
     "<b>A</b> &mdash; misses the danger sign. <b>C</b> &mdash; lack of an oximeter must not delay treatment; use clinical signs. <b>D</b> &mdash; salbutamol does not treat pneumonia, and sending him home is unsafe.",
     "When you cannot measure oxygen, the child's work of breathing is your oximeter.",
     "section 2, ‘Hypoxaemia: find it, treat it’", critical=True)]
)

# ------------------------------------------------------------------ UNIT 14
unit(14, "D", "Acute asthma",
  "Children rarely die of asthma suddenly. They die after hours of under-treatment, a quiet chest mistaken for improvement, and a sedative given to a frightened child who was tiring.",
  [("e", "Grade the severity of an acute asthma attack in a child."),
   ("e", "Give first-hour treatment: inhaled short-acting bronchodilator by spacer, oxygen to target, systemic steroid."),
   ("a", "Escalate severe or life-threatening asthma with ipratropium and intravenous magnesium."),
   ("x", "Recognise the dangers of ventilating a child with asthma, and how to ventilate safely if you must.")],
  [
   roles({"ug": "Grade severity from speech, effort, saturation and chest sounds, and name the first-hour treatments.",
          "nurse": "Deliver inhaled treatment by spacer correctly; monitor SpO₂, heart rate and effort; recognise the quiet chest and escalate.",
          "picu": "Watch for exhaustion and rising CO₂; prepare for the risks of ventilating an obstructed child.",
          "pg": "Lead escalation to magnesium and intensive care; avoid sedation; plan safe ventilation if needed."}),
   sec(1, "Grade the attack", table(
     ["", "Mild to moderate", "Severe", "Life-threatening"],
     [["Talks in", "Phrases or sentences", "Words", "Unable to talk; drowsy or confused"],
      ["Position", "Prefers sitting", "Sits hunched forward", "Exhausted"],
      ["Effort", "Increased", "Marked, accessory muscles", "Poor effort"],
      ["Chest", "Wheeze", "Loud wheeze", "<b>Silent chest</b>"],
      ["SpO₂ in air", "90&ndash;95%", "Below 90%", "Below 90%, cyanosis"],
      ["Heart rate", "Raised", "Very raised", "Bradycardia is pre-terminal"]]) + danger('''<p>A <b>silent chest</b>, drowsiness, poor effort, cyanosis or a falling heart rate are signs of life-threatening asthma. Wheeze gets quieter as air movement falls &mdash; not as the child gets better.</p>''')),

   sec(2, "The first hour", algo("Acute asthma — first hour (GINA; ages 6–11 shown)", '''  OXYGEN            to SpO2 94–98%
  SALBUTAMOL        by pMDI + spacer: 4–10 puffs every 20 minutes
                    for the first hour (nebulised if severe or
                    oxygen-driven delivery is needed)
                    ages 5 and under: 2 puffs (up to 6) by spacer
                    with mask, repeated every 20 minutes
  IPRATROPIUM       add in moderate–severe attacks during the
                    first hour
  SYSTEMIC STEROID  oral prednisolone 1–2 mg/kg (max 40 mg for
                    ages 6–11) — give early; IV if unable to swallow
  REASSESS          after each round: speech, effort, SpO2, air entry''') + evidence('''<p>The Global Initiative for Asthma (GINA) strategy is updated annually; the 2025 and 2026 reports revised charts for young children. Doses above follow GINA for children aged 6&ndash;11; verify doses for younger children and your local protocol in Appendix E. A pMDI with a spacer is as effective as a nebuliser for most attacks, faster to give and cheaper.</p>''', "Source and dosing")),

   sec(3, "When the first hour is not enough", '''
  <ul>
    <li><b>Intravenous magnesium sulphate</b> 40&ndash;50 mg/kg (maximum 2 g) over 20 minutes for severe or life-threatening asthma not responding to initial treatment.</li>
    <li>Continuous or back-to-back salbutamol; consider IV salbutamol or aminophylline in intensive care per local protocol.</li>
    <li>Blood gas: a <b>normal or rising CO₂</b> in a breathless child is a sign of exhaustion.</li>
    <li>No sedatives outside intensive care. An anxious child with severe asthma is anxious because they cannot breathe.</li>
  </ul>''', lvl="a"),

   sec(4, "If you must ventilate", danger('''<p>Intubating a child with severe asthma is high-risk: air trapping, hypotension on induction, pneumothorax and cardiac arrest. It is indicated for exhaustion, falling consciousness, or arrest. Use a slow rate with a long expiratory time, accept a high CO₂ (permissive hypercapnia), limit pressures, and if the child collapses on the ventilator, <b>disconnect briefly to let trapped gas out</b> and check for pneumothorax. Bag slowly: fast bagging worsens air trapping.</p>''', "Ventilating the obstructed child") + tracks(
     ["PICU with ventilation expertise, arterial line and blood gases", "IV magnesium, salbutamol and aminophylline infusions available"],
     ["pMDI and spacer (a plastic bottle spacer if nothing else) in every clinic and ward",
      "Oxygen, oral prednisolone and IV magnesium are cheap and on the essential medicines list: make sure they are stocked",
      "Refer severe asthma not responding to first-hour treatment early, with oxygen and salbutamol for the journey"]), lvl="x"),
  ],
  [Q("A 9-year-old with asthma can say only single words, is sitting hunched forward, and has SpO₂ 88% in room air and a loud wheeze. What are the first-hour treatments?",
     ["Oral salbutamol syrup and review in 2 hours.",
      "Oxygen to 94&ndash;98%, inhaled salbutamol repeated every 20 minutes, ipratropium, and early oral or IV steroid.",
      "Sedation to calm her, then salbutamol.",
      "A course of antibiotics."],
     1,
     "How severe is this attack, and what does GINA give in the first hour?",
     "Single words and SpO₂ below 90% mean severe asthma. Which option combines oxygen, repeated inhaled bronchodilator, ipratropium and steroid?",
     "Single words, hunched posture and SpO₂ 88% indicate <b>severe asthma</b>. Give <b>oxygen</b> to 94&ndash;98%, <b>inhaled salbutamol every 20 minutes</b>, <b>ipratropium</b>, and an <b>early systemic steroid</b>.",
     "<b>A</b> &mdash; oral salbutamol is slow and less effective. <b>C</b> &mdash; sedation in severe asthma can precipitate respiratory arrest. <b>D</b> &mdash; antibiotics do not treat an asthma attack.",
     "Oxygen, bronchodilator, steroid &mdash; early, and all three.",
     "section 2, ‘The first hour’"),
   Q("After an hour of treatment, a 7-year-old with severe asthma is quieter: the wheeze has almost disappeared, but she is drowsy and air entry is poor on both sides. SpO₂ is 90% on oxygen. What does this mean?",
     ["She has responded well; step down treatment.",
      "Life-threatening asthma with exhaustion (silent chest): give IV magnesium, call senior and intensive-care help, and prepare for ventilation.",
      "She is sleepy from salbutamol; let her rest.",
      "The wheeze has resolved, so she can be discharged."],
     1,
     "Why does wheeze disappear in severe asthma?",
     "A quieter chest with poor air entry and drowsiness is not improvement. What is it?",
     "A <b>silent chest</b> with poor air entry and drowsiness is <b>life-threatening asthma</b>. Give IV magnesium, call senior and intensive-care help, check a blood gas and prepare for ventilation.",
     "<b>A</b> &mdash; mistakes a silent chest for recovery. <b>C</b> &mdash; drowsiness is a sign of exhaustion or hypercapnia. <b>D</b> &mdash; discharge would be fatal.",
     "Listen for air entry, not for wheeze. A quiet chest can be a very dangerous chest.",
     "section 1, ‘Grade the attack’", critical=True)]
)

# ------------------------------------------------------------------ UNIT 15
unit(15, "D", "Upper-airway obstruction",
  "In upper-airway obstruction, the enemy is anything that makes the child cry, lie flat or panic. The treatment is often less intervention, done faster, by the right person.",
  [("e", "Recognise upper-airway obstruction and keep the child calm while help arrives."),
   ("e", "Treat croup by severity, and manage choking in infants and children."),
   ("a", "Recognise anaphylaxis, epiglottitis, bacterial tracheitis and retropharyngeal abscess, and act on each."),
   ("x", "Plan the airway for a child with severe upper-airway obstruction.")],
  [
   roles({"ug": "Recognise stridor and explain why the child must not be upset or laid flat.",
          "nurse": "Keep the child with the parent, give oxygen without distress, give nebulised adrenaline as prescribed, and escalate.",
          "picu": "Prepare for a difficult airway with the most experienced operator and surgical backup.",
          "pg": "Decide on steroids, adrenaline and airway intervention; coordinate anaesthesia and ENT for severe obstruction."}),
   sec(1, "Croup", table(
     ["Severity", "Features", "Treatment"],
     [["Mild", "Barking cough, no stridor at rest", "<b>Oral dexamethasone</b> 0.15&ndash;0.6 mg/kg single dose (0.15 mg/kg is often enough for mild croup); home with advice"],
      ["Moderate", "Stridor at rest, some recession, alert", "Dexamethasone; observe; nebulised adrenaline if distress increases"],
      ["Severe", "Marked stridor and recession, agitation, or drowsiness", "<b>Nebulised adrenaline</b> (1 mg/mL solution, 0.5 mL/kg, maximum 5 mL) plus dexamethasone; oxygen; observe at least 2&ndash;4 hours after adrenaline; senior help"],
      ["Impending failure", "Drowsy, cyanosed, quiet stridor, poor effort", "Emergency airway by the most skilled operator"]]) + pitfall('''<p>Distressing the child: examining the throat with a tongue depressor, taking blood, or separating the child from the parent. Crying increases turbulent flow and can precipitate complete obstruction. Keep the child on the parent's lap.</p>''')),

   sec(2, "Choking", algo("Foreign-body airway obstruction", '''  EFFECTIVE COUGH (crying, talking, breathing)
     encourage coughing · watch closely · do not interfere
  INEFFECTIVE COUGH, conscious
     INFANT:  5 back blows, then 5 chest thrusts — repeat
     CHILD:   5 back blows, then 5 abdominal thrusts — repeat
  UNCONSCIOUS
     open the airway, look and remove only a visible object
     5 rescue breaths, then CPR — look in the mouth before breaths
  Never blind finger sweeps.''')),

   sec(3, "Other causes you must not miss", table(
     ["Condition", "Clues", "Action"],
     [["<b>Anaphylaxis</b>", "Sudden onset after exposure; urticaria, facial swelling, stridor or wheeze, hypotension", "<b>IM adrenaline 0.01 mg/kg</b> (1 mg/mL; max 0.5 mg), repeat after 5 minutes; oxygen; fluids for shock"],
      ["<b>Epiglottitis</b> (rare since Hib vaccine)", "Toxic, high fever, drooling, tripod posture, muffled voice, little cough", "Do not examine the throat; keep calm; senior anaesthetist and ENT; airway in theatre; IV antibiotics after the airway is secure"],
      ["<b>Bacterial tracheitis</b>", "Croup-like illness that becomes toxic, with thick secretions, poor response to adrenaline", "Airway support, often intubation; IV antibiotics"],
      ["<b>Retropharyngeal abscess</b>", "Fever, neck stiffness or refusal to move neck, drooling, stridor", "Imaging when stable; antibiotics; ENT drainage"]]), lvl="a"),

   sec(4, "Airway planning in severe obstruction", danger('''<p>A child with severe upper-airway obstruction may lose the airway at induction. The airway should be managed by the most experienced operator available, in the safest place available (often theatre), with a smaller-than-predicted tube, a surgical airway option and ENT support ready. Keep the child sitting and breathing spontaneously until the team is ready.</p>''', "The difficult airway") + tracks(
     ["Theatre with anaesthesia and ENT for epiglottitis or severe obstruction", "Rigid bronchoscopy for inhaled foreign bodies"],
     ["Dexamethasone and nebulised adrenaline are cheap and widely available: stock both",
      "If no one can manage a difficult airway, transfer early, with the child sitting on a parent's lap, oxygen, and adrenaline for the journey",
      "Bag-mask ventilation with a good seal can often ventilate through upper-airway obstruction while help arrives"]), lvl="x"),
  ],
  [Q("A 2-year-old with croup has stridor at rest, marked recession and is agitated. SpO₂ is 94%. What is the best immediate treatment?",
     ["Examine the throat with a tongue depressor to look for a foreign body.",
      "Nebulised adrenaline (1 mg/mL, 0.5 mL/kg, max 5 mL) and dexamethasone, keeping her calm on her parent's lap, with senior review.",
      "Antibiotics and review in 4 hours.",
      "Salbutamol nebuliser."],
     1,
     "What reduces airway swelling within minutes, and what reduces it over hours?",
     "Severe croup needs a fast-acting drug and a slower one. Which option gives both, without distressing the child?",
     "This is <b>severe croup</b>. <b>Nebulised adrenaline</b> reduces swelling within minutes; <b>dexamethasone</b> works over hours. Keep her calm on the parent's lap and involve a senior. Observe for at least 2&ndash;4 hours after adrenaline.",
     "<b>A</b> &mdash; examining the throat can precipitate complete obstruction. <b>C</b> &mdash; croup is viral; antibiotics do not help. <b>D</b> &mdash; salbutamol treats lower-airway bronchospasm, not laryngeal swelling.",
     "In croup, a calm child is part of the treatment.",
     "section 1, ‘Croup’", critical=True),
   Q("A 10-month-old choked on a piece of food. He is conscious but cannot cry or cough effectively and is turning blue. What should you do?",
     ["Five back blows, then five chest thrusts, repeated until the object comes out or he becomes unconscious.",
      "Blind finger sweep of the mouth.",
      "Abdominal thrusts.",
      "Give water to wash the food down."],
     0,
     "How does the choking sequence differ between infants and older children?",
     "The cough is ineffective, so you must intervene. For an infant, which thrusts are used after back blows?",
     "For a conscious <b>infant</b> with an ineffective cough: <b>5 back blows, then 5 chest thrusts</b>, repeated. Abdominal thrusts are not used in infants.",
     "<b>B</b> &mdash; blind sweeps can push the object deeper. <b>C</b> &mdash; abdominal thrusts can injure an infant's abdominal organs; they are for children over 1 year. <b>D</b> &mdash; giving fluids to a choking infant risks aspiration.",
     "Infants: back blows and chest thrusts. Children: back blows and abdominal thrusts.",
     "section 2, ‘Choking’")]
)

# ------------------------------------------------------------------ UNIT 16
unit(16, "D", "Paediatric ARDS",
  "Paediatric acute respiratory distress syndrome is the end of many roads &mdash; pneumonia, sepsis, drowning, trauma. There is no drug that reverses it. What changes survival is protecting the lung from the ventilator while it heals.",
  [("e", "Recognise paediatric ARDS by the PALICC-2 criteria."),
   ("a", "Apply lung-protective ventilation: tidal volume, plateau and driving pressure limits, PEEP and oxygen targets."),
   ("a", "Explain permissive hypercapnia and its exceptions."),
   ("x", "Know the adjuncts with weak evidence and the limits of the guideline.")],
  [
   roles({"ug": "State what PARDS is and why the ventilator itself can injure the lung.",
          "nurse": "Monitor delivered volumes and pressures, oxygenation and fluid balance; report changes early.",
          "picu": "Track plateau and driving pressures, PEEP response and oxygenation index; recognise the need for escalation.",
          "pg": "Set and justify a lung-protective strategy, accept bounded trade-offs, and recognise the exceptions."}),
   sec(1, "Recognise it", '''
  <p>The Second Pediatric Acute Lung Injury Consensus Conference (<b>PALICC-2</b>, 2023) defines paediatric ARDS as:</p>
  <ul>
    <li>onset within <b>7 days</b> of a known clinical insult;</li>
    <li>new opacities on imaging consistent with lung-tissue disease;</li>
    <li>oedema not fully explained by heart failure or fluid overload;</li>
    <li>hypoxaemia graded by oxygenation index (OI) or oxygen saturation index (OSI) in ventilated children, or by P/F or S/F ratios on non-invasive support.</li>
  </ul>
  <p>PALICC-2 also introduced <b>&ldquo;possible PARDS&rdquo;</b> and <b>&ldquo;at risk for PARDS&rdquo;</b> categories and allows diagnosis where advanced imaging or gases are not available.</p>''' + algo("Oxygenation index", '''  OI  = (FiO2 × mean airway pressure × 100) ÷ PaO2
  OSI = (FiO2 × mean airway pressure × 100) ÷ SpO2
  (use OSI when SpO2 is 97% or below and no arterial gas is available)''')),

   sec(2, "Lung-protective ventilation", table(
     ["Variable", "PALICC-2 suggestion"],
     [["Tidal volume", "Physiological range, about 6&ndash;8 mL/kg (predicted or actual body weight, whichever is lower); below 6 if needed to respect pressure limits; caution below 4"],
      ["Plateau pressure", "At or below 28 cmH₂O (29&ndash;32 allowed with reduced chest-wall compliance)"],
      ["Driving pressure", "At or below 15 cmH₂O (measured under static conditions)"],
      ["PEEP", "Titrate to oxygenation and haemodynamics; avoid excessive PEEP"],
      ["SpO₂ target", "92&ndash;97% in mild/moderate PARDS; lower targets (about 88&ndash;92%) may be accepted in severe PARDS after PEEP optimisation, with monitoring of oxygen delivery"],
      ["CO₂", "Permissive hypercapnia accepted to maintain protection, with pH at or above about 7.20"]]) + danger('''<p><b>Exceptions to permissive hypercapnia:</b> raised intracranial pressure, severe pulmonary hypertension, selected congenital heart disease, haemodynamic instability and significant ventricular dysfunction. In these children, CO₂ targets must be individualised.</p>''')),

   sec(3, "Adjuncts and fluids", '''
  <ul>
    <li><b>Fluid:</b> avoid positive fluid balance once resuscitation is complete &mdash; fluid overload is associated with worse outcomes.</li>
    <li><b>Prone positioning:</b> not recommended routinely by PALICC-2; may be considered in severe PARDS.</li>
    <li><b>Neuromuscular blockade, inhaled nitric oxide, high-frequency oscillation, surfactant, steroids:</b> not routine; specific indications or insufficient evidence.</li>
    <li><b>ECMO:</b> for selected children with severe, refractory PARDS where the cause is reversible, in experienced centres.</li>
  </ul>''' + evidence('''<p>Emeriaud G, et al. <i>Executive Summary of the Second International Guidelines for the Diagnosis and Management of Pediatric Acute Respiratory Distress Syndrome (PALICC-2).</i> Pediatr Crit Care Med 2023;24(2):143&ndash;168. Much of it rests on low-certainty evidence and expert consensus: read it as a set of guard-rails, not a recipe.</p>'''), tier="good", lvl="x"),

   sec(4, "Across settings", tracks(
     ["PICU with arterial blood gases, lung mechanics and ECMO referral pathways"],
     ["Many children meeting &ldquo;possible&rdquo; or &ldquo;at risk&rdquo; PARDS criteria are first seen on non-invasive support in district hospitals: recognise them early and refer",
      "S/F ratio and OSI allow severity grading from a pulse oximeter when gases are unavailable",
      "If ventilating before transfer, set a protective tidal volume from the child's weight rather than squeezing to &ldquo;normal&rdquo; CO₂"]), lvl="a"),
  ],
  [Q("A 5-year-old (18 kg) with pneumonia-related PARDS is ventilated with a tidal volume of 180 mL. The plateau pressure is 34 cmH₂O and PaCO₂ 58 mmHg with pH 7.29. The resident suggests increasing tidal volume to 250 mL to normalise the CO₂. What is the most appropriate response?",
     ["Increase the tidal volume to normalise CO₂.",
      "Keep protective volumes and aim to bring the plateau pressure down to 28 or below; accept the CO₂ because pH is above 7.20, provided there is no contraindication.",
      "Increase the rate to 60/min to clear the CO₂ regardless of pressures.",
      "Stop PEEP to reduce plateau pressure."],
     1,
     "Which is more harmful to this lung: a high CO₂ with pH 7.29, or a plateau pressure of 34?",
     "The tidal volume is already 10 mL/kg and the plateau is above the limit. What does PALICC-2 say about CO₂ when pH is above about 7.20?",
     "The plateau (34) is <b>above</b> the PALICC-2 limit and 180 mL is already 10 mL/kg. Protect the lung: reduce toward 6&ndash;8 mL/kg and aim to bring the plateau to 28 or below. The CO₂ is acceptable (<b>permissive hypercapnia</b>, pH 7.29) unless a contraindication exists.",
     "<b>A</b> &mdash; a larger volume would raise the plateau further and worsen lung injury. <b>C</b> &mdash; a very fast rate risks air trapping and does not address the pressure limit. <b>D</b> &mdash; removing PEEP causes alveolar collapse and hypoxaemia.",
     "In PARDS, treat the lung gently; a normal blood gas bought with a high pressure is a bad bargain.",
     "section 2, ‘Lung-protective ventilation’", critical=True),
   Q("For which ventilated child with PARDS should permissive hypercapnia be avoided or individualised?",
     ["A 3-year-old with PARDS after pneumonia and no other conditions.",
      "A 7-year-old with PARDS and a traumatic brain injury with raised intracranial pressure.",
      "A 1-year-old with PARDS after aspiration.",
      "A 10-year-old with PARDS after sepsis, now haemodynamically stable."],
     1,
     "What does CO₂ do to blood flow in the brain?",
     "Rising CO₂ dilates cerebral vessels and raises intracranial pressure. Which child cannot afford that?",
     "Raised CO₂ increases cerebral blood flow and <b>intracranial pressure</b>. In a child with traumatic brain injury and raised ICP, permissive hypercapnia is an exception: CO₂ must be controlled.",
     "<b>A</b>, <b>C</b> and <b>D</b> &mdash; none has a listed exception (raised ICP, severe pulmonary hypertension, selected heart disease, haemodynamic instability or significant ventricular dysfunction).",
     "Every lung-protective rule has exceptions. Know them before you apply the rule.",
     "section 2, ‘Lung-protective ventilation’")]
)
