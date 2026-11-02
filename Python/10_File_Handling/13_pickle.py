"""
list, tuple, when we want to store the data types in the memory and files then we need to be converted into sequence
of bites that the computer can understand. -> this process is called serialization.

and when we want to access back these sequence from the file these sequence must be converted back into the original
data types -> this process of conversion is called deserialization.

"""

students = {"student1": {"roll": 101, "name": "John", "percent": 95.5},
            "student2": {"roll": 102, "name": "Carol", "percent": 92.5},
            "student3": {"roll": 103, "name": "Alice", "percent": 81.5}}

print(students)
print(type(students))

# writing it into the text file


# with open("student_info.txt", "wt") as fh:
#     fh.write(str(students))

# with open("student_info.txt", "rt") as fh:
#     for students in fh:
#         print(students)

import pickle

# serialization
with open("student_bin", "bw") as fh:
    for student in students:
        pickle.dump(students[student], fh)


# Deserialization

with open("student_bin", "rb") as fh:
    data1 = pickle.load(fh)
    print(data1, type(data1))
    data2 = pickle.load(fh)
    print(data2, type(data2))
    data3 = pickle.load(fh)
    print(data3, type(data3))
    # data4 = pickle.load(fh)   gives the error
    # print(data4, type(data4))


