# Filter => filter(function, sequence)

seq = [1,2,3,4]
odd = lambda x:True if x % 2 != 0 else False
filtered_output = filter(odd, seq)
print(filtered_output)  # we need to convert it into the sequence like list, tuple etc.
print(list(filtered_output))

# Map => map(function, sequence)

mapped_output = map(lambda x:True if x % 2 != 0 else False, seq)
print(mapped_output)
print(list(mapped_output))

mapp = map(lambda x: x ** 2, seq)
print(list(mapp))


