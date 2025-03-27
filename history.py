from database import Database

class History:
    def __init__(self, user_id):
        self.user_id = user_id
        self.db = Database()

    def show_history(self):
        query = "SELECT score, category, created_at FROM test_results WHERE user_id = %s ORDER BY created_at DESC"
        results = self.db.execute(query, (self.user_id,), fetch=True)

        if results:
            print("\nYour Test History:")
            for row in results:
                print(f"Score: {row[0]}, Category: {row[1]}, Date: {row[2]}")
        else:
            print("\nNo test history found.")
