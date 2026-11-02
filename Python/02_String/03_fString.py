name = "John"
age = 20
language = 20
hours = 3

# print --> john is 20 years old.

print(name, "is", age, "years old.")

# print --> john is 20 years old. He studies Python 3 hours a day.

print(name, "is", age, "years old. He studies", language, hours, "hours a day")

# Using f string.
print(f"{name} is {age} years old. He studies {language} {hours} hours a day.")


sub1 = 78
sub2 = 87
sub3 = 83

# John scored {} marks
print(f"{name} scored {sub1 + sub2 + sub3} marks in total.")

percent = (sub1 + sub2 + sub3) / 3
print(f"{name} got {percent}%.")


