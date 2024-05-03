# 1. Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
def find_max_min(sequence):
    maximum = sequence[0]
    minimum = sequence[0]
    for num in sequence:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return maximum, minimum

# 2. Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.
def sum_cube_positive_integers(n):
    return sum(i**3 for i in range(1, n))

# 3. Write a Python function to print 1 to n using recursion.
def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)
        print(n)

# 4. Write a recursive function to print Fibonacci series upto n terms.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci_series(n):
    for i in range(n):
        print(fibonacci(i))

# 5. Write a lambda function to find the volume of a cone.
volume_of_cone = lambda radius, height: (1/3) * 3.14159 * radius**2 * height

# 6. Write a lambda function which gives a tuple of max and min from a list.
max_min_tuple = lambda lst: (max(lst), min(lst))

# 7. Write functions to explain mentioned concepts:
# a. Keyword argument
def keyword_argument_example(name, age):
    print("Name:", name)
    print("Age:", age)

# b. Default argument
def default_argument_example(name="John", age=30):
    print("Name:", name)
    print("Age:", age)

# c. Variable length argument
def variable_length_argument_example(*args):
    print("Arguments:", args)

# Test cases for the functions
sequence = [10, 6, 8, 90, 12, 56]
print("Max and Min:", find_max_min(sequence))
print("Sum of cubes up to 5:", sum_cube_positive_integers(5))
print("Numbers from 1 to 5:")
print_numbers(5)
print("Fibonacci series up to 6 terms:")
print_fibonacci_series(6)
print("Volume of cone with radius 3 and height 5:", volume_of_cone(3, 5))
print("Max and Min from list:", max_min_tuple(sequence))

# Test cases for function explanation
keyword_argument_example(age=25, name="Alice")
default_argument_example()
variable_length_argument_example(1, 2, 3, 4, 5)
