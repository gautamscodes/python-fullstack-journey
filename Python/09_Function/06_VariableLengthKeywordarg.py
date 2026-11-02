# **kwargs

def fun(**kwargs):
    print(kwargs, type(kwargs))

fun(x=10, y =20)

def student_details(sid, sname, **marks):
    if len(marks) == 0:
        print(f"{sname} did not attend the exam.")
    else:
        percent = sum(marks.values()) / len(marks)
        print(f"{sname} with id {sid} secured {percent}")

student_details(101, "John", sub1 = 78.5, sub2 = 81.0, sub3 = 90.5)
student_details(102, "Carol", sub4 = 78.0, sub2 = 88.5, sub1 = 90.5, sub3 = 89.6)
print()


def student_details(sid, sname, *extra, **marks):
    if len(marks) == 0:
        print(f"{sname} did not attend the exam.")
    else:
        percent = sum(marks.values()) / len(marks)
        print(f"{sname} with id {sid} secured {percent}")

    print(f"{sname} does {extra}")

student_details(101, "John", "Football", sub1 = 78.5, sub2 = 81.0, sub3 = 90.5)
student_details(102, "Carol","Tennis", "debates", sub4 = 78.0, sub2 = 88.5, sub1 = 90.5, sub3 = 89.6)
