# Comparision in String.

print("Python " == "Python")
print("Python" == "Python")

# Removing spaces from a string --> strip()

s1 = "Python "
s2 = "Python"

s3 = s1.strip()
print(s3)

print(s1.strip() == "Python")


#  Replace function

a1 = "We are learning Python"
print(a1)
print(a1.replace("Python", "Java"))
print(a1.replace("e", "E"))
print(a1.replace("e", "E", 1))
