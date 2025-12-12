AdaptiveLearner – ALF‑Inspired Mini Tutor
AdaptiveLearner is a conceptual Python class that implements a simple three‑phase learning loop inspired by adaptive learning frameworks:

Phase 1 – Diagnose & Isolate

Phase 2 – Hypothesize & Adapt (Drill)

Phase 3 – Validate & Integrate

The example focuses on the kinetic energy formula, but the pattern is general.

Features
Tracks a topic and a history of all interactions.

Phase 1: Analyses a student’s answer and labels the error type (e.g. operator / exponent vs. conceptual confusion).

Phase 2: Uses the error type plus a student‑given hypothesis to generate a targeted drill.

Phase 3: Uses the drill result to decide whether to move on to a more complex “integration” problem or loop back for another drill.

Includes a small CLI loop so the class can be used as a text‑based tutor.

Code overview
Class initialization
python
learner = AdaptiveLearner("Kinetic Energy Formula")
topic: string describing what is being learned.

history: list that stores per‑phase records of inputs, reports, drills, and results.

Phase 1 – Diagnose & isolate
python
report = learner.phase1_diagnose_isolate(question, student_input)
question: the reference question or formula (e.g. E_k = 1/2 * m * v^2).

student_input: the learner’s attempt.

Returns a dict like:

python
{
    "error_type": "Incorrect Operator & Missing Exponent",
    "details": "...",
    "correct_answer": "125 J"
}
Detection is rule‑based and simplified: it checks for misuse of + versus * and missing squaring of velocity.

Phase 2 – Hypothesize & adapt
python
drill = learner.phase2_hypothesize_adapt(error_report, student_hypothesis)
error_report: the dict from Phase 1.

student_hypothesis: a free‑text reflection from the student.

Chooses between an operator/order‑of‑operations drill and a conceptual formula drill based on error_type.

Returns a drill dict:

python
{
    "id": "drill_operator_1",
    "type": "order_of_operations",
    "prompt": "Compute 5 + 3 * 2 and (5 + 3) * 2. Explain why they differ."
}
Phase 3 – Validate & integrate
python
final_test = learner.phase3_validate_integrate(drill_result)
drill_result: for now a dict like {"is_correct": True, "result": "125"}.

If is_correct is True, generates an integration problem:

python
{
    "id": "final_ke_change_1",
    "type": "integration_problem",
    "prompt": (
        "A 5 kg object moves at 20 m/s and accelerates to 30 m/s.\n"
        "What is the change in kinetic energy?"
    ),
}
If is_correct is False, Phase 3 records failure and signals that a new drill is needed.

CLI usage example
At the bottom of the file you can run the tutor as a simple command‑line loop:

python
if __name__ == "__main__":
    learner = AdaptiveLearner("Kinetic Energy Formula")

    while True:
        print("\n--- NEW CYCLE (type 'quit' to stop) ---")
        student_answer = input("Your answer to E_k = 1/2 * m * v^2: ")

        if student_answer.lower().strip() in {"quit", "exit"}:
            print("Exiting tutor. Goodbye.")
            break

        report = learner.phase1_diagnose_isolate(
            "E_k = 1/2 * m * v^2",
            student_answer
        )

        hypothesis = input("Why do you think this was wrong? ")
        drill = learner.phase2_hypothesize_adapt(report, hypothesis)
        print(f"\nDRILL:\n{drill['prompt']}")

        drill_input = input("\nDid you solve this drill correctly? (y/n): ")
        drill_result = {"is_correct": drill_input.lower().startswith("y")}
        final_test = learner.phase3_validate_integrate(drill_result)

        if final_test:
            print("\nFINAL TEST:")
            print(final_test["prompt"])
Run:

bash
python adaptive_learner.py
and interact via the terminal.

Extending the prototype
Some ideas for next steps:

Add more sophisticated _analyze_error rules for different misconception types.

Store student reflections and timestamps in history for later analysis.

Generalize drills and final tests to handle multiple topics, not just kinetic energy.