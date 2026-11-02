# .py file is a module. it also contains executable files.
"""
Python Built in Module are the module which are available when we download the python.
ex:- math, random, datatime,........


"""

# How to import the module

# Simple way is = import module_name
# if we import only few function and variable then we use :=> from module_name import f1,f2,f3
# Syntax to create an alias for the module that is imported: import module_name as alias_name


import math
# math example
# Calculate square root of a number
num = 100
output = math.sqrt(num)
print(f"Square root of {num} is {output}")

# Calculate the area of circle
# pi = 3.14
radius = 5
area_of_circle = math.pi * (radius ** 2)
print(f"Area of Circle with {radius} is {area_of_circle}")
print(math.pi)

# random example

# throw a die
from random import randint
value = randint(1,6)
print(value)

# using datetime

import datetime as dt
t = dt.time(8,43,51)
print(t)

