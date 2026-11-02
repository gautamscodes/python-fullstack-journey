# Tuple creation

t1 = ("Python", 10, 1.5, True, [1,2,3], (10,20))
print(t1)
print(len(t1))

# Accessing items from the tuple using index.

print(t1[0])
print(t1[-1])


t2 = 10,20,30
print(t2)
print(type(t2))

# converting list into tuple

l1 = [1,2,3]
print(type(l1))
print(l1)
t3 = tuple(l1)
print(t3, type(t3))

# converting tuple into the list

fruits = ("Mango", "Orange", "Apple")
print(fruits, type(fruits))

fruits = list(fruits)
print(fruits, type(fruits))


