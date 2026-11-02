# File Handling

- In python basically file handling is classified in two ways 
  1. Text file
     - It stores the data in the form of characters
  2. Binary File
     - It stores the data in the form of binary 8 bytes like images, audio and videos files are binary files
- We can perform the action like read the file, write, add the file, overwrite the file, delete the file
- To open the file in python - we have open function open(). it takes the file as string take as modes ways : r, x, w, a -> r - read, x - edit a file, w - write, a - appending the file.
- t, b -> t open the file in text mode and b open the file in binary mode.
- r -> r open the file in the read mode.
- w -> w open the file in the write mode.
- x -> open the file in the edit and create the file.
- a -> open the file in append mode.
- Whenever we open the file we have to close the also. if we're not doing then file may be corrupt.
- to close the file we use close() function.
- Once the file is closed then we can't do any read and write operation on it.

## Exception Handling

- In python there is two type of Errors 
  1. Compile Time Error
     - It is occurred when any syntax or wrong code are there.
  2. Run Time Error
     - It is occurred when the program is run it means it will give the error on run time.
     - It is also known as Exception Error.
     - It is handled by the try, except in error handling in python.
     - For Handling the file at least one try and except must be used.
     - There are is another keyword are also there that is else and finally
     - else is used when except will not work then else part is executed.
     - finally is always executed.
     - else and finally are optional we can use or may be not used but try except at least one time we have to use to handle the error.