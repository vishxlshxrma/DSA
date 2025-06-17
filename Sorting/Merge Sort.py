'''
Problem statement:
Given an array arr[], its starting position l and its ending position r. Sort the array 
using the merge sort algorithm.

Example 1:
Input:
N = 5
arr[] = {4 1 3 9 7}
Output:
1 3 4 7 9
'''

class Solution:

    def merge(self, arr, l, m, r):
        '''
        This function merges two sorted subarrays of arr[].
        The first subarray is arr[l...m]
        The second subarray is arr[m+1...r]
        '''
        
        i = l           # Starting index of the left subarray
        j = m + 1       # Starting index of the right subarray
        temp = []       # Temporary list to store merged elements

        # Merge the two subarrays by comparing elements
        while (i <= m and j <= r):
            if (arr[i] <= arr[j]):
                temp.append(arr[i])  # Add the smaller element to temp
                i += 1               # Move pointer in the left subarray
            else:
                temp.append(arr[j])  # Add the smaller element to temp
                j += 1               # Move pointer in the right subarray

        # If there are remaining elements in the left subarray, add them
        while (i <= m):
            temp.append(arr[i])
            i += 1

        # If there are remaining elements in the right subarray, add them
        while (j <= r):
            temp.append(arr[j])
            j += 1

        # Copy the merged elements from temp back to the original array
        for k in range(len(temp)):
            arr[l + k] = temp[k]

    def mergeSort(self, arr, l, r):
        '''
        This function recursively sorts the array using the merge sort algorithm.
        arr: The array to be sorted
        l: Starting index
        r: Ending index
        '''
        if (l < r):
            m = l + (r - l) // 2  # Find the middle point to divide the array

            self.mergeSort(arr, l, m)      # Recursively sort the first half
            self.mergeSort(arr, m + 1, r)  # Recursively sort the second half

            self.merge(arr, l, m, r)       # Merge the sorted halves

'''
Example:
Suppose you have the following array to sort:
arr = [13, 24, 46, 20, 9, 52, 28]

Step-by-Step Explanation:

1. mergeSort Function

The mergeSort function is a recursive function that splits the array into two halves, 
sorts each half, and then merges them back together using the merge function.

Structure:
    def mergeSort(self, arr, l, r):
        if l < r:
            m = l + (r - l) // 2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)

- Base Case: 
    The recursion stops when l >= r, meaning the array has one or zero elements, 
    which are inherently sorted.

- Recursive Division:
    The array is split into two halves:
        - Left half: arr[l...m]
        - Right half: arr[m+1...r]

    This continues recursively until each subarray has only one element.

2. merge Function

The merge function combines two sorted subarrays into a single sorted subarray.

Structure:
    def merge(self, arr, l, m, r):
        i = l
        j = m + 1
        temp = []
        while i <= m and j <= r:
            ...
        while i <= m:
            ...
        while j <= r:
            ...
        for k in range(len(temp)):
            arr[l + k] = temp[k]

Explanation:
- Initialization:
    - i is the starting index of the left subarray
    - j is the starting index of the right subarray
    - temp is a temporary list to store merged elements

- Merging:
    - Compare elements from the left and right subarrays.
    - Place the smaller element into temp.
    - Continue this process until one subarray is fully traversed.

- Handling Remaining Elements:
    - After exiting the main loop, there may be leftover elements in either 
      the left or right subarray.
    - Add these remaining elements to temp.

- Copying Back:
    - Copy the sorted elements from temp back to the original array arr 
      starting from index l.

Walkthrough of the Example:

Initial Array:
arr = [13, 24, 46, 20, 9, 52, 28]

Step 1: First Split
Left Half:  [13, 24, 46, 20]
Right Half: [9, 52, 28]

Step 2: Further Split the Left Half
Left:  [13, 24]
Right: [46, 20]

Step 3: Sort and Merge the Subarrays
- [13, 24] remains sorted.
- [46, 20] is sorted to [20, 46].
- Merging [13, 24] and [20, 46]:
  Result: [13, 20, 24, 46]

Step 4: Further Split the Right Half
Left:  [9]
Right: [52, 28]
- [52, 28] is sorted to [28, 52]

Step 5: Merge the Sorted Subarrays
- Merging [9] and [28, 52]:
  Result: [9, 28, 52]

Final Step: Merge the Two Halves
- Merging [13, 20, 24, 46] and [9, 28, 52]:
  Final Sorted Array: [9, 13, 20, 24, 28, 46, 52]

Conclusion:
The merge sort algorithm efficiently sorts the array by dividing it into smaller 
subarrays, sorting those subarrays, and then merging them back together. This process 
results in a fully sorted array, with a time complexity of O(n log n), making it very 
efficient for large datasets.
'''