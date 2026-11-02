# Types of Arguments
# 1. Positional Arguments, 2. Default Arguments, 3.Keyword Arguments
from idlelib.debugobj_r import remote_object_tree_item


# Positional Arguments - passing the arguments in order of their position.

def add(a, b):
    return a + b

result = add(10, 5)
print(result)

# Default arguments
def sub(a, b=10):
    return a - b

result2 = sub(20)
print(result2)

def sub(a, c, b=10):
    return a - b - c

result3 = sub(10,10)
print(result3)

# The non-default arguments should NOT follow the default arguments.


# Keyword Arguments

def mul(a, b, c=10):
    return a * b * c

result4 = mul(b = 10, a = 20, c = 30)
print(result4)