# Algorithms
#### 1. Brute Force (Linear Search, Selection Sort)
#### 2. Divide and Conquer (Merge Sort, Binary Search)
#### 3. Dynamic Programming (Up-bottom and and bottom-up)
#### 4. Greedy Algorithms (for optimization)
#### 5. Backtracking (Branch and Bound)
#### 6. Local Search
#### 7. Transform and Conquer
# Understanding Algorithm Performance
**Big-O Notation** is a way of expressing an upper bound on the execution time or space requirements of an algorithm.

- Measure how an algorithm responds to dataset size
- Big-O notation
  - Classifies performance as the input size grows
  - "O" indicates the order of operation: time scale to perform an operation
- Many algorithms and data structures have more than one Big O
  - Inserting data, searching for data, deleting data, etc.
##### Common Big-O Terms
![](img1.png)

- O(n^3) - Cubic
- O(2^n) - Exponential
- O(n!) - Factorial

Basic operations include:
- Assignments
- Arithmetic operations
- Comparison statements
- Calling a function
- Return statements

One way to count the basic operation is:
```python
n = 100  # Assignment statement 1 time
count = 0  # Assignment statement 1 time
while count < n:  # Comparison statement n times
    count += 1  # Arithmetic operation (and assignment!) n times + n times
    print(count)  # Output statement n times
```
In total, that's 1+1+n+n+n+n =  4n + 2 basic operations.

How to determine which big-O class an algorithm belongs to?
- We make some drastic simplifications
- Depending on how we count, an algorithm may look to have 2n or 5n + 20 basic operations, but for the purposes of analyzing its time complexity, we would consider both to be equivalent to O(n)
- Throw away constants
  - If we have 2n basic operations, we simplify and say the algorithm is O(n)
  - If we have 200 basic operations, we simplify that to O(1)
- Ignore all but the largest term
  - n + 100 operations is simplified to O(n), and so is 500n + 100
  - if we have n^2 + 40n + 400 basic operations, we classify the time complexity as O(n^2)

# Sorting Data
## The Bubble Sort
- Very simple to understand and implement
- Performance: O(n^2)
  - For loops inside of for loops are usually n^2
- Other sorting algorithms are generally much better
- Not considered to be a practical solution
## The Merge sort
- Divide-and-conquer algorithm
- Breaks a dataset into individual pieces and merges them
- Uses recursion to operate on datasets
- Performs well on large sets of data
- In general has a performance of O(n log n) time complexity
## The Quick sort
- Divide-and-conquer algorithm, like the merge sort
- Also uses recursion to perform sorting
- Generally performs better than merge sort, O(n log n)
- Operates in place on the data
- Worst case is O(n2) when data is mostly sorted already

