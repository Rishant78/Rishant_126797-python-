# 1. Create a class of student (name, sap id, marks[phy,chem,maths] ). Create 3 
# objects by taking inputs from the user and display details of all students.

class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Marks (Physics, Chemistry, Maths):", self.marks)

# Create three Student objects
students = []
for i in range(3):
    name = input("Enter student name: ")
    sap_id = input("Enter SAP ID: ")
    phy_marks = int(input("Enter Physics marks: "))
    chem_marks = int(input("Enter Chemistry marks: "))
    maths_marks = int(input("Enter Maths marks: "))
    marks = [phy_marks, chem_marks, maths_marks]
    student = Student(name, sap_id, marks)
    students.append(student)

# Display details of all students
print("\nDetails of all students:")
for student in students:
    student.display_details()
    print()

# 2. Add constructor in the above class to initialize student details of n students and 
# implement following methods: 
# a) Display() student details 
# b) Find Marks_percentage() of each student 
# c) Display result() [Note: if marks in each subject >40% than Pass else Fail] 
# Write a Function to find average of the class. 

class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Marks (Physics, Chemistry, Maths):", self.marks)

    def marks_percentage(self):
        total_marks = sum(self.marks)
        percentage = (total_marks / (len(self.marks) * 100)) * 100
        return percentage

    def result(self):
        for mark in self.marks:
            if mark < 40:
                return "Fail"
        return "Pass"

def class_average(students):
    total_percentage = sum(student.marks_percentage() for student in students)
    average_percentage = total_percentage / len(students)
    return average_percentage

# Create a list of Student objects
students = []
n = int(input("Enter the number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    sap_id = input("Enter SAP ID: ")
    phy_marks = int(input("Enter Physics marks: "))
    chem_marks = int(input("Enter Chemistry marks: "))
    maths_marks = int(input("Enter Maths marks: "))
    marks = [phy_marks, chem_marks, maths_marks]
    student = Student(name, sap_id, marks)
    students.append(student)

# Display details, marks percentage, and result of each student
print("\nDetails of all students:")
for student in students:
    student.display_details()
    print("Marks Percentage:", student.marks_percentage())
    print("Result:", student.result())
    print()

# Calculate and display the average percentage of the class
average = class_average(students)
print("Average Percentage of the class:", average)

