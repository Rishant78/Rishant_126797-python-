num = int(input("Enter a number: "))
is_prime = True

if num <= 1:
    is_prime = False
elif num <= 3:
    is_prime = True
elif num % 2 == 0 or num % 3 == 0:
    is_prime = False
else:
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            is_prime = False
            break
        i += 6

if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

num = input("Enter a number: ")
is_palindrome = num == num[::-1]

if is_palindrome:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")

num = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) for digit in str(num))

print("Sum of digits in", num, "is:", sum_of_digits)

divisible_by_5_or_7 = [num for num in range(1, 101) if num % 5 == 0 or num % 7 == 0]
print("Numbers divisible by 5 or 7 between 1 and 100:", divisible_by_5_or_7)

print("Prime numbers between 1 and 100:")
for num in range(1, 101):
    is_prime = True
    if num <= 1:
        is_prime = False
    elif num <= 3:
        is_prime = True
    elif num % 2 == 0 or num % 3 == 0:
        is_prime = False
    else:
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                is_prime = False
                break
            i += 6
    if is_prime:
        print(num, end=" ")
print()


num = int(input("Enter a number: "))
print("Multiplication table for", num)
for i in range(1, 11):
    print(num, "*", i, "=", num*i)
