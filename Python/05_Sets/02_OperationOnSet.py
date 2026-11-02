from calendar import week

nums = {1,2,3,0,-1}
nums2 = {3,5}

# Membership operator - in, not in
print(0 in nums)
print(10 in nums)
print(10 not in nums)

# Type conversion

weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
weekdays = set(weekdays)
print(weekdays)
print(type(weekdays))

# sets are mutable.
set1 = {2,0,-1}
# set[0] = 10

# using function and method we can add the value in the set.
# add()
set1.add(5)
print(set1)

# remove()
set1.remove(0)
print(set1)

# discard()
set1.add(0)
print(set1)

set1.discard(0)
print(set1)
set1.discard(10)
print(set1)

