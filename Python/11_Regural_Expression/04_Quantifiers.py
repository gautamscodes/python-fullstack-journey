# Quantifiers => are symbols that are used for quantities.
# {4}
import re

message = "The current Python version is 3.13. Other previous are 3.12, 3.11, 3.10."

pat = r"[a-z]{4}"
match_obj = re.search(pat, message)
print(match_obj)

pat = r"[A-Z][a-z]{5}"
match_obj = re.search(pat, message)
print(match_obj)

pat = r"[A-Z][a-z]{2,5}"
match_obj = re.search(pat, message)
print(match_obj)

# + => matches 1 or more repetition of the previous pattern
pat = r"[A-Z][a-z]+"
match_obj = re.search(pat, message)
print(match_obj)

# ? => 0 or 1 repetition of the previous pattern.
pat = r"[A-Z][a-z]?"
match_obj = re.search(pat, message)
print(match_obj)

# * => 0 or more repetition of the previous pattern.
pat = r"[A-Z][a-z]*"
match_obj = re.search(pat, message)
print(match_obj)

