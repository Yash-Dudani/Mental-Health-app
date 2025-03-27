import psycopg2

class Database:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                database="mental_health_db",
                user="postgres",
                password="root",
                host="localhost",
                port="5432"
            )
            self.cur = self.conn.cursor()
        except psycopg2.Error as e:
            print(f"❌ Database connection failed: {e}")

    def execute(self, query, params=None, fetch=False):
        try:
            self.cur.execute(query, params or ())
            self.conn.commit()
            return self.cur.fetchall() if fetch else None
        except psycopg2.IntegrityError as e:
            self.conn.rollback()
            return "integrity_error"  
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"❌ Database error: {e}")
            return None

    def close(self):
        self.cur.close()
        self.conn.close()