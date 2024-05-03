# 1. Scan n values in range 0-3 and print the number of times each value has occurred.
n = int(input("Enter the number of values: "))
occurrences = {0: 0, 1: 0, 2: 0, 3: 0}
for _ in range(n):
    value = int(input("Enter a value (0-3): "))
    if value in occurrences:
        occurrences[value] += 1
print("Occurrences of each value:", occurrences)

# 2. Create a tuple to store n numeric values and find the average of all values.
n = int(input("Enter the number of values: "))
values = tuple(float(input("Enter a numeric value: ")) for _ in range(n))
average = sum(values) / n
print("Average of all values:", average)

# 3. WAP to input a list of scores for N students in a list data type. Find the score of the
#    runner-up and print the output.
N = int(input("Enter the number of students: "))
scores = list(map(int, input("Enter scores of N students separated by space: ").split()))
unique_scores = list(set(scores))
unique_scores.sort(reverse=True)
print("Runner-up score:", unique_scores[1])

# 4. Create a dictionary of n persons where the key is the name and the value is the city.
#    a) Display all names
#    b) Display all city names
#    c) Display student name and city of all students.
#    d) Count the number of students in each city.
n = int(input("Enter the number of persons: "))
persons = {}
for _ in range(n):
    name = input("Enter person's name: ")
    city = input("Enter person's city: ")
    persons[name] = city

# a) Display all names
print("Names:", list(persons.keys()))

# b) Display all city names
print("City Names:", list(set(persons.values())))

# c) Display student name and city of all students.
print("Student Name and City:")
for name, city in persons.items():
    print(name, "-", city)

# d) Count the number of students in each city.
city_count = {}
for city in persons.values():
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1
print("Number of students in each city:", city_count)

# 5. Store details of n movies in a dictionary by taking input from the user. Each movie
#    must store details like name, year, director name, production cost, collection made (earning).
#    Perform the following:
#    a) print all movie details
#    b) display names of movies released before 2015
#    c) print movies that made a profit.
#    d) print movies directed by a particular director.
n = int(input("Enter the number of movies: "))
movies = []
for i in range(n):
    movie_details = {}
    print(f"Enter details for movie {i+1}:")
    movie_details['name'] = input("Name: ")
    movie_details['year'] = int(input("Year: "))
    movie_details['director'] = input("Director Name: ")
    movie_details['production_cost'] = float(input("Production Cost: "))
    movie_details['collection'] = float(input("Collection: "))
    movies.append(movie_details)

# a) Print all movie details
print("All movie details:")
for movie in movies:
    print(movie)

# b) Display names of movies released before 2015
print("Movies released before 2015:")
for movie in movies:
    if movie['year'] < 2015:
        print(movie['name'])

# c) Print movies that made a profit
print("Movies that made a profit:")
for movie in movies:
    if movie['collection'] > movie['production_cost']:
        print(movie['name'])

# d) Print movies directed by a particular director
director = input("Enter director's name to find their movies: ")
print(f"Movies directed by {director}:")
for movie in movies:
    if movie['director'] == director:
        print(movie['name'])
