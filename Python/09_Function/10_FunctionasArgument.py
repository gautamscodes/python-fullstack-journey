# In python, we can pass a function as argument of another function.

def add_1(number):
    return number + 1
print(add_1(10))


def square(number):
    return number ** 2

print(square(4))

num = int(input("Enter a number : "))
res = add_1(num)
res2 = square(res)
print(f"Output is : {res2}")

res3 = square(add_1(num))
print(res3)

