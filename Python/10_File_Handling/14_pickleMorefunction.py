import pickle

students = {"student1": {"roll": 101, "name": "John", "percent": 95.5},
            "student2": {"roll": 102, "name": "Carol", "percent": 92.5},
            "student3": {"roll": 103, "name": "Alice", "percent": 81.5}}

print(students)
print(type(students))

# Serialization
with open("student.bin", "bw") as fh:
    for student in students:
        pickle.dump(students[student], fh)


# Deserialization

# with open("student.bin", "rb") as fh:
#     while True:
#         try:
#             data = pickle.load(fh)
#             print(data, type(data))
#         except EOFError:
#             print("Done!")
#             break

# Print the names of the students who secured 90 or more percent
# with open("student.bin", "rb") as fh:
#     while True:
#         try:
#             data = pickle.load(fh)
#             if data['percent'] >= 90:
#                 print(data['name'])
#         except EOFError:
#             print("Done!")
#             break


# Print the names of the students as a list who secured 90 or more percent
student_list_90 = []
with open("student.bin", "rb") as fh:
    while True:
        try:
            data = pickle.load(fh)
            if data['percent'] >= 90:
                student_list_90.append(data['name'])
        except EOFError:
            print("Done!")
            break

print(f"list of students who secured 90 or more are: {student_list_90}")
