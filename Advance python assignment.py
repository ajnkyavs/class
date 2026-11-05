


# 1. DATA TYPES


#1. Find the data type of every value in a mixed list.



my_list = [10, "Hello", 10.5, True, 5 + 2j]

for i in my_list:
    print(i, type(i))


#2. Convert a nested list into a tuple of tuples.

my_list = [[1, 2], [3, 4], [5, 6]]
result = tuple(tuple(i) for i in my_list)
print(result)


#3. Remove all duplicate values while preserving the original order.



my_list = [1, 2, 3, 2, 4, 1, 5]
new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)



# 2. OPERATORS


#4. Check whether a number is a power of 2 using operators.


num = 16

if num > 0 and (num & (num - 1)) == 0:
    print("Power of 2")
else:
    print("Not a power of 2")


#5. Swap two numbers using bitwise XOR.
a = 10
b = 20

a = a ^ b
b = a ^ b
a = a ^ b

print("a =", a)
print("b =", b)



#6. Check whether a number is divisible by both 4 and 6.


num = 24

if num % 4 == 0 and num % 6 == 0:
    print("Divisible by both")
else:
    print("Not divisible by both")


#7. Calculate the electricity bill using different unit rates.
# Example: first 100 units = Rs. 5/unit,
# next 100 units = Rs. 7/unit, above 200 = Rs. 10/unit.



units = int(input("Enter electricity units: "))

if units < 0:
    print("Units cannot be negative")
elif units <= 100:
    bill = units * 5
    print("Total bill:", bill)
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
    print("Total bill:", bill)
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
    print("Total bill:", bill)



# 3. CONDITIONAL STATEMENTS


#8. Check whether three sides can form a triangle.


a = 5
b = 6
c = 7

if a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and a + c > b:
    print("Valid triangle")
else:
    print("Invalid triangle")



#9. Determine the type of triangle.



a = 5
b = 5
c = 5

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or b + c <= a or a + c <= b:
    print("Invalid triangle")
elif a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")



#10. Create a simple ATM menu (Withdraw, Deposit, Balance).



balance = 10000

print("1. Withdraw")
print("2. Deposit")
print("3. Balance")
choice = int(input("Enter your choice: "))

if choice == 1:
    amount = int(input("Enter amount to withdraw: "))
    if 0 < amount <= balance:
        balance = balance - amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)
    else:
        print("Invalid amount or insufficient balance")
elif choice == 2:
    amount = int(input("Enter amount to deposit: "))
    if amount > 0:
        balance = balance + amount
        print("Deposit successful")
        print("New balance:", balance)
    else:
        print("Invalid amount")
elif choice == 3:
    print("Balance:", balance)
else:
    print("Invalid choice")


#11. Calculate income tax based on example tax slabs.
# Practice example only; this is not the current Indian tax calculation.



income = int(input("Enter annual income: "))

if income < 0:
    print("Income cannot be negative")
elif income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.20
else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

if income >= 0:
    print("Income tax:", tax)


#12. Create a menu-driven calculator using if-elif.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
elif choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")



# 4. LOOPS


#13. Print all prime numbers between 1 and n.


n = 20

for num in range(2, n + 1):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        print(num)


#14. Find the factorial of a number using a loop.

num = 5
fact = 1

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial:", fact)



#15. Print the Fibonacci series up to n terms.
n = 10
a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c


#16. Check whether a number is an Armstrong number.



num = 153

if num < 0:
    print("Not an Armstrong number")
else:
    temp = num
    total = 0
    digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == num:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")


#17. Reverse a number and check whether it is a palindrome.


num = 121
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

print("Reverse:", reverse)

if num == reverse:
    print("Palindrome")
else:
    print("Not palindrome")


#18. Find the Greatest Common Divisor (GCD) of two numbers.



a = 12
b = 18

x = abs(a)
y = abs(b)

while y != 0:
    temp = y
    y = x % y
    x = temp

print("GCD:", x)



# 5. FUNCTIONS


#19. Write a function to check whether a string is a palindrome.



def palindrome(text):
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")

palindrome("madam")


#20. Write a function to count vowels and consonants in a string.




def count_letters(text):
    vowels = 0
    consonants = 0

    for i in text.lower():
        if i.isalpha():
            if i in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)

