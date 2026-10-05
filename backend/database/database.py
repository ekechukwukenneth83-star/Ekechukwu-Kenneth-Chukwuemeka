import mysql.connector
from mysql.connector import Error


class Database:

    def __init__(self):

        self.connection = None
        self.cursor = None


    # ==========================================
    # CONNECT
    # ==========================================

    def connect(self):

        try:

            self.connection = mysql.connector.connect(

                host="localhost",

                user="root",

                password="kennethe83",

                database="student_platform"

            )

            if self.connection.is_connected():

                self.cursor = self.connection.cursor(
                    dictionary=True
                )

                print("Database connected successfully.")

                return True

        except Error as error:

            print("Database connection error:", error)

            return False


    # ==========================================
    # EXECUTE QUERY
    # ==========================================

    def execute_query(self, query, values=None):

        try:

            self.cursor.execute(query, values)

            self.connection.commit()

            return True

        except Error as error:

            print("Database error:", error)

            self.connection.rollback()

            return False


    # ==========================================
    # FETCH ALL
    # ==========================================

    def fetch_all(self, query, values=None):

        try:

            self.cursor.execute(query, values)

            return self.cursor.fetchall()

        except Error as error:

            print("Database error:", error)

            return []


    # ==========================================
    # FETCH ONE
    # ==========================================

    def fetch_one(self, query, values=None):

        try:

            self.cursor.execute(query, values)

            return self.cursor.fetchone()

        except Error as error:

            print("Database error:", error)

            return None


    # ==========================================
    # CLOSE
    # ==========================================

    def close(self):

        if self.cursor:

            self.cursor.close()

        if self.connection and self.connection.is_connected():

            self.connection.close()