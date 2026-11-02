# x mode => create a file

fh = open("file2.txt", "+xt")
# when we create the file we can also write some contents
# write into a file
# write(content)

fh.write("This file is created using the 'x' mode in Python. \n")
fh.write("Next Line.")

# after write the content we have to close the file also
fh.close()
fh.write("Test content")

