# Architecture Overview  
Adaptive Learning Framework (ALF)

This document describes the internal architecture of ALF.  
It is not a roadmap or a fixed blueprint — ALF evolves organically through new insights, experiments, and iterative refinement.

The goal of this document is to make the system transparent, understandable, and extensible for anyone who wishes to explore or contribute.

---

## 1. Design Philosophy

ALF is built on three core principles:

### **1. Modularity**
Engine, learner, UI, and content are strictly separated.  
This ensures clarity, testability, and long-term maintainability.

### **2. Transparency**
All logic is explicit and inspectable.  
No hidden heuristics, no black boxes — every decision is traceable.

### **3. Organic Growth**
ALF does not follow a rigid roadmap.  
It evolves through experimentation, reflection, and new insights.  
This mirrors real learning and real system development.

---

## 2. High-Level Architecture

+---------------------------+
|        Streamlit UI       |
|       (alf_app.py)        |
+-------------+-------------+
|
v
+---------------------------+
|   Adaptive Learning Engine |
|         (engine.py)        |
+-------------+-------------+
|
v
+---------------------------+
|     Adaptive Learner       |
|   (state machine object)   |
+-------------+-------------+
|
v
+---------------------------+
|     JSON Problem Bank      |
|         (problems/)        |
+---------------------------+


---

## 3. Components

### **3.1 Streamlit UI (`alf_app.py`)**
- Handles language selection (English/Dutch)
- Loads topics dynamically from the `problems/` folder
- Initializes a new learner when the topic changes
- Sends user input to the engine
- Displays:
  - diagnosis results  
  - drill prompts  
  - integration tests  

The UI contains **no learning logic** — only presentation and flow.

---

### **3.2 Engine (`engine.py`)**
The engine orchestrates the adaptive learning cycle.

It contains:

#### **ProblemBank**
- Loads all JSON modules at startup  
- Provides topic lookup  
- Ensures content is decoupled from logic  

#### **AdaptiveLearner**
A state machine with three phases:

1. **Diagnosis**  
   Detects error patterns in student input.

2. **Drill**  
   Generates targeted practice based on the detected misconception.

3. **Integration**  
   Confirms mastery with a final test.

The learner stores:
- topic  
- problem data  
- history  
- current phase  
- last detected error  

#### **AdaptiveLearningFramework**
A thin orchestration layer that:
- initializes learners  
- routes answers to the correct learner phase  
- returns structured results to the UI  

---

## 4. JSON Problem Modules

Each topic is defined in a standalone JSON file:

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

This structure ensures:

content is language-agnostic

topics can be added without modifying the engine

educators can contribute without touching code

5. Evolution Documentation (FotoDocs/)

This folder contains images documenting the growth of ALF.

These images serve several purposes:

They show the authentic evolution of the system

They help educators and policymakers understand the project’s trajectory

They demonstrate that ALF is not theoretical — it is built, tested, refined

They provide transparency and trust

This visual history is part of ALF’s identity.

6. Why This Architecture Works

It is simple enough to understand at a glance

It is modular enough to extend indefinitely

It is transparent enough for educators and researchers

It is flexible enough to grow organically

ALF is not a static product — it is a living framework.

7. Future Evolution (Not a Roadmap)

ALF will continue to evolve through:

new insights

new topics

new pedagogical ideas

new experiments

community contributions

The architecture supports this natural growth without imposing constraints.

8. Contributing

See CONTRIBUTING.md for guidelines on adding new topics or improving the system.
