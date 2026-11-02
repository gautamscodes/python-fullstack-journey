import re
from idlelib.pyshell import restart_line

# sub()
s1 = "Sunday, Monday, Tuesday, Monday, Sunday "

pat = "Sunday"
replacement = "Friday"

result = re.sub(pat, replacement, s1)
print(result)

# sub() in count()

result = re.sub(pat, replacement, s1, count=1)
print(result)

pat2 = "S[a-z]+"
result = re.sub(pat2, replacement, s1)
print(result)


message = ("We are learning re. Using RE, we can search for a pattern in a given string."
           "Using the sub(), we can replace the pattern with a given string as well.")

patt = r'\bre\b'
replacement = "Regular Expression"
result = re.sub(patt, replacement, message)
print(result)

patt = r'\bre\b'
replacement = "Regular Expression"
result = re.sub(patt, replacement, message, flags=re.IGNORECASE)
print(result)

phone_nums = "+91-1234567890, +91-9999999999"
pattern = r"[+-]"
replacement = " "
result = re.sub(pattern, replacement, phone_nums)
print(result)