count_letters("Hello World")


#21. Create a function to calculate simple and compound interest.
def interest(p, r, t):
    si = (p * r * t) / 100
    ci = p * (1 + r / 100) ** t - p

    print("Simple Interest:", si)
    print("Compound Interest:", ci)

interest(10000, 5, 2)


#22. Write a function to return all factors of a number.


def factors(num):
    result = []

    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)

    return result

print(factors(12))





#23. Write a function to find the second-largest number in a list.



def second_largest(my_list):
    new_list = list(set(my_list))
    new_list.sort()

    if len(new_list) >= 2:
        return new_list[-2]
    else:
        return None

print("Second largest:", second_largest([10, 20, 30, 40, 40]))



# 6. LISTS


#24. Merge two lists without duplicates.



a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
result = []

for i in a + b:
    if i not in result:
        result.append(i)

print(result)


#25. Find the second-largest and second-smallest elements.



my_list = [10, 20, 30, 40, 50]
new_list = list(set(my_list))
new_list.sort()

if len(new_list) >= 2:
    print("Second smallest:", new_list[1])
    print("Second largest:", new_list[-2])
else:
    print("Not enough distinct elements")


#26. Rotate a list to the left by k positions.



my_list = [1, 2, 3, 4, 5]
k = 2

if len(my_list) > 0:
    k = k % len(my_list)
    result = my_list[k:] + my_list[:k]
else:
    result = my_list

print(result)


#27. Separate even and odd numbers into two lists.


my_list = [1, 2, 3, 4, 5, 6]
even = []
odd = []

for i in my_list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even:", even)
print("Odd:", odd)


#28. Find the common elements between two lists.



a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common = []

for i in a:
    if i in b and i not in common:
        common.append(i)

print(common)



# 7. TUPLES & SETS


#29. Count the frequency of each element in a tuple.



my_tuple = (1, 2, 2, 3, 3, 3)

for i in set(my_tuple):
    print(i, ":", my_tuple.count(i))


#30. Find the union, intersection and difference of two sets.


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a.union(b))
print("Intersection:", a.intersection(b))
print("Difference:", a.difference(b))


#31. Check whether one set is a subset of another.



a = {1, 2}
b = {1, 2, 3, 4}

if a.issubset(b):
    print("Subset")
else:
    print("Not a subset")



# 8. DICTIONARIES


#32. Count the frequency of words in a sentence.



sentence = "python is easy and python is useful"
words = sentence.split()
frequency = {}

for i in words:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)


#33. Create a dictionary from two lists (keys and values).



keys = ["name", "age", "city"]
values = ["Rahul", 25, "Pune"]

my_dict = dict(zip(keys, values))
print(my_dict)


#34. Sort a dictionary by its values.



my_dict = {"A": 30, "B": 10, "C": 20}
result = dict(sorted(my_dict.items(), key=lambda x: x[1]))

print(result)



# 9. FILE HANDLING


#35. Read a text file and count lines, words and characters.
# Create a file named data.txt in the same folder before running this.



with open("data.txt", "r") as file:
    text = file.read()

lines = text.splitlines()
words = text.split()
characters = len(text)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)


#36. Copy only the even-numbered lines from one file to another.
# This reads data.txt and writes the even-numbered lines to output.txt.




with open("data.txt", "r") as file:
    lines = file.readlines()

with open("output.txt", "w") as new_file:
    for i in range(len(lines)):
        if (i + 1) % 2 == 0:
            new_file.write(lines[i])

print("Even-numbered lines copied to output.txt")



# 10. EXCEPTION HANDLING





#37. Handle invalid integer input using try-except.



try:
    num = int(input("Enter an integer: "))
    print("Number:", num)
except ValueError:
    print("Please enter a valid integer")


#38. Handle file-not-found errors while reading a file.


try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")



# 11. MODULES


#39. Create a random password generator using random and string modules.


import random
import string

characters = string.ascii_letters + string.digits
password = ""

for i in range(8):
    password += random.choice(characters)

print("Password:", password)


#40. Use datetime to calculate the number of days between two dates.



from datetime import date

date1 = date(2026, 1, 1)
date2 = date(2026, 12, 31)

difference = date2 - date1
print("Total days:", abs(difference.days))






