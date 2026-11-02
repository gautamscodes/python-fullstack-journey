# Keys
d1 = {"Nine":9, "Four":4}
print(d1)


d2 = {2:True, 0: False}
print(d2)

d3 = {True: 6, False: 1}
print(d3)

d4 = {(1,2,3): 6, (1,2): 3}
print(d4)

# Values
# values can be list
student1 = {'id': 1001, 'name':'John', 'marks':[89.5,71.5,81.0]}
print(student1)
print(student1['marks'])
print(student1['marks'][1])

# dictionary
student2 = {'id': 1001, 'name':'John', 'marks':{'eng':89.5,'maths':71.5,'bio':81.0}}
print(student2)
print(student2['marks'])
print(student2['marks']['eng'])

# Some function to fetch the keys.
# keys()

print(student1.keys())

# values()
print(student1.values())

# items()
print(student1.items())
print(type(student1.items()))
