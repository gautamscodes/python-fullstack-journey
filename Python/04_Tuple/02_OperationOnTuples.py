'''

concatenation, repetition, membership
count, index,
min, max,sum

'''
from itertools import count

student_details1 = (1001, "John")
student_details2 = (78.5, 91.0, 83.5, 79.5)

# concatenation (+)
student_details = student_details1 + student_details2
print(student_details)

# Repetition (*)
t1 = ("Class 5", 5000)
print(t1 * 5)

# membership (in, not in)
print(91.0 in student_details2)
print(91.0 not in student_details2)

# We can perform only read operation not write operation on tuple.

# count

t1 = ( 10, 4, 1, 9, 0, 3, 1)
print(t1.count(1))

# index --> it will find the index position value.
print(t1.index(4)) # what is the index of 4 in tuple 1?
print(t1.index(1)) # It will return only the first occurrence value index only.

# Universal function --> min, max, sum

print(min(t1))
print(max(t1))
print(sum(t1))




