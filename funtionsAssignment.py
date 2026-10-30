#1

n = int(input("Enter number: "))

def is_even(n):
    if n % 2 == 0:
        print("number is even")
    else:
        print("number is odd")

print(is_even(n))

#2
a = int(input("Enter number: "))
b = int(input("Enter number: "))

def largest(a, b):
    if a > b:
        return a
    else:
        return b

print(largest(a, b))

#3

n = int(input("Enter number: "))

def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print(print_numbers(n))

#4

n = int(input("Enter number: "))

def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_n(n))

#5

n = int(input("Enter number: "))

def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

print(table(n))

#6



def count_even_numbers():
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    return count

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(count_even_numbers())

#7

def largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(largest_number(numbers))

#11



def fizz_buzz(n):
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FIZZBUZZ")
        elif i % 3 == 0:
            print("FIZZ")
        elif i % 5 == 0:
            print("BUZZ")
        else:
            print(i)

print(fizz_buzz(100))


#12

def check_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

print(check_palindrome("wow"))

#13

def count_vowels(string):
    count = 0
    for char in string:
        if char.lower() in "aeiou":
            count += 1
    return count

print(count_vowels("Hi hope you are doing good"))

#14

#Can't think of a function for this one. Please help me with this one?

#15

def guessing_game():
    import random
    number_to_guess = random.randint(1, 10)
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess != number_to_guess:
            print("No try again")
        else:
            print(f"Congratulations you guessed the number {number_to_guess}")
            break

print(guessing_game())

#16

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

print(grade(int(input("Enter marks: "))))