from datetime import datetime

class Student:
    def __init__(self, student_id, name, marks, dob, fee_paid, total_fee=10000):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.dob = dob
        self.fee_paid = fee_paid
        self.total_fee = total_fee

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def calculate_cgpa(self):
        return round(self.calculate_average() / 10, 2)

    def calculate_age(self):
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

    def calculate_fee_balance(self):
        return self.total_fee - self.fee_paid

    def display_student_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average Marks: {self.calculate_average():.2f}")
        print(f"CGPA: {self.calculate_cgpa()}")
        print(f"Age: {self.calculate_age()}")
        print(f"Fee Paid: {self.fee_paid}")
        print(f"Fee Balance: {self.calculate_fee_balance()}")
        print("-" * 40)

class College:
    def __init__(self, college_code, college_name, location):
        self.college_code = college_code
        self.college_name = college_name
        self.location = location
        self.students = []

    def register_student(self, student):
        self.students.append(student)

    def display_college_details(self):
        print(f"College Code: {self.college_code}")
        print(f"College Name: {self.college_name}")
        print(f"Location: {self.location}")
        print("=" * 40)

    def display_all_students(self):
        for student in self.students:
            student.display_student_details()

college = College("ANIL", "ANITS", "Vizag")

s1 = Student("S001", "Geetha", [85, 90, 78], "2002-05-12", 8000)
s2 = Student("S002", "Ayesha", [75, 88, 92], "2001-08-23", 9500)
s3 = Student("S003", "Surya", [65, 70, 80], "2003-01-15", 7000)

college.register_student(s1)
college.register_student(s2)
college.register_student(s3)

college.display_college_details()
college.display_all_students()