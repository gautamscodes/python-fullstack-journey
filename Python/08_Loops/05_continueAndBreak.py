# Continue

for num in range(10):
    if num % 3 == 0: # if the number is divisible by 3
        continue
    print(num, end=" ")

# Break

for num in range(1, 10):
    if num % 3 == 0:
        break
    print(num)

