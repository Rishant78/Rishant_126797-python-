'''1. Declare these variables (x, y and z) as integers. Assign a value of 9 to x, Assign a 
value of 7 to y, perform addition, multiplication, division and subtraction on these 
two variables and Print out the result. 
2. Write a Program where the radius is taken as input to compute the area of a circle. 
3. Write a Python program to solve (x+y)*(x+y) 
Test data : x = 4 , y = 3 
Expected output: 49 
4. Write a program to compute the length of the hypotenuse (c) of a right triangle 
using Pythagoras theorem.  
5. Write a program to find simple interest. 
6. Write a program to find area of triangle when length of sides are given. 
7. Write a program to convert given seconds into hours, minutes and remaining 
seconds. 
8. Write a program to swap two numbers without taking additional variable. 
9. Write a program to find sum of first n natural numbers. 
10. Write a program to print truth table for bitwise operators( & , | and ^ operators) 
11. Write a program to find left shift and right shift values of a given number. 
12. Using membership operator find whether a given number is in sequence 
(10,20,56,78,89) 
13. Using membership operator find whether a given character is in a string.'''


x=input("Enter a number:")
x_as_int=int(x)
y=int(input("Enter a number:"))
Add=x_as_int+y
mul=x_as_int*y
div=x_as_int/y
print(mul)
print(Add)
print(div)

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius**2
print("Area of the circle:", area)

x = 4
y = 3
result = (x + y) * (x + y)
print("Result:", result)

a = float(input("Enter Perpendicular: "))
b = float(input("Enter Base: "))

h = math.sqrt(a**2 + b**2)  
c = h**2  

print("Hypotenuse =", c)

a = float(input("Enter the length of side 'a': "))
b = float(input("Enter the length of side 'b': "))
c = float(input("Enter the length of side 'c': "))

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Area of the triangle:", area)

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)

seconds = int(input("Enter the number of seconds: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Remaining Seconds:", remaining_seconds)

a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

a = a + b
b = a - b
a = a - b

print("After swapping, a =", a)
print("After swapping, b =", b)

n = int(input("Enter a positive integer (n): "))
sum_natural_numbers = (n * (n + 1)) // 2
print("Sum of first", n, "natural numbers:", sum_natural_numbers)

print("Truth Table for Bitwise AND (&):")
print("0 & 0 =", 0 & 0)
print("0 & 1 =", 0 & 1)
print("1 & 0 =", 1 & 0)
print("1 & 1 =", 1 & 1)

print("\nTruth Table for Bitwise OR (|):")
print("0 | 0 =", 0 | 0)
print("0 | 1 =", 0 | 1)
print("1 | 0 =", 1 | 0)
print("1 | 1 =", 1 | 1)

print("\nTruth Table for Bitwise XOR (^):")
print("0 ^ 0 =", 0 ^ 0)
print("0 ^ 1 =", 0 ^ 1)
print("1 ^ 0 =", 1 ^ 0)
print("1 ^ 1 =", 1 ^ 1)

number = int(input("Enter a number: "))
shift_value = int(input("Enter the shift value: "))

left_shift_result = number << shift_value
right_shift_result = number >> shift_value

print("Left Shift Result:", left_shift_result)
print("Right Shift Result:", right_shift_result)

sequence = [10, 20, 56, 78, 89]
number_to_check = int(input("Enter a number to check: "))

if number_to_check in sequence:
    print(number_to_check, "is in the sequence.")
else:
    print(number_to_check, "is not in the sequence.")

string_input = input("Enter a string: ")
character_to_check = input("Enter a character to check: ")

if character_to_check in string_input:
    print(character_to_check, "is present in the string.")
else:
    print(character_to_check, "is not present in the string.")




