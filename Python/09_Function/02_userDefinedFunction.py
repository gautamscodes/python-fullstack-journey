# user-define function

def greeting_someone():
    print("Hello, good morning!")
    print("It's a beautiful day.")

# Calling a function
greeting_someone()
# greeting_someone()
# greeting_someone()

# Arguments :- some value we paas inside the function.

def greet(name):
    print(f"Radhe Radhe {name}, Hare krishna!")
    print(f"Kaise ho Aap {name}.")

greet("Siddhant")
greet("Gautam")
greet("Radhe")


def even_odd(number):
    if number % 2 == 0:
        print(f"{number} is Even.")
    else:
        print(f"{number} is Odd.")

# calling the function

even_odd(50)
even_odd(49)


def add(num1, num2):
    result = num1 + num2
    print(f"Result : {result}")

add(10,3)
add(9, -5)
