from backend.database.database import Database


class AuthController:

    def __init__(self):

        self.db = Database()

        if not self.db.connect():

            raise Exception(
                "Could not connect to database."
            )

        self.logged_in = False
        self.current_user = None

    # ==========================================
    # LOGIN
    # ==========================================

    def login(
        self,
        username,
        password
    ):

        query = """
        SELECT *
        FROM users

        WHERE username = %s
        AND password = %s
        """

        user = self.db.fetch_one(
            query,
            (username, password)
        )

        if user:

            self.logged_in = True

            self.current_user = user

            print()
            print("========================================")
            print(" LOGIN SUCCESSFUL")
            print("========================================")

            print(
                "Welcome,",
                username
            )

            return True

        print()
        print("Invalid username or password.")

        return False

    # ==========================================
    # LOGOUT
    # ==========================================

    def logout(self):

        if self.logged_in:

            username = self.current_user[
                "username"
            ]

            self.logged_in = False

            self.current_user = None

            print()
            print("========================================")
            print(" LOGOUT SUCCESSFUL")
            print("========================================")

            print(
                "Goodbye,",
                username
            )

            return True

        print(
            "No user is currently logged in."
        )

        return False

    # ==========================================
    # CHECK LOGIN
    # ==========================================

    def is_logged_in(self):

        return self.logged_in

    # ==========================================
    # CLOSE
    # ==========================================

    def close(self):

        self.db.close()