import math

# 1. Check whether given number is divisible by 3 and 5 both.
num = 15
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5.")
else:
    print(f"{num} is not divisible by both 3 and 5.")

# 2. Check whether a given number is a multiple of five or not.
num = 20
if num % 5 == 0:
    print(f"{num} is a multiple of five.")
else:
    print(f"{num} is not a multiple of five.")

# 3. Find the greatest among two numbers. If numbers are equal, then print “numbers are equal”.
num1, num2 = 10, 20
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num2 > num1:
    print(f"{num2} is greater than {num1}.")
else:
    print("Numbers are equal.")

# 4. Find the greatest among three numbers assuming no two values are the same.
num1, num2, num3 = 30, 40, 50
if num1 > num2 and num2 > num3:
    print(num1,"is greater:")
elif num2 > num3 and num2 > num1:
    print(num2,"is greater:")
else:
    print(num3,"is greater:")

# 5. Check whether the quadratic equation has real roots or imaginary roots. Display the roots.
a, b, c = 1, -3, 2
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"The quadratic equation has real roots: {root1}, {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"The quadratic equation has real and equal roots: {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"The quadratic equation has imaginary roots: {real_part} + {imaginary_part}i, {real_part} - {imaginary_part}i")

# 6. Find whether a given year is a leap year or not.
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 7. Write a program which takes any date as input and display the next date of the calendar.
day, month, year = 29, 2, 2004
leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if leap_year:
    days_in_month[1] = 29
if day < days_in_month[month - 1]:
    next_day = day + 1
    next_month = month
    next_year = year
else:
    next_day = 1

    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
print(f"Next date: day={next_day} month={next_month} year={next_year}")


# 8. Print the grade sheet of a student for the given range of CGPA.
name = "Rishant Kushwaha"
roll_number = "R2142232084"
semester = 1
marks = {'PDS': 80, 'Python': 80, 'Chemistry': 90, 'English': 78, 'Physics': 75}
total_marks = sum(marks.values())
percentage = total_marks / (len(marks) * 100) * 100
cgpa = percentage / 10

if cgpa <= 3.4:
    grade = 'F'
elif cgpa <= 5.0:
    grade = 'C+'
elif cgpa <= 6.0:
    grade = 'B'
elif cgpa <= 7.0:
    grade = 'B+'
elif cgpa <= 8.0:
    grade = 'A'
elif cgpa <= 9.0:
    grade = 'A+'
else:
    grade = 'O (Outstanding)'

print(f"Name: {name}\nRoll Number: {roll_number}\nSem: {semester}")
print("Subject name: Marks")
for subject, marks in marks.items():
    print(f"{subject}: {marks}")
print(f"Percentage: {percentage}%\nCGPA: {cgpa}\nGrade: {grade}")
