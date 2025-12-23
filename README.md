Adaptive Learning Framework (ALF)

A modular, open‑source engine for adaptive STEM education.

🚀 Overview

The Adaptive Learning Framework (ALF) is a lightweight, modular system designed to diagnose student misconceptions, generate targeted drills, and verify understanding through integration tests. It is fully open‑source, easy to extend, and built for both research and practical classroom use.

ALF currently supports:

🧠 A modular adaptive learning engine

🎛️ A Streamlit‑based user interface

📚 A JSON‑driven problem bank

🔄 Multi‑topic support via a topic selector

🌐 Local execution and GitHub Codespaces compatibility

✨ Features

🔍 Diagnostic Engine

ALF analyzes student answers and identifies common error patterns defined in each JSON module.

🎯 Targeted Drills

Based on the detected misconception, ALF generates a focused drill question to reinforce understanding.

🧩 Integration Test

After a correct drill response, ALF presents an integration test to confirm mastery.

📚 JSON Problem Bank

Each topic is defined as a standalone JSON file, making it easy to add or modify content.

🌍 Multi‑Language Support

ALF supports both English and Dutch, with more languages planned.

📁 Project Structure

ALFFramework/
│
├── alf_app.py          # Streamlit UI
├── ALFFramework.py     # Adaptive learning engine
├── alf_cli.py          # Command-line interface
│
├── problems/           # JSON problem modules
│   ├── algebra_linear.json
│   ├── calculus_derivatives.json
│   └── physics_newton2.json
│
└── README.md           # Documentation

🧪 Example JSON Module

{
  "topic": "Calculus — Derivatives",
  "question": "Compute the derivative of f(x) = 3x^2 + 4x - 5",
  "correct_answer": "f'(x) = 6x + 4",

  "common_errors": [
    {
      "pattern": "power_rule_mistake",
      "description": "Incorrect application of the power rule.",
      "drill_prompt": "Apply the power rule to g(x) = 5x^3."
    }
  ],

  "integration_test": {
    "prompt": "Compute the derivative of f(x) = x^3 - 2x + 1"
  }
}

🏁 Getting Started

Run locally

pip install -r requirements.txt
streamlit run alf_app.py


Run in GitHub Codespaces
Just open the repo in Codespaces — everything is preconfigured.

🤝 Contributing
Contributions are welcome!
You can add new JSON modules, improve the engine, or extend the UI.

📜 License
This project is licensed under the GPL‑3.0 License.



