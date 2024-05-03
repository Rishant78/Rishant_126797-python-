# 1. Add few names, one name in each row, in “name.txt" file.
with open("name.txt", "w") as file:
    file.write("Alice\n")
    file.write("Bob\n")
    file.write("Charlie\n")
    file.write("David\n")
    file.write("Eva\n")

# a. Count the number of names
with open("name.txt", "r") as file:
    names = file.readlines()
num_of_names = len(names)
print("Number of names:", num_of_names)

# b. Count all names starting with a vowel
vowels = "aeiouAEIOU"
num_starting_with_vowel = sum(1 for name in names if name[0] in vowels)
print("Number of names starting with a vowel:", num_starting_with_vowel)

# c. Find the longest name
longest_name = max(names, key=len).strip()
print("Longest name:", longest_name)

# 2. Store integers in a file.
with open("integers.txt", "w") as file:
    file.write("10\n")
    file.write("20\n")
    file.write("30\n")
    file.write("40\n")
    file.write("50\n")

# Read integers from file
with open("integers.txt", "r") as file:
    integers = [int(line.strip()) for line in file]

# a. Find the max number
max_number = max(integers)
print("Max number:", max_number)

# b. Find average of all numbers
average = sum(integers) / len(integers)
print("Average:", average)

# c. Count number of numbers greater than 100
num_greater_than_100 = sum(1 for num in integers if num > 100)
print("Number of numbers greater than 100:", num_greater_than_100)

# 3. Create a file named "city.txt" with details of 5 cities.
with open("city.txt", "w") as file:
    file.write("Dehradun 5.78 308.20\n")
    file.write("Delhi 190 1484\n")
    file.write("Mumbai 120 603\n")
    file.write("Kolkata 70 185\n")
    file.write("Chennai 60 426\n")

# a. Display details of all cities
with open("city.txt", "r") as file:
    cities = [line.strip().split() for line in file]
print("Details of all cities:")
for city in cities:
    print(city)

# b. Display city names with population more than 10 Lakhs
population_more_than_10_lakhs = [city[0] for city in cities if float(city[1]) > 10]
print("City names with population more than 10 Lakhs:", population_more_than_10_lakhs)

# c. Display sum of areas of all cities
sum_of_areas = sum(float(city[2]) for city in cities)
print("Sum of areas of all cities:", sum_of_areas)

# 4. Implement the integer division operation.
try:
    N = int(input("Enter the number of test cases: "))
    for _ in range(N):
        a, b = map(int, input().split())
        print(a // b)
except ZeroDivisionError:
    print("Error Code: integer division or modulo by zero")
except ValueError as e:
    print(f"Error Code: {e}")

# 5. Create multiple suitable exceptions for a file handling program.
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to access the file.")
except Exception as e:
    print(f"An error occurred: {e}")
