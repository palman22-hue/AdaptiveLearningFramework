class GamifiedLearner:
    """GEAR Framework: Focuses on encouraging, relatable, and fun feedback."""

    def phase1_spot_the_glitch(self, question, student_input):
        analysis_report = self._analyze_error_friendly(question, student_input)
        
        print("\n🚀 **Spot the Glitch!**")
        print(f"**Oopsie Finder Report:** {analysis_report['friendly_error']}")
        # Instead of just variables, use analogies
        print("💡 **Think of it like cooking:** You added sugar when the recipe said salt!")
        return analysis_report

    def phase2_level_up(self, error_report):
        explanation = self._get_relatable_explanation(error_report)
        drill_problem = self._create_drill_relatable(error_report)
        
        print("\n💪 **Time to Level Up!**")
        print(f"**Why it matters:** {explanation}")
        print(f"**Challenge:** {drill_problem}")
        return drill_problem

    # ... and so on for Phase 3 (Final Boss Test)