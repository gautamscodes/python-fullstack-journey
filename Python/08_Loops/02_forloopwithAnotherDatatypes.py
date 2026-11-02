# Strings with loop

s1 = "Hello world"

for char in s1:
    print(char, end=",")
print("End of the loop")


# Tuple with loop

t = (12,1,10, 30,36)

for tup in t:
    print(tup, end=",")
print("End of the Program")

# dictionary with loop

employee = {'empid':1001, 'name': "John Grey", "department": "HR"}

for dict in employee:
    print(dict, employee[dict])

print(employee.items())

for i in employee.items():
    print(i)
    print(i[0])
    print(i[1])
