from backend.database.database import Database


class StudentController:

    def __init__(self):

        self.db = Database()

        if not self.db.connect():

            raise Exception(
                "Could not connect to database."
            )

    # ==========================================
    # REGISTER STUDENT
    # ==========================================

    def register_student(self, student):

        query = """
        INSERT INTO students
        (
            matric_number,
            first_name,
            last_name,
            gender,
            date_of_birth,
            department,
            level,
            email,
            phone,
            address
        )
        VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            student.matric_number,
            student.first_name,
            student.last_name,
            student.gender,
            student.date_of_birth,
            student.department,
            student.level,
            student.email,
            student.phone,
            student.address
        )

        if self.db.execute_query(query, values):

            print()
            print("========================================")
            print(" STUDENT REGISTERED SUCCESSFULLY")
            print("========================================")

            print(
                "Matric Number:",
                student.matric_number
            )

            print(
                "Name:",
                student.first_name,
                student.last_name
            )

            return True

        return False

    # ==========================================
    # GET ALL STUDENTS
    # ==========================================

    def get_all_students(self):

        query = """
        SELECT *
        FROM students
        ORDER BY student_id DESC
        """

        return self.db.fetch_all(query)

    # ==========================================
    # SEARCH STUDENT
    # ==========================================

    def get_student_by_matric(
        self,
        matric_number
    ):

        query = """
        SELECT *
        FROM students
        WHERE matric_number = %s
        """

        return self.db.fetch_one(
            query,
            (matric_number,)
        )

    # ==========================================
    # UPDATE STUDENT
    # ==========================================

    def update_student(
        self,
        matric_number,
        first_name,
        last_name,
        gender,
        date_of_birth,
        department,
        level,
        email,
        phone,
        address
    ):

        query = """
        UPDATE students

        SET
            first_name = %s,
            last_name = %s,
            gender = %s,
            date_of_birth = %s,
            department = %s,
            level = %s,
            email = %s,
            phone = %s,
            address = %s

        WHERE matric_number = %s
        """

        values = (
            first_name,
            last_name,
            gender,
            date_of_birth,
            department,
            level,
            email,
            phone,
            address,
            matric_number
        )

        if self.db.execute_query(
            query,
            values
        ):

            print(
                "Student record updated successfully."
            )

            return True

        return False

    # ==========================================
    # DELETE STUDENT
    # ==========================================

    def delete_student(
        self,
        matric_number
    ):

        query = """
        DELETE FROM students
        WHERE matric_number = %s
        """

        if self.db.execute_query(
            query,
            (matric_number,)
        ):

            print(
                "Student deleted successfully."
            )

            return True

        return False

    # ==========================================
    # CLOSE DATABASE
    # ==========================================

    def close(self):

        self.db.close()