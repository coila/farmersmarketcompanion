import psycopg2

class DB:

    def __init__(self):
        self.connection = psycopg2.connect("dbname=farmerbrown user=emma")
        self.cursor = self.connection.cursor()

    def query(self, q):
        cursor = self.cursor
        cursor.execute(q)
        self.connection.commit()

        if cursor:
            try:
                return cursor.fetchall()
            except:
                return []

    def __del__(self):
        self.connection.close()

