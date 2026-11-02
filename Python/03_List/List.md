# List in Python

## List

- List is data structure in python which is used to store collection of data.
- It can store any type of date on it.
- List are sequence of any data.
- List are ordered so that we can access through index.
- for access the value of list we use index like string.
- It also follows the +ve and -ve indexing in the list.
- finding the length of the list using len function.
- If we try to fetch the value that have no any index then it will give error index of range.

## List Operation

### Slicing 

- List support slicing through that we can fetch the value from the list.


### List Methods

1. append() It is a method which is used to add the element at last.
  - syntax : fruits.append("Mango") it will add mango to end of the list existing list.
  - if we try print(fruits.append("orange")) then it will return None because list is mutable.
2. insert() :- It will add an element before teh specified index.
   - syntax:- list.insert(index, item)
   - ex:- fruits.insert(_index: 2, _object:"Banana")
3. extend() :- It is also added the list at the last. It will add multiple element at a time in the existing list.
   - It also add another list inside the existing list.
   - ex :- list.extend(["Banana", "Grapes"])
4. remove() :- It is used to remove the elements from the list.
   - It will remove only the first occurrence it means very first element it will remove if duplicate is existing.
   - 
5. pop() :- It is also used to delete the element from the existing list.
    - It will take the index to delete the elements.
    - syntax :- list.pop(2)
    - If we give the index value then it will delet that element but if we not giving any index value then it will always delete the last element form the list.
   
### Sorting Methods in list

1. reverse()
2. sort()
3. count()
4. membership operation.