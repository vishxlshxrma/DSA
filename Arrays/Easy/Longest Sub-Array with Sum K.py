'''
Problem statement:
Given an array arr[] containing integers and an integer k, your task is to find the length of the longest 
subarray where the sum of its elements is equal to the given value k. It is guaranteed that a valid 
subarray exists.

Examples:

Input: arr[] = [10, 5, 2, 7, 1, 9], k = 15
Output: 4
Explanation: The subarray [5, 2, 7, 1] has a sum of 15 and length 4.

Input: arr[] = [-1, 2, 3], k = 6
Output: 0
Explanation: There is no subarray with a sum of 6.

Input: arr[] = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] has a sum of 3 and length 4.

Constraints:
1 ≤ arr.size() ≤ 106
-109 ≤ arr[i], k ≤ 109
'''

class Solution:
    def lenOfLongestSubarr(self, arr, k):  
        cumulative_sum_map = {}
        current_sum = 0
        max_length = 0

        for i in range(len(arr)):
            current_sum += arr[i]

            if current_sum == k:
                max_length = i + 1

            if (current_sum - k) in cumulative_sum_map:
                max_length = max(max_length, i - cumulative_sum_map[current_sum - k])
            
            if current_sum not in cumulative_sum_map:
                cumulative_sum_map[current_sum] = i
        
        return max_length
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.lenOfLongestSubarr(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends


'''
The goal is to find the length of the longest subarray in `arr[]` where the sum of its elements is 
exactly equal to `k`. We use a dictionary to efficiently track cumulative sums and find the longest 
subarray with the target sum.

Code Breakdown:

```python
def longest_subarray_with_sum_k(arr, k):
    # Dictionary to store the cumulative sum and its earliest index
    cumulative_sum_map = {}
    current_sum = 0
    max_length = 0

    for i in range(len(arr)):
        # Update the cumulative sum
        current_sum += arr[i]

        # Check if the entire array up to the current index has the sum `k`
        if current_sum == k:
            max_length = i + 1

        # Check if `current_sum - k` exists in the dictionary
        if (current_sum - k) in cumulative_sum_map:
            # Calculate the length of this subarray
            max_length = max(max_length, i - cumulative_sum_map[current_sum - k])

        # If current_sum is not in the dictionary, add it with the current index
        if current_sum not in cumulative_sum_map:
            cumulative_sum_map[current_sum] = i

    return max_length
```

Explanation:

1. Initialize Variables**:
   ```python
   cumulative_sum_map = {}
   current_sum = 0
   max_length = 0
   ```
   - `cumulative_sum_map` is a dictionary that stores cumulative sums and their first occurrences.
   - `current_sum` keeps track of the sum of elements from the beginning up to the current index.
   - `max_length` stores the length of the longest subarray found so far that sums to `k`.

2. Iterate Through the Array:
   ```python
   for i in range(len(arr)):
       current_sum += arr[i]
   ```
   - A loop iterates over each element in `arr`, and `current_sum` is updated by adding the current element 
   at each index.
   - `current_sum` represents the sum of elements from the start of the array to the current index.

3. Check if the Entire Array So Far Has Sum `k`:
   ```python
   if current_sum == k:
       max_length = i + 1
   ```
   - If `current_sum` equals `k` at any point, it means the subarray from the beginning to the current index 
   sums to `k`.
   - In this case, update `max_length` to `i + 1` because this is the longest subarray (from index `0` to `i`) 
   that sums to `k` found so far.

4. Check for a Subarray Ending at Current Index with Sum `k`:
   ```python
   if (current_sum - k) in cumulative_sum_map:
       max_length = max(max_length, i - cumulative_sum_map[current_sum - k])
   ```
   - We check if `current_sum - k` exists in `cumulative_sum_map`.
   - If it does, then there is an earlier subarray ending before the current index whose sum is exactly 
   `current_sum - k`. This implies that the subarray from `cumulative_sum_map[current_sum - k] + 1` to `i` 
   has a sum of `k`.
   - We calculate the length of this subarray as `i - cumulative_sum_map[current_sum - k]` and update 
   `max_length` if this subarray is longer than any found so far.

5. Store the Cumulative Sum with the Earliest Index:
   ```python
   if current_sum not in cumulative_sum_map:
       cumulative_sum_map[current_sum] = i
   ```
   - If `current_sum` is not already in `cumulative_sum_map`, we add it with its current index `i`.
   - This ensures we only store the **first occurrence** of each cumulative sum, which helps in maximizing 
   the length of subarrays with sum `k` when we encounter `current_sum - k`.

6. Return the Length of the Longest Subarray:
   ```python
   return max_length
   ```
   - After iterating through the array, `max_length` will hold the length of the longest subarray with sum `k`.
   - The function returns `max_length` as the result.

Example Walkthrough:

Let's go through an example to see how the code works step-by-step:

```python
arr = [10, 5, 2, 7, 1, 9]
k = 15
```

Step-by-Step Execution:

1. Initialization:
   - `cumulative_sum_map = {}`
   - `current_sum = 0`
   - `max_length = 0`

2. Loop Iterations:

   - Index 0 (Element 10):
     - `current_sum = 10`
     - `current_sum` is not `k`, so we check if `current_sum - k = -5` is in `cumulative_sum_map`, but it's not.
     - Add `10` to `cumulative_sum_map` with index `0`: `{10: 0}`.

   - Index 1 (Element 5):
     - `current_sum = 10 + 5 = 15`
     - `current_sum == k`, so the subarray `[10, 5]` (from index `0` to `1`) has a sum of `k`.
     - Update `max_length = 2` (length of subarray `[10, 5]`).
     - Add `15` to `cumulative_sum_map` with index `1`: `{10: 0, 15: 1}`.

   - Index 2 (Element 2):
     - `current_sum = 15 + 2 = 17`
     - `current_sum` is not `k`, so check if `current_sum - k = 2` is in `cumulative_sum_map`, but it's not.
     - Add `17` to `cumulative_sum_map` with index `2`: `{10: 0, 15: 1, 17: 2}`.

   - Index 3 (Element 7):
     - `current_sum = 17 + 7 = 24`
     - `current_sum` is not `k`, so check if `current_sum - k = 9` is in `cumulative_sum_map`, but it's not.
     - Add `24` to `cumulative_sum_map` with index `3`: `{10: 0, 15: 1, 17: 2, 24: 3}`.

   - Index 4 (Element 1):
     - `current_sum = 24 + 1 = 25`
     - `current_sum` is not `k`, so check if `current_sum - k = 10` is in `cumulative_sum_map`.
     - `10` is in the map at index `0`, so the subarray `[5, 2, 7, 1]` (from index `1` to `4`) has a sum of `k`.
     - Update `max_length = 4` (length of subarray `[5, 2, 7, 1]`).
     - Add `25` to `cumulative_sum_map` with index `4`: `{10: 0, 15: 1, 17: 2, 24: 3, 25: 4}`.

   - Index 5 (Element 9):
     - `current_sum = 25 + 9 = 34`
     - `current_sum` is not `k`, so check if `current_sum - k = 19` is in `cumulative_sum_map`, but it's not.
     - Add `34` to `cumulative_sum_map` with index `5`: `{10: 0, 15: 1, 17: 2, 24: 3, 25: 4, 34: 5}`.

3. Return Statement:
   - After the loop, `max_length = 4`, so the function returns `4`.

Final Result:
The function returns `4`, which is the length of the longest subarray with sum `k` found in `arr`.

Key Points

- The function uses a dictionary to track cumulative sums, allowing efficient lookup for subarrays with sum `k`.
- This approach works in linear time, `O(n)`, making it efficient for large arrays.
- The space complexity is also `O(n)` due to the dictionary used to store cumulative sums.
'''