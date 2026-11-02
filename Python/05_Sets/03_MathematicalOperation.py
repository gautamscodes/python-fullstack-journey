student1 = {"English", "Maths", "CS", "Chemistry", "Physics"}
student2 = {"English", "Biology", "Chemistry", "Physics"}
student3 = {"Sanskrit", "Maths", "English"}
# print(student1, type(student1))
# print(student2, type(student2))

# common Subjects from student1 and Student2
# intersection () // &

common_sub = student1.intersection(student2)
print(common_sub)

common_sub2 = student1 & student2
print(common_sub2)

common_sub3 = student1.intersection(student2, student3)
print(student3)

# all subjects of student1 and student2
# union() // |

all_subjects = student1.union(student2, student3)
print(all_subjects)

all_subjects2 = student1 | student2 | student3

# difference

days = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}
weekends = {"Sat", "Sun"}

weekdays = days.difference(weekends)
print(weekends)
