correct_password = "Python"

while True:
    user_password = input("Enter you Password: ")
    if user_password == correct_password:
        print("Password is correct! Congrats.")
        break
    else:
        print("Wrong Password, try again.")
print("Logged in!")

# Ascending order
num = 10

while num <= 20:
    print(num, end=" ")
    num = num + 2
print()

# Descending order
nums = 20
while nums >= 10:
    print(nums, end=" ")
    nums = nums - 2
