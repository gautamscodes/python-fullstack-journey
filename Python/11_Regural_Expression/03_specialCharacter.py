import re

s1 = "Python is a programming Language. python3.13i s th current version."

# [A-Z], [a-z] => it will match the characters consutive to it.

pat = r"[A-Z][a-z][a-z]"
match_obj = re.search(pat,s1)
print(match_obj)

# \d and \D
# \d matches 1 digit character. It is similar to [0-9].
pat = r"[a-z][a-z][a-z]\d"
match_obj = re.search(pat, s1)
print(match_obj)

# \D matches 1 non-digit character. It is similar to [0-9]
pat = r"[a-z][a-z][a-z]\D"
match_obj = re.search(pat, s1)
print(match_obj)

s2 = """Hi there
We are learning Python
"""

# \s, \S
# \s matches any whitespace character, tab and new line character as well.
pat = r"[a-z][a-z][a-z]\s"
match_obj = re.search(pat,s2)
print(match_obj)

# \S => opposite of \s. It matches any character except, space, \n and \t.
pat = r"[a-z][a-z][a-z]\S"
match_obj = re.search(pat, s2)
print(match_obj)

# \w - matches [a-z], [A-Z], [0-9], -
pat = r"[a-z][a-z][a-z]\w"
match_obj = re.search(pat, s2)
print(match_obj)

# \W => opposite to \w -> matches a character except [a-z], [A-Z], [0-9], _
pat = r"[a-z][a-z][a-z]\W"
match_obj = re.search(pat, s2)
print(match_obj)

