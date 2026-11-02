# raise

salary = float(input("Enter salary: "))

if salary < 0:
    raise ValueError("Salary Cannot be negative!")
else:
    print(f"Your salary is {salary}")


# Raising Exception
age = int(input("Enter your age: "))

if age < 0:
    raise Exception("Age cannot be negative!")
else:
    if age >= 18:
        print("You can vote")
    else:
        print("You cannot vote")
