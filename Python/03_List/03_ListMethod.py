# List Method
# append() :- adds an item to teh end of the list

fruits = ["Mango", "Apple", "Orange"]
print(fruits)
fruits.append("Banana")
print(fruits)
print(fruits.append("Kiwi"))  # It gives None because list does not make new list so that it will add it on the previous one so that value is added, but we need to re print the variable.

# s1.replace("Python", "Java") in string will return the result as new string so that I can get the result but in list will not create new one so that it will get none.

# insert() :- It will add the element before the specified index

fruits.insert(1,"Kiwi")
print(fruits)


# extend()

fruits.extend(["Grapes", "Gawvava"])
print(fruits)
print(len(fruits))

fruits.append(["animal", "fruits"])
print(fruits)
print(len(fruits))

# remove() :- It will remove the first occurrence only.

fruits.remove("Kiwi")
print(fruits)

# pop()

fruits.pop(7)
print(fruits)

