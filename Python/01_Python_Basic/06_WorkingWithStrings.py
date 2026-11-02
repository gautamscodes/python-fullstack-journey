# Working with Strings

s1 = "hello world"
print(s1)
print(type(s1))

s2 = "We are learning Python"
print(s2)
print(type(s2))

s3 = """ Hello everyone.
We are looking at strings.
Bye"""
print(s3)
print(type(s3))

# length of the strings

s4 = "Python"
print(len(s4))
print(s4)

print(len(s1))
print(len(s2))
print(len(s3))

# Indexing in Strings

print(s4[0])
print(s4[1])
print(s4[5])
# print(s4[6])  --- Index out of range.

# negative indexing
print(s4[-1])
print(s4[-3])
print(s4[-6])

# join two string

s5 = s1 + ' ' + s2
print(s5)



