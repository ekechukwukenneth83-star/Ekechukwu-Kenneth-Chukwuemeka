from backend.models.student import Student
from backend.controllers.student_controller import StudentController
from backend.controllers.auth_controller import AuthController


class StudentPlatform:

    def __init__(self):

        self.auth = AuthController()

        self.student_controller = StudentController()

    # ==========================================
    # LOGIN
    # ==========================================

    def login(self):

        print()
        print("========================================")
        print("      STUDENT MANAGEMENT SYSTEM")
        print("                 LOGIN")
        print("========================================")

        username = input(
            "Username: "
        ).strip()

        password = input(
            "Password: "
        ).strip()

        return self.auth.login(
            username,
            password
        )

    # ==========================================
    # REGISTER STUDENT
    # ==========================================

    def register_student(self):

        if not self.auth.is_logged_in():

            print(
                "Please login first."
            )

            return

        print()
        print("========================================")
        print("         STUDENT REGISTRATION")
        print("========================================")

        matric_number = input(
            "Matric Number: "
        ).strip()

        first_name = input(
            "First Name: "
        ).strip()

        last_name = input(
            "Last Name: "
        ).strip()

        gender = input(
            "Gender: "
        ).strip()

        date_of_birth = input(
            "Date of Birth (YYYY-MM-DD): "
        ).strip()

        department = input(
            "Department: "
        ).strip()

        while True:

            try:

                level = int(
                    input("Level: ")
                )

                break

            except ValueError:

                print(
                    "Level must be a number."
                )

        email = input(
            "Email: "
        ).strip()

        phone = input(
            "Phone: "
        ).strip()

        address = input(
            "Address: "
        ).strip()

        # Create Student object

        student = Student(
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

        # Save student to MySQL

        self.student_controller.register_student(
            student
        )

    # ==========================================
    # DISPLAY ALL STUDENTS
    # ==========================================

    def display_students(self):

        if not self.auth.is_logged_in():

            print(
                "Please login first."
            )

            return

        students = (
            self.student_controller
            .get_all_students()
        )

        print()
        print("========================================")
        print("           STUDENT RECORDS")
        print("========================================")

        if not students:

            print(
                "No student records found."
            )

            return

        for student in students:

            print("----------------------------------------")

            print(
                "Student ID:",
                student["student_id"]
            )

            print(
                "Matric Number:",
                student["matric_number"]
            )

            print(
                "Name:",
                student["first_name"],
                student["last_name"]
            )

            print(
                "Gender:",
                student["gender"]
            )

            print(
                "Date of Birth:",
                student["date_of_birth"]
            )

            print(
                "Department:",
                student["department"]
            )

            print(
                "Level:",
                student["level"]
            )

            print(
                "Email:",
                student["email"]
            )

            print(
                "Phone:",
                student["phone"]
            )

            print(
                "Address:",
                student["address"]
            )

            print(
                "Registered:",
                student["created_at"]
            )

        print("----------------------------------------")

    # ==========================================
    # SEARCH STUDENT
    # ==========================================

    def search_student(self):

        if not self.auth.is_logged_in():

            print(
                "Please login first."
            )

            return

        matric_number = input(
            "Enter matric number: "
        ).strip()

        student = (
            self.student_controller
            .get_student_by_matric(
                matric_number
            )
        )

        if student:

            print()
            print("========================================")
            print("             STUDENT FOUND")
            print("========================================")

            print(
                "Student ID:",
                student["student_id"]
            )

            print(
                "Matric Number:",
                student["matric_number"]
            )

            print(
                "Name:",
                student["first_name"],
                student["last_name"]
            )

            print(
                "Gender:",
                student["gender"]
            )

            print(
                "Date of Birth:",
                student["date_of_birth"]
            )

            print(
                "Department:",
                student["department"]
            )

            print(
                "Level:",
                student["level"]
            )

            print(
                "Email:",
                student["email"]
            )

            print(
                "Phone:",
                student["phone"]
            )

            print(
                "Address:",
                student["address"]
            )

        else:

            print(
                "Student not found."
            )

    # ==========================================
    # UPDATE STUDENT
    # ==========================================

    def update_student(self):

        if not self.auth.is_logged_in():

            print(
                "Please login first."
            )

            return

        matric_number = input(
            "Enter matric number to update: "
        ).strip()

        student = (
            self.student_controller
            .get_student_by_matric(
                matric_number
            )
        )

        if not student:

            print(
                "Student not found."
            )

            return

        print()
        print(
            "Enter the new information."
        )

        first_name = input(
            "First Name: "
        ).strip()

        last_name = input(
            "Last Name: "
        ).strip()

        gender = input(
            "Gender: "
        ).strip()

        date_of_birth = input(
            "Date of Birth (YYYY-MM-DD): "
        ).strip()

        department = input(
            "Department: "
        ).strip()

        while True:

            try:

                level = int(
                    input("Level: ")
                )

                break

            except ValueError:

                print(
                    "Level must be a number."
                )

        email = input(
            "Email: "
        ).strip()

        phone = input(
            "Phone: "
        ).strip()

        address = input(
            "Address: "
        ).strip()

        self.student_controller.update_student(
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

    # ==========================================
    # DELETE STUDENT
    # ==========================================

    def delete_student(self):

        if not self.auth.is_logged_in():

            print(
                "Please login first."
            )

            return

        matric_number = input(
            "Enter matric number to delete: "
        ).strip()

        student = (
            self.student_controller
            .get_student_by_matric(
                matric_number
            )
        )

        if not student:

            print(
                "Student not found."
            )

            return

        confirmation = input(
            "Delete this student? (yes/no): "
        ).lower()

        if confirmation == "yes":

            self.student_controller.delete_student(
                matric_number
            )

        else:

            print(
                "Delete operation cancelled."
            )

    # ==========================================
    # LOGOUT
    # ==========================================

    def logout(self):

        return self.auth.logout()

    # ==========================================
    # CLOSE SYSTEM
    # ==========================================

    def close(self):

        self.student_controller.close()

        self.auth.close()