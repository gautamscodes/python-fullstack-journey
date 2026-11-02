"""
Recursion is a process in which a function calls itself till a certain condition is not met
Factorial of n => n * (n-1) * (n -2) * .... 2 * 1
n!
4! = 4 * 3 * 2 * 1 = 24

n! => n * (n-1) * (n-2) * .... * 2 * 1
    => n * (n-1)!
    => n * (n-1)! * (n-2)! ........

There are 2 parts to any recursive function
1. Base/terminal condition
2. Recursive condition
"""

# normal way to write the program for factorial

def fact(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    return factorial

n = 5
print(f"Factorial of {n} is {fact(n)}")


# With Recursion

def fact_rec(num):
    if num == 1:
        return 1
    else:
        factorial = num * fact(num -1)
        return factorial

print(fact_rec(5))

