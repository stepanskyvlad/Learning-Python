# Built-in Objects
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

# Data Structures
Data Structure - A collection with a defined way of accessing and storing items. "A container that holds data."
## Strings
Most programming languages have a data type called a string, which is used for data values that are made up of ordered sequences of characters, such as "hello world". A string can contain any sequence of characters, visible or invisible, and characters may be repeated.
## Arrays
Collection of elements, where each item is identified by an index or key.
Array can store elements of only one data type but List can store the elements of different data types too. Hence, Array stores homogeneous data values, and the list can store heterogeneous data values.
List cannot manage arithmetic operations. Array can manage arithmetic operations.
To use an array in Python, you'll need to import this data structure from the NumPy package or the array module.

```python
import numpy as np

array = np.array([3, 6, 9, 12])
division = array/3
print(division)
print (type(division))
```
#### Multidimensional Arrays
Multidimensional Array concept can be explained as a technique of defining and storing the data on a format with more than two dimensions (2D). In Python, Multidimensional Array can be implemented by fitting in a list function inside another list function, which is basically a nesting operation for the list function. Here, a list can have a number of values of any data type that are segregated by a delimiter like a comma. Nesting the list can result in creating a combination of values for creating the multidimensional array.
```python
List = [ [1, 3, 5], [8, 5, 6], [7, 1, 6] ]
#or
# at first we will create an array of c columns and r rows
c = 4
r = 3
arr = [[0] * c for i in range(r)]
# loop will run for the length of the outer list
for i in range(r):
# loop will run for the length of the inner lists
    for j in range(c):
        if i < j:
            arr[i][j] = 8
        elif i > j:
            arr[i][j] = 4
        else:
            arr[i][j] = 7
for r in arr:
    print( ' '.join([str(x) for x in r] ) )
```
Numpy Multidimensional Arrays
```python
import numpy as nmp
X = nmp.array( [ [ 1, 6, 7],
                 [ 5, 9, 2],
                 [ 3, 8, 4] ] )
print(X[1][2]) # element at the given index i.e. 2
print(X[0])     # first row
print(X[1])      # second row
print(X[-1])     # last row
print(X[:, 0])  # first column
print(X[:, 2])  # third column
print(X[:, -1]) # last column
```
#### Jagged arrays
A jagged array can have elements of different dimensions and sizes.
For example, with jagged array, the number of columns is not fixed, meaning the inner arrays can be any length we'd like.

Array Operations:
- Calculate item index: O(1)
- Insert or delete item at beginning: O(n)
- Insert or delete item in middle: O(n)
- Insert or delete item at end: O(1)
## Linked Lists
A linked list is a sequence of data structures, which are connected together via links. Linked List is a sequence of links which contains items. Each link contains a connection to another link. Linked list is the second most-used data structure after array.
- Collection of data elements, called nodes
- Contain reference to the next node in the list
- Hold whatever data the application needs
- Elements can be easily inserted and removed
- Underlying memory doesn't need to be reorganized
- Can't do constant-time access
- Item lookup is linear in time complexity: O(n)

Also, there are doubly linked list. Each data item has a reference to both the previous and next items that are its neighbors.

Pros and cons:
- Access: first item - O(1), last item - O(n).
- Update: O(N) in the worst cases
- Insert: first item - O(1), in the back of the list - O(N)
- Search: O(N) in the worst cases
- Delete: O(N) in the worst cases

Merge sort is typically preferred for linked lists.
## Stacks and Queues
*_Stacks_* operate on a principle called "last in, first out or LIFO". 
When adding an item to the stack, we use the terminology 'push'. When removing an item we use the word pop.

Pushing and popping elements - O(1)

*_Queues_* operate on a principle called "first in, first out or FIFO". Enqueue is when an item is added to a list. Dequeue is when an item is removed from the list.
peek() - see the first item in the queue without removing it.

To enqueue or to dequeue an element - O(1)

Using:
- Stack
  - Expression processing
  - Backtracking: browser back stack, for example
- Queue
  - Order processing
  - Messaging
## Hash-Based Data Structures
**Associated array rules:**
- Key-value pairs are bound together
- Each key must be unique
- Order isn't important
- Values are accessed with the key
- Value do not need to be unique.

Pros:
- Search: O(1)
- Insertion: O(1)
- Deletion: O(1)

A *_hash table_* is an implementation of the associative array abstract data structure.
For small datasets, arrays are usually more efficient. Hash tables don't order entries in a predictable way.
```python
states_to_capital = {}

states_to_capital['Texas'] = 'Austin'
states_to_capital['New York'] = 'Albany'

print(states_to_capital['New York'])
```
## Trees and Graphs
Similar to linked lists, hash maps, and other data structures, a **set** is an abstract data type.
Set is:
- A collection of unique items.
- Order doesn't matter.
- None of the elements are duplicated.

We use sets when we want to check if a certain value exists in our container.
```python
primary_colors = frozenset(['red', 'blue', 'yellow'])

color = 'green'

if color.lower() in primary_colors:
    print(color + " is a primary color")
else:
    print(color + " is not a primary color")

letters = {'a', 'b'}
letters.add('c')
print(letters)
```
Binary Search Tree: maintain sorted order while staying fast for insertion, deletion, and accessing: for Balance tree - O(log(N))

Heaps - great for priority queues:
- Find min/max: O(1)
- Insert: O(log(N))
- Search: O(N)
- Delete: O(N)

Search information about heaps, tree data structures, graphs
