class RestRecommender:

    @staticmethod
    def suggest(features):
        suggestions = []

        if features["overlap_count"] > 0:
            suggestions.append("Avoid overlapping shifts")

        if features["total_hours"] > 40:
            suggestions.append("Reduce weekly working hours")

        if features["avg_gap"] < 1:
            suggestions.append("Increase rest gaps between shifts")

        if not suggestions:
            suggestions.append("Your schedule looks balanced")

        return suggestions