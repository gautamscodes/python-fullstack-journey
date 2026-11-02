# open the file manually without with
fh = open("practise.txt", "rt")
contents = fh.read()
fh.close()
print(contents)

# Using with statements it will auto close the file also.

with open("practise.txt", "rt") as fh:
    content = fh.read()

print(content)


# with open("practise1.txt", "xt") as fh:
#     fh.write("New creation using with\n")
#     fh.write("Bye")

with open("practise1.txt", "at") as fh:
    fh.write("\nNew Creation using with in at\n")
    fh.write("Good Work")

