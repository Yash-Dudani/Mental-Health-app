import re
from database import Database

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.db = Database()

    def is_valid_email(self):
        """Check if email is in correct format"""
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, self.email) is not None

    def email_exists(self):
        """Check if email already exists in database"""
        query = "SELECT id FROM users WHERE email = %s"
        result = self.db.execute(query, (self.email,), fetch=True)
        return len(result) > 0  

    def save(self):
        """Save user to database with validations"""
        if not self.is_valid_email():
            print("❌ Invalid email format. Please enter a valid email address.")
            return "invalid_email"
        
        if self.email_exists():
            print("❌ Email already registered. Try a different one.")
            return "email_exists"

        query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s) RETURNING id"
        result = self.db.execute(query, (self.name, self.email, self.password), fetch=True)
        if result:
            self.id = result[0][0]
            print("✅ Registration successful!")
            return "success"
        return "error"

    @classmethod
    def login(cls, email, password):
        """Authenticate user and return user data if successful"""
        db = Database()
        query = "SELECT id, name FROM users WHERE email = %s AND password = %s"
        result = db.execute(query, (email, password), fetch=True)
        db.close()
        return result[0] if result else None

    def delete_account(self, user_id):
        """Delete user account and all associated data"""
        queries = [
            "DELETE FROM test_results WHERE user_id = %s",
            "DELETE FROM users WHERE id = %s"
        ]
        for query in queries:
            self.db.execute(query, (user_id,))
        self.db.close()
        print("✅ Account deleted successfully!")