# Return the value

def even_odd(num):
    if num % 2 == 0:
        return f"{num} is Even"
        # print(f"{num} is Even")

    else:
        return f"{num} is Odd"
        # print(f"{num} is Odd")

even_odd(10)
even_odd(11)

# checking the function returning anything or not  -> if function return None then it means function not return anything.

result = even_odd(10)
print(result)

def add(num1, num2):
    result = num1 + num2
    return result


val1 = int(input("Enter a num1 : "))
val2 = int(input("Enter a num2 : "))

val = add(val1, val2)
print(f"Addition of {val1} and {val2} is {val}")

# Returning Multiple result

def arithmetic(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    return add, sub, mul

res1, res2, res3 = arithmetic(val1, val2)
print(f"Addition of {val1} and {val2} is {res1}")
print(f"Substraction of {val1} and {val2} is {res2}")
print(f"Multiplication of {val1} and {val2} is {res3}")

