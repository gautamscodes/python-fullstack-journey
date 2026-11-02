student1 = {"English", "Maths", "CS", "Chemistry", "Physics"}
student2 = {"English", "Biology", "Chemistry", "Physics"}
student3 = {"Sanskrit", "Maths", "English"}
# print(student1, type(student1))
# print(student2, type(student2))

all_subs = student1 | student2 | student3
print(all_subs)