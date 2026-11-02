"""
    >= 90, grade A
    80 and 89, grade B
    70 and 79, grade C
    60 and 69, grade D
    < 60, grade F

"""

# if-elif-else

mark = int(input("Enter you marks: "))

if mark >= 90:
    print(f"{mark} Scored, Grade A")
elif 80 <= mark < 90:
    print(f"{mark} Scored, Grade B")
elif mark >= 70 and mark < 80:
    print(f"{mark} Scored, Grade C")
elif mark >= 60 and mark < 70:
    print(f"{mark} Scored, Grade D")
else:
    print(f"{mark} Scored, Grade F")
