'''
Problem statement:
You are given an integer array 'arr' of size 'N'.
You must sort this array using 'Bubble Sort'.

Note:
Change in the input array itself. You don't need to return or print the elements.
Example:
Input: 'N' = 7
'arr' = [2, 13, 4, 1, 3, 6, 28]

Output: [1 2 3 4 6 13 28]
Explanation: After applying bubble sort on the input array, the output is [1 2 3 4 6 13 28].

'''

from typing import List

def bubbleSort(arr: List[int], n: int):
    n = len(arr)
    for i in range(n-1,0,-1):
        for j in range(i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]

'''
Bubble sort is a simple sorting algorithm that repeatedly steps through the list to be sorted, 
compares each pair of adjacent items, and swaps them if they are in the wrong order. 
The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

Here's a step-by-step explanation of how bubble sort works:


1. Start at the beginning of the list.
2. Compare the first two elements of the list. If they are in the wrong order, swap them.
3. Move to the next pair of elements and repeat the comparison and swap if necessary.
4. Continue this process until you reach the end of the list.
5. After the first pass through the list, the largest element will be in its correct position at the end of the list.
6. Repeat steps 1-5 for the remaining elements in the list, excluding the last element that is already in its correct position.
7. Continue this process until no more swaps are needed, indicating that the list is sorted.

Code Breakdown:
Certainly! Let's break down the provided code line by line:

```python
from typing import List
```
This line imports the `List` class from the `typing` module. It's used to indicate that the `arr` parameter in the `bubbleSort` 
function is expected to be a list of integers.

```python
def bubbleSort(arr: List[int], n: int):
```
This line defines a function named `bubbleSort` that takes two parameters: a list of integers `arr` and an integer `n`. 
The `n` parameter is redundant since you are already using `n = len(arr)` inside the function. You can remove the `n` parameter 
from the function definition.

```python
    n = len(arr)
```
This line initializes the variable `n` with the length of the input list `arr`. However, since you already have a parameter `n` in 
the function, you can remove this line.

```python
    for i in range(n-1, 0, -1):
```
This line starts an outer loop that iterates from `n-1` down to 1 (inclusive) with a step of -1. This loop represents each pass 
through the list.

```python
        for j in range(i):
```
Within the outer loop, an inner loop is initiated that iterates over the range from 0 to `i-1`. This loop represents the 
comparison and swapping of adjacent elements.

```python
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```
Within the inner loop, there's a conditional statement that compares adjacent elements. If the element at index `j` is greater 
than the element at index `j+1`, a swap is performed using a simultaneous assignment. This is a common idiom in Python for 
swapping two values without using a temporary variable.

'''