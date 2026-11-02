import re

phone = "Alice-1234567890, Mark-9876556543, Carol-1290875673"

pattern = r"\d{10}"
match_obj = re.findall(pattern, phone)
print(match_obj)

pattern_compiled = re.compile(pattern)
# match_obj = re.findall(pattern_compiled, phone)
print(match_obj)
print(pattern_compiled)
print(type(pattern_compiled))


with open("student_details", "rt") as fh:
    data = fh.read()
print(data)
print(type(data))

phone_matches = re.finditer(pattern_compiled, data)
print(phone_matches)
for matches in phone_matches:
    print(matches)
    

