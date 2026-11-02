# JSON => JSON is used for api storage.

import json

students = {"student1": {"roll": 101, "name": "John", "percent": 95.5, "sports": False},
            "student2": {"roll": 102, "name": "Carol", "percent": 92.5, "sports": False},
            "student3": {"roll": 103, "name": "Alice", "percent": 81.5, "sports": True}}

print(students)
print(type(students))
print("=============================================")

# dump() => It is used for stor the data into the JSON file.
# with open("student_data.json", "xt") as fh:
#     json.dump(students, fh)

print("=============================================")

# dump() with indent = 4

with open("student_data.json", "wt") as fh:
    json.dump(students, fh, indent= 4)

print("=============================================")

# load()
#
# with open("student_data.json", "r") as fh:
#     data = json.load(fh)
#
# print(data)
# print(type(data))

print("=============================================")

# update()
try:
    # read the old data from the JSON file after loading use json.update()

    with open("student_data.json", "r") as fh:
        data = json.load(fh)
except FileNotFoundError:
    with open("student_data.json", "w") as fh:
        json.dump(students, fh, indent=4)
else:
    # update Operation
    data.update(students)
    # dump => write the updated data in the JSON file
    with open("student_data.json", "w") as fh:
        json.dump(data, fh, indent=4)



# for updation we have to read the data after that


