# Understanding Algorithm Performance
- Measure how an algorithm responds to dataset size
- Big-O notation
  - Classifies performance as the input size grows
  - "O" indicates the order of operation: time scale to perform an operation
- Many algorithms and data structures have more than one Big O
  - Inserting data, searching for data, deleting data, etc.
##### Common Big-O Terms
![](img1.png)

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

