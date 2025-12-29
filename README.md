📘 Adaptive Learning Framework (ALF)

[![DOI](https://zenodo.org/badge/1121764509.svg)](https://doi.org/10.5281/zenodo.18035787)

A modular, bilingual, open‑source engine for adaptive STEM education.

🚀 Overview
The Adaptive Learning Framework (ALF) is a lightweight, extensible system designed to diagnose student misconceptions, generate targeted drills, and verify understanding through integration tests. It is fully modular, JSON‑driven, and built for both research and practical classroom use.

ALF now includes:

🧠 A state‑machine Adaptive Learner

⚙️ A clean, modular engine (engine.py)

🎛️ A bilingual Streamlit UI (alf_app.py)

📚 A scalable JSON problem bank

🌍 Full English + Dutch interface support

🔄 Automatic topic loading and learner initialization

🖼️ A visual evolution timeline (see /FotoDocs)

✨ Features
🔍 Phase 1 — Diagnosis
ALF analyzes student input and detects error patterns defined in each JSON module.

🎯 Phase 2 — Drill
Based on the detected misconception, ALF generates a targeted drill prompt.

🧩 Phase 3 — Integration Test
After a correct drill response, ALF presents an integration test to confirm mastery.

📁 JSON‑Driven Problem Bank
Each topic is defined as a standalone JSON file, making the system easy to extend.

🌐 Bilingual UI
The interface supports English and Dutch, selectable via the sidebar.

🧱 Modular Architecture
Engine, learner, UI, and content are cleanly separated for clarity and scalability.

📂 Project Structure

AdaptiveLearningFramework/
│
├── alf_app.py               # Streamlit UI (bilingual)
├── engine.py                # Adaptive engine + learner state machine
├── alf_cli.py               # Optional CLI interface
│
├── problems/                # JSON problem modules
│   ├── kinetic_energy.json
│   ├── chemistry_moles.json
│   └── ...
│
├── FotoDocs/                # Evolution photos of the framework
│
├── README.md                # Documentation
└── LICENSE

🧪 Example JSON Module

{
  "topic": "Chemistry — Moles",
  "question": "Calculate the number of moles in 18 grams of water (H₂O).",
  "correct_answer": "1 mol",

  "common_errors": [
    {
      "pattern": "wrong_formula",
      "description": "The student used an incorrect molar mass formula.",
      "drill_prompt": "Write the correct molar mass formula for H₂O and calculate it step by step."
    }
  ],

  "integration_test": {
    "prompt": "How many moles are in 44 grams of CO₂?"
  }
}

🖥️ Running the App

Local Execution

pip install -r requirements.txt
streamlit run alf_app.py

🌍 Bilingual Interface
The UI automatically adapts based on the selected language:

English

Nederlands

This affects UI labels, not the content of the JSON modules, keeping the problem bank language‑agnostic.

📸 Evolution of the Framework
The /FotoDocs folder contains images documenting the growth of ALF from early prototypes to the current modular architecture.

These images illustrate:

the initial concept

the first working adaptive loop

the final bilingual, modular system

This visual history is part of ALF’s identity and open‑source transparency.

🤝 Contributing
Contributions are welcome!

You can help by:

adding new JSON problem modules

improving the engine

extending the UI

adding new languages

refining documentation

📜 License

This project is licensed under the GPL‑3.0 License.