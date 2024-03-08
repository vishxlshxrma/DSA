'''
Problem statement:
Sort the given unsorted array 'arr' of size 'N' in non-decreasing order using the selection sort algorithm.

Note:
Change in the input array/list itself. 

Example:
Input:
N = 5
arr = {8, 6, 2, 5, 1}

Output:
1 2 5 6 8 

'''

from typing import List

def selectionSort(arr: List[int]) -> None: 
    N = len(arr)
    for i in range(N-1):
        mini = i
        for j in range(i+1, N):
            if arr[j] < arr[mini]:
                mini = j
                
        arr[i], arr[mini] = arr[mini], arr[i]

'''
Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum (or maximum) element from 
the unsorted portion of the array and swapping it with the element at the beginning of the unsorted portion. 
Here's how it works:

1. Start by finding the smallest element in the array and swap it with the element at the first position.
2. Move to the next position and find the smallest element in the remaining unsorted portion of the array and swap it 
   with the element at the second position.
3. Repeat this process until the entire array is sorted.

Code Breakdown:
Let's break down the provided Python code line by line:

```python
from typing import List
```
- This line imports the `List` type hint from the `typing` module. It is used to specify that the function `selectionSort` 
takes a list of integers as input.

```python
def selectionSort(arr: List[int]) -> None:
```
- This line defines a function named `selectionSort`. It takes one argument `arr`, which is expected to be a list of integers. 
The `-> None` indicates that the function does not return any value (or returns `None`).

```python
    N = len(arr)
```
- This line calculates the length of the input list `arr` and assigns it to the variable `N`.

```python
    for i in range(N-1):
```
- This line starts a `for` loop that iterates over indices from `0` to `N-2`. It iterates through the list up to the 
second-to-last element, as the last element will be automatically sorted when the rest of the list is sorted.

```python
        mini = i
```
- This line initializes the variable `mini` to the current index `i`. It keeps track of the index of the minimum element found so far.

```python
        for j in range(i+1, N):
```
- This line starts another `for` loop nested inside the outer loop. It iterates over the indices from `i+1` to `N-1`. 
This loop searches for the index of the minimum element in the unsorted portion of the list.

```python
            if arr[j] < arr[mini]:
```
- This line checks if the element at index `j` is less than the element at the current minimum index `mini`.

```python
                mini = j
```
- If the element at index `j` is smaller than the element at the current minimum index `mini`, `mini` is updated to `j`.

```python
        arr[i], arr[mini] = arr[mini], arr[i]
```
- After finding the index of the minimum element in the unsorted portion of the list, this line swaps the elements at indices `i` and `mini`. 
This places the minimum element in its correct position in the sorted portion of the list.

The function repeats this process until the entire list is sorted in ascending order.

'''