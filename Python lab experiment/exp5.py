'''Experiment 5: String and Sets 
1.  Write a program to count and display the number of capital letters in a given string. 
2.  Count total number of vowels in a given string. 
3.  Input a sentence and print words in separate lines. 
4. WAP to enter a string and a substring. You have to print the number of times that 
the substring occurs in the given string. String traversal will take place from left to 
right, not from right to left. 
Sample Input 
ABCDCDC 
CDC 
Sample Output 
2 
5. Given a string containing both upper and lower case alphabets. Write a Python 
program to count the number of occurrences of each alphabet (case insensitive) 
and display the same. 
Sample Input 
ABaBCbGc 
Sample Output 
2A 
3B 
2C 
1G 
6. Program to count number of unique words in a given sentence using sets. 
7. Create 2 sets s1 and s2 of n fruits each by taking input from user and find: 
a) Fruits which are in both sets s1 and s2 
b) Fruits only in s1 but not in s2 
c) Count of all fruits from s1 and s2 
8. Take two sets and apply various set operations on them : 
S1 = {Red ,yellow, orange , blue } 
S2 = {violet, blue , purple}'''

string = input("Enter a string: ")
capital_count = sum(1 for char in string if char.isupper())
print("Number of capital letters:", capital_count)


string = input("Enter a string: ")
vowels = 'aeiouAEIOU'
vowel_count = sum(1 for char in string if char in vowels)
print("Total number of vowels:", vowel_count)


sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    print(word)


string = input("Enter a string: ")
substring = input("Enter a substring: ")
count = string.count(substring)
print("Number of times the substring occurs:", count)


string = input("Enter a string: ").lower()
alphabet_count = {char: string.count(char) for char in string if char.isalpha()}
for char, count in alphabet_count.items():
    print(count, char)


sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)
print("Number of unique words:", len(unique_words))



n = int(input("Enter the number of fruits: "))
s1 = set(input("Enter fruits for set 1: ").split()[:n])
s2 = set(input("Enter fruits for set 2: ").split()[:n])

# a) Fruits which are in both sets s1 and s2
print("Fruits in both sets:", s1.intersection(s2))

# b) Fruits only in s1 but not in s2
print("Fruits only in s1:", s1.difference(s2))

# c) Count of all fruits from s1 and s2
print("Total count of fruits:", len(s1.union(s2)))




S1 = {'Red', 'yellow', 'orange', 'blue'}
S2 = {'violet', 'blue', 'purple'}

# Union of two sets
print("Union of sets:", S1.union(S2))

# Intersection of two sets
print("Intersection of sets:", S1.intersection(S2))

# Difference of two sets (S1 - S2)
print("Difference of sets (S1 - S2):", S1.difference(S2))

# Symmetric difference of two sets
print("Symmetric difference of sets:", S1.symmetric_difference(S2))
