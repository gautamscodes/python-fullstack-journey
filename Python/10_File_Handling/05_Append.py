# 'a' mode => Append mode

fh = open("file2.txt", 'at')
fh.write("\nThis content has been written using 'a' mode.\n")
fh.write("'a' mod is used to add new content at the end of the file.\n")
fh.write("Good bye!")
fh.close()

# if the file does not exist, 'a' mode creates the file.
fh2 = open("file4.text", 'at')
fh2.write("\nThis content has been written using 'a' mode.\n")
fh2.write("'a' mod creates the file if not already existing.\n")
fh2.write("Good bye!")
fh2.close()