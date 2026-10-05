from backend.system.student_platform import StudentPlatform
from frontend.menu import Menu
import os 


def main():

    try:

        platform = StudentPlatform()

        while True:

            # =====================================
            # LOGIN MENU
            # =====================================

            if not platform.auth.is_logged_in():

                Menu.show_login_menu()

                choice = input(
                    "Choose an option: "
                ).strip()

                if choice == "1":

                    platform.login()

                elif choice == "2":

                    print()
                    print(
                        "Thank you for using "
                        "Student Management System."
                    )

                    platform.close()

                    break

                else:

                    print(
                        "Invalid option."
                    )

            # =====================================
            # MAIN SYSTEM
            # =====================================

            else:

                Menu.show_main_menu()

                choice = input(
                    "Choose an option: "
                ).strip()

                if choice == "1":

                    platform.register_student()

                elif choice == "2":

                    platform.display_students()

                elif choice == "3":

                    platform.search_student()

                elif choice == "4":

                    platform.update_student()

                elif choice == "5":

                    platform.delete_student()

                elif choice == "6":

                    platform.logout()

                else:

                    print(
                        "Invalid option."
                    )

    except Exception as error:

        print()
        print(
            "System error:",
            error
        )


# =============================================
# START PROGRAM
# =============================================

if __name__ == "__main__":

    main()
    