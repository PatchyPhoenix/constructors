class student:
    def __init__(self):
        self.student_name = input("\nEnter the student's name: ")
        self.student_age = input("Enter the student's age: ")
        self.student_gender = input("Enter the student's gender: ")
    def display(self):
        print(f"Enter the student's name : {self.student_name}: ")
        print(f"Enter the student's age : {self.student_gender}: ")
        print(f"Enter the student's gender : {self.student_gender}: ")

class Marks:
    def __init__(self):
        self.grade = input("Enter the grade of the student: ")
        print("-------------------Evaluate Marks per subject-----------------------")
        self.english = int(input("Enter marks of English: "))
        self.math = int(input("Enter marks of Math: "))
        self.physics = int(input("Enter marks of Physics: "))
        self.chemistry = int(input("Enter marks of Chemistry: "))
        self.computer = int(input("Enter marks of Computer: "))

    def display(self):
        self.total = self.english + self.math + self.physics + self.chemistry + self.computer
        print("Total marks: ",self.total)

class Data(student,Marks):
    def __init__(self):
        student.__init__(self)
        Marks.__init__(self)
    def result(self):
        Marks.display(self)

s1 = Data()
s1.result()
s2 = Data()
s2.result()

print("You can create more objects to add more student data")
