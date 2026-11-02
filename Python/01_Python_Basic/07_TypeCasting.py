# Type Conversion and Type Casting in Python.
from sys import flags

# integer to float
num1 = 100
print(num1)
print(type(num1))

print(float(num1))

num2 = float(num1)
print(num2)
print(type(num2))

print(type(num1))

num1 = float(num1)
print(num1)
print(type(num1))

# Explicit Conversion
num3 = 56.45
print(num3)
print(type(num3))
print(int(num3))

print(int(77.85))

print(num3)
print(num2)
print(num1)

num4 = 1000
print(num4)

print(str(num4))

# integer to String ---> it is possible
x = str(num4)
print(x)
print(type(x))

# String to int --> not possible, if it is charcters in the variable.

s2 = '123'
s3 = int(s2)
print(s3)
print(type(s3))
print(s2)


# type of conversion of boolean

val1 = True
print(val1)
print(type(val1))

print(str(val1))





