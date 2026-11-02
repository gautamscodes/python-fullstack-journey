# Counting substrings from a string
# count()
# string.count()

s1 = "We are learning Python. Python is fun."
s2 = "Python"
print(s1.count(s2))
print(f"Occurrences of {s2} is {s1.count(s2)}")

# finding the characters
s3 = "e"
print(f"Occurrence of {s3} is {s1.count((s3))}")
s4 = " "
print(f"Occurrence of {s4} is {s1.count((s4))}")


# Case in Python.
# upper(), lower(), capatilizer()

x1 = "Python"
print(x1.upper())
x2 = "Python3.14"
print(x2.upper())
print(x2.lower())  # Lowercase()
print(s1.title()) # each word of first charcter will be Capital.
print(s1.capitalize())


# starting and ending of a string.

s1 = "We are learning Python"

#startswith() --> starting. startswith(substring)
print(s1.startswith("We"))

# endswith()
print(s1.endswith("Python"))


