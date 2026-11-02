# Dictionary in Python

## Dictionary

- It is data structure.
- It have key-value pair, comma separated key-value paris encloded within {}
- {Key1:value1, key2:value2,......}
- dictionary does not support indexes
- dictionary are mutable


## Operation on dictionary

- get() it is used to access the value from the dictionary
- if keys is not available then it will not give any error while accessing. it gives None.
- If we want to access normally then it will give the error.
- We can use it default value if any keys are not available ex: dic.get('phone', 989998) these are the key value that are not available on the dictionary so it will print 989998.
- Membership operator will also find the key not value.
- if we check with in operator with value then it will return false.
- Keys cannot be duplicate in dictionary.
- two time key will not store but their value will be updated to the recently used.

## Working with Keys and Values

- Keys are allowed in dictionary is  string, integer, float, bool, tuple.
- Keys are not allowed in dictionary is list, set, dict
- list,set,dict are mutable so that it is not allowed as key in dictionary.
- String, int, float, bool, tuple is immutable. so that keys of the dictionary can only be immutable data types only.
- For Values can be data types.
- values can be list, dictionary

## Shallow Copy and Deep Copy

- Shallow copy means it will copy the outer list but not copy the internal list.
- ex:- [10, 20, 30, [1, 2, 3], 6] if we copy as shallow copy then it will copy and if we want to change outer list value then it will reflect on the copy items also. But if we try to change the internal list then it will not reflect to the copy one. because it is created using copy.copy() function.
- import copy --> it's a module to copy the data as shallow copy and deep copy.
- Deep copy means, when we change either internal or external list then it will reflect on the another one also.
- 