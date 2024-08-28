'''
Problem statement:
Given an array arr[], its starting position is low (the index of the array) and its 
ending position is high(the index of the array).

Note: The low and high are inclusive.
Implement the partition() and quickSort() functions to sort the array.

Example 1:

Input:
N = 5
arr[] = {4 1 3 9 7}
Output:
1 3 4 7 9
'''

class Solution:
    def partition(self, arr, low, high):
        pivot = arr[high]  
        i = low - 1  

        for j in range(low, high):

            if arr[j] <= pivot:
                i += 1

                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickSort(self, arr, low, high):
        if low < high:

            pi = self.partition(arr, low, high)

            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

'''
Example:
Suppose you have the following array to sort:
```
arr = [13, 24, 46, 20, 9, 52, 28]
```

Step-by-Step Explanation:

1. `quickSort` Function

The `quickSort` function is a recursive function that sorts the array by selecting a 
pivot element, partitioning the array around the pivot, and then recursively sorting 
the subarrays.

```python
def quickSort(self, arr, low, high):
    if low < high:
        pi = self.partition(arr, low, high)  # Partition the array
        
        self.quickSort(arr, low, pi - 1)  # Recursively sort the left subarray
        self.quickSort(arr, pi + 1, high)  # Recursively sort the right subarray
```

- Base Case: 
  - The recursion stops when the array has one or zero elements (`low >= high`), 
  which are inherently sorted.

- Recursive Division:
  - The array is divided around a pivot element.
    - Elements less than the pivot are placed on its left.
    - Elements greater than the pivot are placed on its right.
  - This continues recursively until each subarray has only one element.

2. `partition` Function

The `partition` function selects a pivot element and rearranges the array such that 
elements smaller than the pivot are on the left and elements larger are on the right.

```python
def partition(self, arr, low, high):
    pivot = arr[high]  # Choose the pivot as the last element
    i = low - 1  # Pointer for the smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if the element is smaller than or 
                                                equal to pivot
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place the pivot in the correct 
                                                    position
    return i + 1
```

- Initialization:
  - The pivot is chosen as the last element of the array segment.
  - `i` is initialized to one less than `low` to keep track of the boundary of 
  elements smaller than the pivot.

- Partitioning:
  - The loop iterates through the array, comparing each element to the pivot.
  - If an element is less than or equal to the pivot, it is swapped with the element 
  at index `i+1`, effectively moving it to the left side.
  - After the loop, the pivot is swapped with the element at `i+1`, placing it in its 
  correct sorted position.

Walkthrough of the Example:

Initial Array:
```
arr = [13, 24, 46, 20, 9, 52, 28]
```

Step 1: First Partitioning
- Pivot: 28 (last element)
- Array before partitioning:
  ```
  [13, 24, 46, 20, 9, 52, 28]
  ```
- Partitioned Array: Elements are rearranged around the pivot 28.
  ```
  [13, 24, 20, 9, 28, 52, 46]
  ```
- Pivot Index: 4 (Element 28 is now at the correct position)

Step 2: QuickSort Left Subarray `[13, 24, 20, 9]`
- Pivot: 9
- Array before partitioning:
  ```
  [13, 24, 20, 9]
  ```
- Partitioned Array:
  ```
  [9, 24, 20, 13]
  ```
- Pivot Index: 0 (Element 9 is now at the correct position)

Step 3: QuickSort Subarray `[24, 20, 13]`
- Pivot: 13
- Array before partitioning:
  ```
  [24, 20, 13]
  ```
- Partitioned Array:
  ```
  [13, 20, 24]
  ```
- Pivot Index: 1 (Element 13 is now at the correct position)

Step 4: QuickSort Right Subarray `[52, 46]`
- Pivot: 46
- Array before partitioning:
  ```
  [52, 46]
  ```
- Partitioned Array:
  ```
  [46, 52]
  ```
- Pivot Index: 5 (Element 46 is now at the correct position)

Final Step: Combining the Sorted Subarrays
- The subarrays are now combined to form the fully sorted array:
  ```
  Final Sorted Array: [9, 13, 20, 24, 28, 46, 52]
  ```

Conclusion:
The QuickSort algorithm efficiently sorts the array by selecting a pivot element, 
partitioning the array around it, and recursively sorting the resulting subarrays. 
This process results in a fully sorted array, with a time complexity of \(O(n \log n)\) 
on average, making it efficient for large datasets.

'''