import random
from random import choice

# random() - returns random float between 0.0 and 1.0 (excluded)

print(random.random())
print(random.random())

# randint(a,b) => returns random int between a and b (both included)
print(random.randint(10,15))

nums = [10,4,1,8,4,3]
# choice(sequence) => return a random item from the sequence.
print(random.choice(nums))

fruits = ["Apple", "Orange", "Mango"]
print(choice(fruits))

# shuffle(sequence) => returns the elements shuffled in random order.
random.shuffle(fruits)
print(fruits)



