# One Way to write the try catch.
try:
    with open("practise3.txt", "rt") as fh:
        data = fh.read()
    print(data)
except FileNotFoundError:
    print("The File that you are trying to open does not exists!")

print("==================================================================")

# Another way to write the try catch program.

try:
    with open("practise3.txt", "rt") as fh:
        data = fh.read()
    print(data)
except FileNotFoundError as file_err:
    print("The File that you are trying to open does not exists!")
    print(file_err)

print("==================================================================")

# else block => it is fall back option. it will run when exception is not running.

try:
    with open("practise.txt", "rt") as fh:
        data = fh.read()
except FileNotFoundError as file_err:
    print("The File that you are trying to open does not exists!")
    print(file_err)

else:
    print(data)

print("==================================================================")

# finally () => it will always run

try:
    fh = open("file10.txt", "rt")
    data = fh.read()
    fh.close()
except FileNotFoundError as file_err:
    print("The File that you are trying to open does not exist!!")
    print(file_err)
else:
    print("else block")
    print(data)
finally:
    print("Finally block")

print("==================================================================")

import io

try:
    fh = open("file10.txt", "wt")
    data = fh.read()
    fh.close()
except FileNotFoundError as file_err:
    print("The File that you are trying to open does not exist!!")
    print(file_err)
except io.UnsupportedOperation as io_err:
    print(io_err)
else:
    print("else block")
    print(data)
finally:
    print("Finally block")

print("==================================================================")

try:
    fh = open("file10.txt", "wt")
    fh.write("Hello")
except FileNotFoundError as file_err:
    print("The File that you are trying to open does not exist!!")
    print(file_err)
except io.UnsupportedOperation as io_err:
    print(io_err)
else:
    print("else block")
    # print(data)
finally:
    print("Finally block")
    fh.close()

print("==================================================================")

try:
    fh = open("file10.txt", "wt")
    fh.write("Hello")
except FileNotFoundError as file_err:
    print("The File that you are trying to open does not exist!!")
    print(file_err)
except io.UnsupportedOperation as io_err:
    print(io_err)
finally:
    print("Finally block")
    fh.close()

print("==================================================================")
