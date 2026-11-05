


#1. Write a Python program to check whether a number is even or odd.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")






#2. Write a program to find the largest of three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number:", a)
elif b >= a and b >= c:
    print("Largest number:", b)
else:
    print("Largest number:", c)






#3. Write a program to check whether a given number is prime.
num = int(input("Enter a number: "))
count = 0

if num > 1:
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")






#4. Write a program to print the Fibonacci series up to n terms.
n = int(input("Enter number of terms: "))
a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c






#5. Write a program to find the factorial of a number using a loop.
num = int(input("Enter a number: "))
fact = 1

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    for i in range(1, num + 1):
        fact = fact * i

    print("Factorial:", fact)






#6. Write a program to reverse a string without using [::-1].
text = input("Enter a string: ")
reverse = ""

for i in text:
    reverse = i + reverse

print("Reversed string:", reverse)






#7. Write a program to check whether a string is a palindrome.
text = input("Enter a string: ")
reverse = ""

for i in text:
    reverse = i + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")






#8. Write a program to count the number of vowels and consonants in a string.
text = input("Enter a string: ")
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






#9. Write a program to find the sum of all elements in a list.
my_list = [10, 20, 30, 40, 50]
total = 0

for i in my_list:
    total = total + i

print("Sum:", total)






#10. Find the largest and smallest element in a list without max() or min().
my_list = [10, 5, 30, 2, 50]

largest = my_list[0]
smallest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)






#11. Write a program to remove duplicate elements from a list.
my_list = [1, 2, 3, 2, 4, 1, 5]
new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)

print("List without duplicates:", new_list)






#12. Count how many times each element appears in a list using a dictionary.
my_list = [1, 2, 2, 3, 3, 3, 4]
frequency = {}

for i in my_list:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print("Frequency:", frequency)






#13. Write a program to find the second-largest number in a list.
my_list = [10, 20, 30, 40, 40]
new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)

new_list.sort()

if len(new_list) >= 2:
    print("Second largest:", new_list[-2])
else:
    print("Second-largest number does not exist")






#14. Write a program to sort a list without using sort() or sorted().
my_list = [5, 2, 8, 1, 3]

for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] > my_list[j]:
            temp = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = temp

print("Sorted list:", my_list)






#15. Write a function that returns a list containing only even numbers.
def even_numbers(my_list):
    even = []

    for i in my_list:
        if i % 2 == 0:
            even.append(i)

    return even

print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8]))






#16. Write a program to find the frequency of each character in a string.
text = input("Enter a string: ")
frequency = {}

for i in text:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print("Character frequency:", frequency)






#17. Write a program to check whether two strings are anagrams of each other.
text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

text1 = text1.replace(" ", "").lower()
text2 = text2.replace(" ", "").lower()

if len(text1) == len(text2):
    if sorted(text1) == sorted(text2):
        print("Anagrams")
    else:
        print("Not anagrams")
else:
    print("Not anagrams")






#18. Write a program to find all duplicate values in a list.
my_list = [1, 2, 3, 2, 4, 1, 5, 3]
duplicates = []

for i in my_list:
    if my_list.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicate values:", duplicates)






#19. Write a program that takes a sentence and finds the longest word.



sentence = input("Enter a sentence: ")
words = sentence.split()

if len(words) > 0:
    longest = words[0]

    for i in words:
        if len(i) > len(longest):
            longest = i

    print("Longest word:", longest)
else:
    print("No words entered")



# 20. STUDENT MARKS, TOTAL, PERCENTAGE, GRADE AND RESULT






marks = []

for i in range(5):
    mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)

valid = True

for mark in marks:
    if mark < 0 or mark > 100:
        valid = False

if valid:
    total = 0

    for mark in marks:
        total = total + mark

    percentage = total / 5

    print("Total marks:", total)
    print("Percentage:", percentage, "%")

  
    passed = True

    for mark in marks:
        if mark < 35:
            passed = False

    if passed:
        print("Result: Pass")

        if percentage >= 90:
            print("Grade: A+")
        elif percentage >= 80:
            print("Grade: A")
        elif percentage >= 70:
            print("Grade: B")
        elif percentage >= 60:
            print("Grade: C")
        elif percentage >= 50:
            print("Grade: D")
        else:
            print("Grade: E")
    else:
        print("Result: Fail")
        print("Grade: F")
else:
    print("Invalid marks. Enter marks between 0 and 100.")







