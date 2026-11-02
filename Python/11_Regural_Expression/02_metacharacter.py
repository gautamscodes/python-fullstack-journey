# Metacharacter
import re

message = ("The current Python version is 3.13. Other"
           "previous version are 3.12, 3.11, 3.10.")

match_object = re.search("[0-9][0-9]", message)
match_object1 = re.search("[0-123456789][0-9]", message)

print(match_object)
print(match_object1)

match_object2 = re.search("[0-9][0-9]", "House number : 251/A")
print(match_object2)
message1 = "The year is 2011"
match_object3 = re.search("[0-9][0-9][0-9]", message1)
print(match_object3)
match_object4 = re.search("[0-9][.],[0-9][0-9]", message)
print(match_object)




