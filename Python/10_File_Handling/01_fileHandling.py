# Opening a file in Python
# open (file_name, mode_to_open)
# Modes: r, x, w, a, t, b => rt are default modes

file_handler = open("practise.txt", 'rt')
print(file_handler)

# when we open the file we have to close the file also. if we not close the then data will corrupt.
# closing a file close()
file_handler.close()
print(file_handler)

# Read Operation
