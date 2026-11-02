# How to read the files
# Read Operation
# read() => read function reads the contents of the file as str

file_handler = open("practise.txt", "rt")

# read operation

content = file_handler.read()

# file_handler.close()

print(content)
print(type(content))


# read some certain number of contents then we use
file = open("practise.txt", "rt")
line1 = file.read(10)    # this will read first 10 characters of the file.
print(f"Line 1: {line1}")

# readline()
line2 = file.readline()
print(f"Line 1: {line2}")

line3 = file.readline()
print(f"Line 2: {line3}")

line4 = file.readline()
print(f"Line 3: {line4}")

line5 = file.readline()
print(f"Line 4: {line5}")
print(type(line5))

# readlines()
content = open("practise.txt", "+rt")
lines = content.readlines()
print(f"Lines : {lines}")
print(type(lines))

for line in lines:
    print(line)

