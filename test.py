from database import Database

class MentalHealthTest:
    questions = [
        {"text": "How often do you feel stressed?", "scale": "1 (Never) - 5 (Always)"},
        {"text": "Do you find it hard to focus?", "scale": "1 (Never) - 5 (Always)"},
        {"text": "How well do you sleep?", "scale": "1 (Poor) - 5 (Excellent)"},
        {"text": "Do you experience mood swings frequently?", "scale": "1 (Never) - 5 (Always)"},
        {"text": "Do you feel socially withdrawn?", "scale": "1 (Never) - 5 (Always)"}
    ]

    def __init__(self, user_id):
        self.user_id = user_id
        self.total_score = 0
        self.db = Database()

    def conduct_test(self):
        for q in self.questions:
            print(f"\n{q['text']} ({q['scale']})")
            while True:
                try:
                    response = int(input("Your response (1-5): "))
                    if 1 <= response <= 5:
                        break
                    else:
                        print("❌ Please enter a number between 1 and 5.")
                except ValueError:
                    print("❌ Invalid input! Enter a number between 1 and 5.")

            self.total_score += response

        self.save_result()

    def save_result(self):
        category, solution = self.classify_score()
        query = "INSERT INTO test_results (user_id, score, category) VALUES (%s, %s, %s)"
        self.db.execute(query, (self.user_id, self.total_score, category))
        print(f"\n🧠 Your Mental Health Category: {category}")

        if solution:
            print("\n💡 Suggested Solutions:")
            for tip in solution:
                print(f"- {tip}")

    def classify_score(self):
        if self.total_score <= 7:
            return "Good Mental Health", None
        elif self.total_score <= 15:
            return "Moderate Stress", [
                "Try meditation or deep breathing exercises.",
                "Engage in regular physical activity.",
                "Maintain a healthy sleep schedule.",
                "Talk to a friend or a therapist."
            ]
        else:
            return "High Stress", [
                "Consider seeking professional help.",
                "Practice mindfulness and relaxation techniques.",
                "Ensure a balanced diet and proper hydration.",
                "Limit screen time and social media consumption.",
                "Engage in hobbies or activities you enjoy."
            ]