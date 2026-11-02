# if-else
import numbers

age = int(input("What is your age?: "))

if age >= 18:
    print("Congrats! you can cast your vote!")
else:
    print("A few more years before you can vote.")

print("Rest of the program")

"""
    Write a Program to print if a number is odd or even
    Even - when the number is divisible by 2.
    Odd - when the number is not divisible by 2.
    
"""

number = int(input("Enter the number?: "))

if number % 2 == 0:
    print(f"{number} is Even Number.")
else:
    print(f"{number} is Odd Number.")

"""
    Write a program to print the number is negative or positive.
    
"""

num = int(input("Enter the number : "))

if num <= 0:
    print(f"{num} is negative number.")
else:
    print(f"{num} is Positive number.")
    