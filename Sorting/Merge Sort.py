'''
Problem statement:
Given an array arr[], its starting position l and its ending position r. Sort the array 
using merge sort algorithm.
Example 1:

Input:
N = 5
arr[] = {4 1 3 9 7}
Output:
1 3 4 7 9
'''
class Solution:
    def merge(self,arr, l, m, r): 
        n1 = m - l + 1
        n2 = r - m
        
        left_half = [0] * n1
        right_half = [0] * n2
        
        for i in range(n1):
            left_half[i] = arr[l + i]
        
        for j in range(n2):
            right_half[j] = arr[m + 1 + j]
        
        i = 0  
        j = 0  
        k = l  
        
        while i < n1 and j < n2:
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < n1:
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < n2:
            arr[k] = right_half[j]
            j += 1
            k += 1
            
    def mergeSort(self,arr, l, r):
        if l < r:
            m = (l + r) // 2
            
            self.mergeSort(arr, l, m)
            
            self.mergeSort(arr, m + 1, r)
            
            self.merge(arr, l, m, r)

'''
Example:
Suppose you have the following array to sort:
```
arr = [13, 24, 46, 20, 9, 52, 28]
```

Step-by-Step Explanation:

 1. `mergeSort` Function

The `mergeSort` function is a recursive function that splits the array into two halves, sorts each half, and then merges them back together using the `merge` function.

```python
def mergeSort(self, arr, l, r):
    if l < r:
        m = (l + r) // 2
        
        self.mergeSort(arr, l, m)   # Sort the first half
        self.mergeSort(arr, m + 1, r)  # Sort the second half
        
        self.merge(arr, l, m, r)    # Merge the two halves
```

- Base Case: 
  - The recursion stops when the array has one or zero elements (`l >= r`), which are inherently sorted.
  
- Recursive Division:
  - The array is split into two halves:
    - First half: `arr[l...m]`
    - Second half: `arr[m+1...r]`
  - This continues recursively until each subarray has only one element.

2. `merge` Function

The `merge` function combines two sorted subarrays into a single sorted subarray.

```python
def merge(self, arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    
    left_half = [0] * n1
    right_half = [0] * n2
    
    for i in range(n1):
        left_half[i] = arr[l + i]
    
    for j in range(n2):
        right_half[j] = arr[m + 1 + j]
    
    i = 0  
    j = 0  
    k = l  
    
    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = left_half[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = right_half[j]
        j += 1
        k += 1
```

- Initialization:
  - `n1` and `n2` are the sizes of the two halves.
  - `left_half` and `right_half` arrays temporarily store the elements of the left and right subarrays.

- Copying Elements:
  - The elements from `arr[l...m]` are copied into `left_half`.
  - The elements from `arr[m+1...r]` are copied into `right_half`.

- Merging:
  - The merging process compares elements from `left_half` and `right_half`, placing the smaller element back into the original array (`arr`).
  - This continues until all elements from one of the halves are placed back into `arr`.
  - After that, any remaining elements from `left_half` or `right_half` are copied into `arr`.

Walkthrough of the Example:

Initial Array:
```
arr = [13, 24, 46, 20, 9, 52, 28]
```

Step 1: First Split
```
Left Half:  [13, 24, 46, 20]
Right Half: [9, 52, 28]
```

Step 2: Further Split the Left Half
```
Left:  [13, 24]
Right: [46, 20]
```

Step 3: Sort and Merge the Subarrays
- After sorting:
  - `[13, 24]` remains as is.
  - `[20, 46]` is sorted.
- Merging `[13, 24]` and `[20, 46]`:
  ```
  Result: [13, 20, 24, 46]
  ```

Step 4: Further Split the Right Half
```
Left:  [9]
Right: [52, 28]
```
- `[52, 28]` is sorted to `[28, 52]`.

Step 5: Merge the Sorted Subarrays
- Merging `[9]` and `[28, 52]`:
  ```
  Result: [9, 28, 52]
  ```

Final Step: Merge the Two Halves
- Merging `[13, 20, 24, 46]` and `[9, 28, 52]`:
  ```
  Final Sorted Array: [9, 13, 20, 24, 28, 46, 52]
  ```

Conclusion

The merge sort algorithm efficiently sorts the array by dividing it into smaller 
subarrays, sorting those subarrays, and then merging them back together. This process 
results in a fully sorted array, with a time complexity of \(O(n \log n)\), making it 
very efficient for large datasets.

'''