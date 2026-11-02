"""
Their two type of error in the python
1. Compile time error :- Compile time error => syntax error & Indentation error.
2. Run time error :- Exception Error => exception are nothing but syntactically correct, but it will give the error
on run time that is called Exception error.
    Error during the runtime is called Run time error and Exception error.


"""
from zoneinfo import reset_tzpath

# compile time error

# print("this compile time error')
# age = 10
# if age < 18:
# print(age)

# Exception Error

# x = 100/0
# print(x)

# handle the exception error using try and except block



try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("The Denominator can not be Zero(0)")
except ValueError:
    print("Input should only be digits")





