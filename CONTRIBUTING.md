# Contributing to the Adaptive Learning Framework (ALF)

Thank you for your interest in contributing to ALF!  
This project aims to build an open, modular, and transparent adaptive learning ecosystem for STEM education.

We welcome contributions of all kinds — from bug fixes and new features to documentation, translations, and new problem modules.

---

## 🧱 Project Philosophy

ALF is built on four core principles:

1. **Modularity** — Engine, UI, and content remain cleanly separated.
2. **Transparency** — All logic is explicit, inspectable, and reproducible.
3. **Scalability** — JSON-based problem modules allow unlimited expansion.
4. **Accessibility** — Bilingual UI and open-source design.

---

## 🛠️ How to Contribute

### 1. Fork the Repository
Click the **Fork** button on GitHub and clone your fork locally:

git clone https://github.com/palman22-hue/AdaptiveLearningFramework


### 2. Create a Feature Branch

git checkout -b feature/my-new-feature


### 3. Make Your Changes
Follow the project structure:

engine.py           # Core engine + learner state machine
alf_app.py         # Streamlit UI
problems/          # JSON problem modules
FotoDocs/          # Visual evolution of the project


### 4. Add or Update JSON Problem Modules
Each module must follow the standard schema:

```json
{
  "topic": "Topic Name",
  "question": "...",
  "correct_answer": "...",
  "common_errors": [
    {
      "pattern": "keyword",
      "description": "...",
      "drill_prompt": "..."
    }
  ],
  "integration_test": {
    "prompt": "..."
  }
}

5. Run the App Locally

streamlit run alf_app.py

6. Commit Your Changes

git commit -m "Add new topic: Momentum"

7. Push and Open a Pull Request

git push origin feature/my-new-feature

Then open a PR on GitHub.

🧪 Coding Standards

Use clear, readable Python.

Keep engine logic in engine.py.

Keep UI logic in alf_app.py.

Avoid duplicating logic across modules.

Ensure JSON files are valid and UTF‑8 encoded.

Test all topics in both English and Dutch UI modes.

🧩 Adding New Topics

To add a new topic:

Create a new JSON file in problems/

Follow the standard schema

Include:

A clear question

At least one error pattern

A meaningful drill prompt

An integration test

Test the topic in the UI

🖼️ Adding Evolution Photos

Place images in:

FotoDocs/

These help document the growth of the project and are encouraged.

🐛 Reporting Issues

If you find a bug:

Open an issue on GitHub

Include steps to reproduce

Include screenshots if relevant

Mention your environment (local, Codespaces, OS)

❤️ Code of Conduct

Be respectful, constructive, and collaborative.
We build this framework together.

Thank you for helping make ALF better!