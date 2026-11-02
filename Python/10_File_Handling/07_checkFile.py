# Checking file exist or not

# os.path.exists() => it is part of os module. it will find the file are exist or not.

import os

file_name = "practise1.txt"

if os.path.exists(file_name):
    print("File exists.")
else:
    print("File does not exist")

# finding the file using full path.
# we have to convert forward slash to the backward slash here, or we can also simply put r -> row string. or double forward slash.
file_name2 = "D:\\Learning\\Python Full Stack\\Python\\10_File_Handling\\practise1.txt"

if os.path.exists(file_name2):
    print("File exists.")
else:
    print("File does not exist")

# pathlib.Path.existes()

from pathlib import Path

file_name2 = Path("D:\\Learning\\Python Full Stack\\Python\\10_File_Handling\\practise1.txt")

if file_name2.exists():
    print("File exists.")
else:
    print("File does not exits.")


# if file is not exists then it will creates.

file_name2 = Path("D:\\Learning\\Python Full Stack\\Python\\10_File_Handling\\practise1.txt")

if file_name2.exists():
    print("File exists. Cannot create!")
else:
    print("File does not exits, creating it")
    fh = open(file_name2, 'xt')
    fh.write("some content")
    fh.close()