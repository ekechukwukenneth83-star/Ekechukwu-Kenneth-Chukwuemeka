class Student:

    def __init__(
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

        self.matric_number = matric_number
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.department = department
        self.level = level
        self.email = email
        self.phone = phone
        self.address = address

    def display(self):

        print("----------------------------------------")
        print("STUDENT INFORMATION")
        print("----------------------------------------")

        print("Matric Number :", self.matric_number)
        print("Name          :", self.first_name, self.last_name)
        print("Gender        :", self.gender)
        print("Date of Birth :", self.date_of_birth)
        print("Department    :", self.department)
        print("Level         :", self.level)
        print("Email         :", self.email)
        print("Phone         :", self.phone)
        print("Address       :", self.address)

        print("----------------------------------------")