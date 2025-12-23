🎓Adaptive Learning Framework (ALF) — Versie 2
    
   - Diagnose → Hypothese → Drill → Integratie
    
   - Een open, modulair en uitbreidbaar leerframework voor STEM‑onderwijs

---

🚀Over dit project

   - Het Adaptive Learning Framework (ALF) is een modulair systeem dat automatisch:

   - fouten van studenten diagnosticeert

   - hypothesen over misconcepties vormt

   - gerichte drills genereert

   - en een integratie‑test aanbiedt om begrip te bevestigen

  Deze versie (v2) introduceert:

   - een Streamlit‑interface

   - een JSON‑gebaseerde probleembank

   - volledige GitHub Codespaces‑compatibiliteit

   - een opgeschoonde, schaalbare projectstructuur

   - ALF is ontworpen om transparant, reproduceerbaar en uitbreidbaar te zijn —    ideaal voor onderzoek, onderwijs en open‑source samenwerking.

---

📁 Projectstructuur

ALFFramework/
├── ALFFramework.py        # De ALF-engine (diagnose, drill, validatie)
├── alf_app.py             # Streamlit UI
├── problems/              # JSON-probleembank
│   └── kinetic_energy.json
└── README.md

---

🧭 Installatie in GitHub Codespaces

1. Open de repository in Codespaces

   - Ga naar de GitHub‑pagina van dit project

   - Klik op Code

   - Kies Codespaces → Create codespace on main

   - Wacht tot de omgeving volledig geladen is

2. Installeer de benodigde packages

   - Open de terminal in Codespaces en voer uit:

   - pip install streamlit

(Andere dependencies worden automatisch opgepakt door Python.)

3. Start de Streamlit‑app

   - In de terminal:

   - streamlit run alf_app.py

   - Codespaces opent automatisch een browser‑preview met de werkende ALF‑interface.

---

🧪 Hoe ALF werkt

Fase 1 — Diagnose (🔍)
    
   - ALF analyseert het student‑antwoord en matcht het met foutpatronen uit de JSON‑module.

Fase 2 — Hypothese & Drill (🧩)
    
   - ALF genereert een gerichte drill gebaseerd op het fouttype.

Fase 3 — Validatie & Integratie (🚀)
    
   - Bij een correcte drill volgt een integratie‑test om begrip te bevestigen.

---

📚 JSON‑Probleembank
Alle STEM‑problemen worden opgeslagen in problems/ als JSON‑modules.

Voorbeeld:

{
  "topic": "Kinetic Energy",
  "question": "E_k = 1/2 * m * v^2",
  "correct_answer": "125 J",

  "common_errors": [
    {
      "pattern": "missing_exponent",
      "description": "Student vergeet v^2 toe te passen.",
      "drill_prompt": "Schrijf de formule voor kinetische energie en label elk symbool."
    }
  ],

  "integration_test": {
    "prompt": "Een object van 5 kg versnelt van 20 m/s naar 30 m/s. Wat is de verandering in kinetische energie?"
  }
}

Nieuwe onderwerpen toevoegen = simpelweg een nieuw JSON‑bestand toevoegen.

---

🧩 Onderwerpen uitbreiden

Voeg nieuwe bestanden toe in problems/, zoals:

   - algebra_linear.json

   - calculus_derivatives.json

   - physics_newton2.json

   - chemistry_moles.json

ALF laadt ze automatisch.

---

🌍 Waarom ALF bijzonder is

   - Volledig modulair

   - Open en transparant

   - Schaalbaar naar honderden STEM‑onderwerpen

   - Eenvoudig te integreren in andere systemen

   - Perfect voor onderzoek naar adaptief leren

---

🤝 Bijdragen

    Pull requests, uitbreidingen en nieuwe JSON‑modules zijn welkom.
    Samen bouwen we een open ecosysteem voor STEM‑onderwijs.

---    

🧠 Credits

    Ontwikkeld door Esteban Palman    
    Met een focus op modulariteit, transparantie en schaalbaarheid in STEM‑onderwijs.