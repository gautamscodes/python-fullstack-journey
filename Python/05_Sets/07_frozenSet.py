# Normal Set

s1 = {1,2,4,0}
s1.add(-1)
print(s1, type(s1))

# Frozen Set --> Immutable set

fs1 = frozenset({10,20,30})
print(fs1, type(fs1))

fs2 = frozenset({10, 50, 100, 200})
print(fs2, type(fs2))

# Intersection
print(fs1 & fs2)

# Union
print(fs1 | fs2)

# difference
print(fs1 - fs2)


# Testing
s2 = set(fs1)
print(s2)

fs3 = frozenset(s2)
print(fs3)
print(len(fs3))

s2.add(11)
print(s2)
