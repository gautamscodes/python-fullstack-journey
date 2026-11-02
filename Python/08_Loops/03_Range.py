# Range()

for i in range(1,10):
    print(i, end=" ")
print()

# reverse order --> 20 to 10 (exluding 10) only even

for i in range(20,10, -2):
    print(i, end=" ")
print()
# Countdown from 10 to 1 (1 included)

for i in range(10, 0, -1):
    print(i, end=" ")
print()
print("Happy New Year!")

# without step bydefault 1

for i in range(1, 5):
    print(i, end=" ")
print()

for i in range(5):
    print(i, end=" ")
print()


groceries = ['salt', 'milk', 'sugar']

for item in groceries:
    print(item, end=" ")
print()

for index in range(len(groceries)):
    print(index, end=" ")
print()


profits = [9, 11, 6, 10]
# Profit of quarter 1 is 9
# Profit of quarter 2 is 11
# Profit of quarter 3 is 6
# Profit of quarter 4 is 10

for index in range(len(profits)):
    q = index + 1
    print(f"Profit for quarter {q} is {profits[index]}")
    

