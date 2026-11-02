# Python Basic

## What is Python 

-   Medium to communicate with computer.
- Keywords/ reserved words - example - if, for, else, while, return, ....
- Syntax - set of rules.

## What is Literals?

- That data involved in the program is called literals.
- example :- name - "Gautam", age = 22 then Gautam and 22 is literals.
- There are some type of literals
  - Numeric literals
    - integer literals
    - float literals
    - 
  - String literals 
    - It is used for storing name, characters
    - It is sequence of characters, and it must be written inside the quotes like single, double and triple quotes.
    - example :- 'hello', "Hello", '''Hello''', these three are valid.
    - String literals can a sentence as well.
    - example :- "Hello I am Gautam Kumar" this is also valid.
    - triple quotes are used for writing the code in multiple lines and also used for the making multiple comments in the python.
  - Boolean literals
    - Boolean literals are used when I have to check the condition.
    - True / False 
    - T and F are capital letter.
  - None literals
    - It is representing as no any value none value.
    - If you don't have any data for some cases then we use none literals.

## Variables in Python

- Variables are the reserved memory location.
- It is container that's store some actual value.
- example :- a = 1, print(a), age = 22 print(age)
- Exception to Variable
  - Begins with alphabet and underscore
  - it follows the Pascal rules, --> First letter must be capital
  - It should not start with number.
  - if you have to separate the variable using underscore.

## Keywords in Python

- It is special reserved words.
- variable should not be a keywords name.
- example :- for, while, break, continue, def, lambda, and, or, not, Ture, False, None these are the keywords in the python.
- If you want to see the keywords in the python do these steps.
- import keyword  --> print(keyword.kwlist)

## Datatypes in Python

1. Primitive Datatypes
   1. Integers
   2. Float
   3. String
   4. Boolean
   5. None
2. Non-Primitive Datatypes
- Python is Dynamically typed so that it will allocate the data types in Runtime.
- Using type function we can check type of datatypes in python.

### Basic Operation in Strings

- concatenation using + operators it will works on String.
- Finding the length using len function
- indexing in the string. we can also work with negative indexing.
- Joining the string together.
- index start with 0th position "python" = 012345
- indexing will start with square brackets.

## Type Conversion and Type Casting.

- Type Conversion and Type Casting in Python.
- if we convert int to float then it will convert easily we called as implicit conversion.
- if we convert float to int then it will convert force fully by defining the data types infront of the variable is called Explicit conversion.
- It is possible to convert integer or float to String.
- But it is not possible to convert string to float or integer when in variable it will stores the character values. If it is sotres any integer value then it possible to convert.
- only concatenate string not string or integer or float.
- boolean is also typecasting into string, float and integer but if you put (0 or 0.0 and '') then it will be False.
- (0.5) will be True. also (' ') is also give True.
- Empty string, zero and zero point zero and None will not convert into bool it gives False.


## Operators in Python

- Operators are some symbols that performs some operations.
- eg :- =, +, -, *, /
1. Arithmetic Operator
   1. +, -, *, /, //, **, % these are the Arithmetic operator.
   2. flore division will return integer value
   3. Normal division will return the float value also if possible division.
   4. %, Operator gives us the 
2. Assignment Operator
   1. =, single equal to is assignment operator
   2. It is used for set the value to the left side of variable.
   3. eg :- =, +=, -+, *=, /=, it will operate with 1
3. Relational Operator
   1. It is used for checking the equality between two or more operands
   2. eg:- ==, !=, >, <, <=, >=
   3. It is always return the True or False only it means return boolean value.
   4. 
4. Logical Operator
   1. It is also work with boolean values it means also return True and False.
   2. and, or in python is used for the logical operators.
   3. short circuit --> in the case of and --> one part is False then it will not check the second part and return the result as False only.
   4. short circuit --> in the case of or --> one part is True then it will not check the second part and return the result as True only.

### Precedence and Associativity

- It is a rule to perform some operation on the basis of their precedence.
- and perform first then or will be.

### Classification of Operators based on the number of operands
1. Unary Operator
   -  The Operator that operates on single operator is called Unary Operator.
   - (-10) is the unary operator.
2. Binary Operator
   - The Operator that operates on double operator is called Binary Operator.
   - (10 - 5) is the binary operator.
3. Ternary Operator
   - The Operator that operates on triple operator is called Ternary Operators.
   - it is involved in if else part.

## Print Function

- using print() we can print the anything on the console.
- name = "Gautam" print(name)
- age = 22 print(name, age)
- print(10,20,30,40) it is also valid. it will print with space by default.
- we can change the separator in print() function.
- print(10,20,30,40, sep=",") use (sep = ",")
- print(10,20,30, sep="hi")

## Taking input

- input() it is used for taking the input from the user.
- By default, it will take the value as string. 
- so if we want to take the value as integer then we have to type cast into int or any data type we want.
- 