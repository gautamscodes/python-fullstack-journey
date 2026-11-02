# W mode :- it is used for open to file for writting. Overwrite the file content.
# if file is exist then we can do
fh = open("file2.txt", "+wt")
fh.write("This file is Overwritten using 'w' mode in python.\n")
fh.write("Have a nice day!")
fh.close()


# if file is not exist then w mode create first after that write it on that file.
fh = open("file3.txt", "+wt")
fh.write("This file is created using 'w' mode in python.\n")
fh.write("Have a nice day!")
fh.close()
