import copy

l1 = [1, 2.5, [10,20,30], 'Python']

# Shallow Copy

l2 = copy.copy(l1)
print(l2)
print(id(l1))
print(id(l2))

l1[0] = 100
l1[2][0] = 50
print(l1, id(l1))
print(f"l2 -> {l2}", id(l2))

# deep Copy
l3 = copy.deepcopy(l1)

l1[0] = 5
l1[2][0] = 60
print(f"l1 -> {l1}", id(l1))
print(f"l3 -> {l3}", id(l3))

d1 = {"id":1111, "name": "John", "marks":{"eng":71.5, "maths":91.5, "bio":80.0}}

# shallow Copy
d2 = copy.copy(d1)

d1['name'] = 50
d1['marks']['maths'] = 92.0
print(f"d1 -> {d1}", id(d1))
print(f"d2 -> {d2}", id(d2))

# deep copy
d3 = copy.deepcopy(d1)
print(f"d3 -> {d3}", id(d3))
