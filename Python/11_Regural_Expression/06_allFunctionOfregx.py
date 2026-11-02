import re

# match()
s1 = "We are learning regx in Python"
pat = r"[A-Z][a-z]"
match_obj = re.match(pat,s1)
print(match_obj)

pat = r"[a-z]{3}"
match_obj = re.match(pat,s1)
print(match_obj)

phones = "John-1234567890, Carol-9876545678, Mark-9087654321, Alice-45876877, Dan-123456789987654321"

pat = r"[0-9]{10}"
match_obj = re.search(pat,phones)
print(match_obj)

# findall()
pat = r"[0-9]{10}"
match_obj = re.findall(pat,phones)
print(match_obj)

pat = r"[0-9]+"
match_obj = re.findall(pat,phones)
print(match_obj)

# fetch all phone numbers. the phone numbers are exactly 7 digits and should not exceed as 15 digit.

pat = r"[0-9]{7,15}"
match_obj = re.findall(pat,phones)
print(match_obj)

# fetch all phone numbers. the phone numbers are at least 7 digits.

pat = r"[0-9]{7,}" # 7 or more
match_obj = re.findall(pat, phones)
print(match_obj)

# \b - avoid boundary
# fetch all phone numbers. the phone number are exactly 7 digits and should not exceed 15.
pat = r"\b[0-9]{7,15}\b"
match_obj =re.findall(pat, phones)
print(match_obj)

# finditer() it also find the all the occurance.
pat = r"\b[0-9]{7,15}\b"
match_obj_iter =re.finditer(pat, phones)
for matches in match_obj_iter:
    print(matches)
    
