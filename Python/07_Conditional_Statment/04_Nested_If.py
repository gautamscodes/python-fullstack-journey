# Nested If

"""
    if marks >= 60, student is Pass else
    student is Fail.

    and the student is Pass, then we print
    grade.

    >= 90, grade A
    80 and 89, grade B
    70 and 79, grade C
    60 and 69, grade D
    < 60, grade F

"""
marks = int(input("Enter your marks: "))

if marks >= 60:
    print("Congrats, you have passed the exam!")
    if marks >= 90:
        print("Your Grade is A")
    elif 80 <= marks < 90:
        print("Your Grade is B")
    elif 70 <= marks < 80:
        print("Your Grade is C")
    else:
        print("Your Grade is D")
else:
    print("You have to failed, study hard next time")