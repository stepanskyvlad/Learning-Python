# Objects
Mutable vs. Immutable:
- A mutable object can be modified after creation.
- Immutable objects are stuck in their creation state.

Mutable objects in Python:
list, dict, set

Immutable objects in Python:
string, tuple

In Python, the plus operator creates a new string containing the concatenated phrase, and binds the new object to the name of variable.

# Data Structures
Data Type - An attribute of data that describes the values it can have and how the data can be used.
## Primitive vs. Reference types
We also use the word object to describe a value in memory referenced by an identifier. Reference types reference their specific value from an address of where the item is stored rather than direct access to the data itself. This means if the address changes, the value the variable represents also changes. Again, it's important to remember that with reference types, we are adding this extra address layer whereas with primitive types, we directly access the data. This type of memory management is the foundation of data structures. Whether the tools needed to change pointers or access addresses are available to you or not depend on the programming language. Usually this is all abstracted to you and all you have to worry about is creating the string using a programming languages syntax. However, in some languages like C++ you have to manage these pointers and manage this memory in data. But in other languages like Java and Python, this memory management is handled for you.
### Primitive Types(Numbers, Characters, Booleans):
(variableName -> data)
- character
- boolean
- short
- int
- long
- float
- double

Numerical data type:
- Singed:
  - Positive and negative values;
  - Example: 16-bit short range: -32,768 to 32,767   
- Unsigned
  - Only positive values.
  - Example: 16-bit short range: 0 to 65,535

### Referenced Types:
(variableName -> memoryAddress -> value)
- Strings
- Other data Structures

## Data Structures
Data Structure - A collection with a defined way of accessing and storing items. "A container that holds data."
### Strings
Most programming languages have a data type called a string, which is used for data values that are made up of ordered sequences of characters, such as "hello world". A string can contain any sequence of characters, visible or invisible, and characters may be repeated.
### Arrays
Collection of elements, where each item is identified by an index or key.
Array can store elements of only one data type but List can store the elements of different data types too. Hence, Array stores homogeneous data values, and the list can store heterogeneous data values.
List cannot manage arithmetic operations. Array can manage arithmetic operations.
To use an array in Python, you'll need to import this data structure from the NumPy package or the array module.

'''python
array = np.array([3, 6, 9, 12])
division = array/3
print(division)
print (type(division))
'''
