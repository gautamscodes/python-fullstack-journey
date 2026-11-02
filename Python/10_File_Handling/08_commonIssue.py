# 1. First issue is to check the file name correctly otherwise it will give erorr.
# fh = open("practise3.txt", "rt")
# content = fh.read()
# fh.close()
# print(content)

# 2. Second issue is we can't write the file in the reading mode opened files. also not read when you open in another mode.
# wt mode when it will open then data will we deleted if you run the program.
fh = open("practise1.txt", "rt")
fh.write("some contents")
fh.close()

