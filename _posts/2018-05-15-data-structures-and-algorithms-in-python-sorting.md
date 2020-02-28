---
id: 1718
title: 'Data Structures and Algorithms in Python Sorting'
date: 2018-05-15T22:01:48+05:30
author: Pradeep Pant
layout: post

---
## Bubble Sort Implementation

The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order. Each pass through the list places the next largest value in its proper place. In essence, each item “bubbles” up to the location where it belongs.

  * Regardless of how the items are arranged in the initial list, n−1 passes will be made to sort a list of size n, so 1 pass n-1 comparisons, 2 pass n-2 comparisons and n-1 is 1 comparisons.

  * A bubble sort is often considered the most inefficient sorting method since it must exchange items before the final location is known. These “wasted” exchange operations are very costly. However, because the bubble sort makes passes through the entire unsorted portion of the list, it has the capability to do something most sorting algorithms cannot. In particular, if during a pass there are no exchanges, then we know that the list must be sorted. A bubble sort can be modified to stop early if it finds that the list has become sorted. This means that for lists that require just a few passes, a bubble sort may have an advantage in that it will recognize the sorted list and stop.

#### Performance:  
  - Worst case: `O(n2) n-square` 
  - Best case: `O(n)` 
  - Average case: `O(n2) n-square`

	
#### Example:

```python
arr = [2,7,1,8,5,9,11,35,25]
bubble_sort(arr)
print (arr)
[1, 2, 5, 7, 8, 11, 25, 35]
```

## Selection Sort Implementation

  Selection sort is a in-place algorithm. It works well with small files. It is used for sorting the files with large values and small keys this is due to the fact that selection is based on keys and swaps are made only when required. The selection sort improves on the bubble sort by making only one exchange for every pass through the list. In order to do this, a selection sort looks for the largest value as it makes a pass and, after completing the pass, places it in the proper location. As with a bubble sort, after the first pass, the largest item is in the correct place. After the second pass, the next largest is in place. This process continuesand requires n−1 passes to sort n items, since the final item must be in place after the (n−1) st pass.

#### Performance: 
  - Worst case: `O(n2) n-square` 
  - Best case: `O(n)` 
  - Average case: `O(n2) n-square` 
  - Worst case space complexity: `O(1)`

#### Example: 
```python
arr = [2,7,1,8,5,9,11,35,25]
selection_sort(arr)
print (arr)
[1, 2, 5, 7, 8, 11, 25, 35]
```

## Insertion Sort Implementation
Insertion sort always maintains a sorted sub list in the lower portion of the list Each new item is then inserted back into the previous sublist such that the sorted sub list is one item larger complexity O(n2) square

#### Example 
```python
arr = [2,7,1,8,5,9,11,35,25]
insertion_sort(arr)
print (arr)
[1, 2, 5, 7, 8, 11, 25, 35]
```

## Merge Sort Implementation
Merge sort is a recursive algorithm (example of divide and conquer) that continually splits a list in half. If the list is empty or has one item, it is sorted by definition (the base case).
If the list has more than one item, we split the list and recursively invoke a
Merge sort on both halves. Once the two halves are sorted, the fundamental operation, called a merge, is performed. Merging is the process of taking two smaller sorted lists and combining them
together into a single, sorted, new list. This algorithm is used to sort a linked list.

#### Performance: 
- Worst case: `O(nlog n)` 
- Best case: `O(nlog n)` 
- Average case: `O(nlog n)`

#### Example

```python
arr = [11,2,5,4,7,6,8,1,23]
merge_sort(arr)
print (arr)
[1, 2, 4, 5, 6, 7, 8, 11, 23]
```
## Quick Sort Implementation
The quick sort uses divide and conquer to gain the same advantages as the merge sort, while not using additional storage also known as partition exchange sort.
As a trade-off, however, it is possible that the list may not be divided in half. When this happens, we will see that performance is diminished. A quick sort first selects a value, which is called the pivot value. The role of the pivot value is to assist with splitting the list.
The actual position where the pivot value belongs in the final sorted list, commonly called the split point, will be used to divide the list for subsequent calls to the quick sort.

#### Performance: 
- Worst case: `O(n square)` 
- Best case: `O(nlog n)`
- Average case: `O(nlog n)`

#### Example:

```python
arr = [2,7,1,8,5,9,11,35,25]
quick_sort(arr)
print (arr)
[1, 2, 5, 7, 8, 11, 25, 35]
```
## Shell Sort Implementation
This is also called diminishing incremental sort. The shell sort improves on insertion sort by breaking the original list into a number of smaller sublists. The unique way these sun lists are chosen is the key to the shell sort. Instead of breaking the list into sublists of contiguous items, the shell sort uses an increment ”i” to create a sublist by choosing all items that are ”i” items apart. Shell sort is efficient for medium size lists Complexity somewhere between O(n) and O(n2) square.

#### Example:

```python
arr = [45,67,23,45,21,24,7,2,6,4,90]
shell_sort(arr)
print (arr)
[2, 4, 6, 7, 21, 23, 24, 45, 45, 67, 90]
```

------

------

Check **[GitHub](https://github.com/ppant/DS-Algos-Python)** for the full working code.

I will keep adding more problems/solutions.
Stay tuned!

**Reference:** The inspiration of implementing DS in Python is from **[this](http://interactivepython.org/runestone/static/pythonds/index.html)** course.
    