'''
Problem statement:
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], 
[2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
More formally, if all the permutations of the array are sorted in one container according to their 
lexicographical order, then the next permutation of that array is the permutation that follows it in the 
sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible 
order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger 
rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.


Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
'''

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)

        gola_index = -1

        # Step 1: Find the first decreasing element from the right
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                gola_index = i - 1
                break

        if gola_index != -1:
            # Step 2: Find the smallest element larger than nums[gola_index] to the right
            for j in range(n - 1, gola_index, -1):
                if nums[j] > nums[gola_index]:
                    # Swap them
                    nums[gola_index], nums[j] = nums[j], nums[gola_index]
                    break

        # Step 3: Reverse the portion of the array after gola_index
        nums[gola_index + 1:] = reversed(nums[gola_index + 1:])



'''
A permutation of an array of integers is a rearrangement of its members into a sequence or linear order. 
The task is to compute the next permutation of the given array in lexicographical order.

Detailed Description:
1. If the array is sorted in ascending order, its next permutation will be the smallest rearrangement that is 
larger than the current sequence.
2. If the array is sorted in descending order, it is the last permutation. The next permutation in this case 
will reset the sequence to its smallest possible arrangement (i.e., sorted in ascending order).
3. The solution must rearrange the elements in place and use constant extra memory.

Examples:


Example 1:
Input:
`nums = [1, 2, 3]`  

Output:
`[1, 3, 2]`  

Explanation:
The next permutation in lexicographical order after `[1, 2, 3]` is `[1, 3, 2]`.

Example 2:
Input:  
`nums = [3, 2, 1]`  

Output:
`[1, 2, 3]`  

Explanation:
Since `[3, 2, 1]` is the largest permutation, the next permutation is the smallest one: `[1, 2, 3]`.

Example 3:
Input:  
`nums = [1, 1, 5]`  

Output:
`[1, 5, 1]`  

Explanation:
The next permutation in lexicographical order after `[1, 1, 5]` is `[1, 5, 1]`.


Approach to Solve:
The solution can be broken into three key steps:

Step 1: Identify the "Pivot" (First Decreasing Element from the Right)
- Traverse the array from right to left to find the first element (`nums[gola_index]`) that is smaller than 
its next element.
- This indicates the position where a rearrangement is needed to create the next permutation.
- If no such element exists, the array is in descending order. In this case, reverse the array to get the 
smallest permutation.

Step 2: Swap the Pivot with the Smallest Larger Element to its Right
- Starting from the rightmost element, find the smallest element greater than `nums[gola_index]`.
- Swap these two elements to ensure the permutation remains as close as possible to the current one.

Step 3: Reverse the Elements to the Right of the Pivot
- Reverse the subarray to the right of `gola_index` to get the smallest lexicographical order.


Code with Line-by-Line Explanation:

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)  # Get the size of the array
        gola_index = -1  # Initialize the pivot index
        
        # Step 1: Find the first decreasing element from the right
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:  # Check if nums[i] > nums[i-1]
                gola_index = i - 1  # Set the pivot index
                break

        # Step 2: If a pivot exists, find the element to swap
        if gola_index != -1:  # If a valid pivot was found
            for j in range(n - 1, gola_index, -1):
                if nums[j] > nums[gola_index]:  # Find the smallest number greater than nums[gola_index]
                    nums[gola_index], nums[j] = nums[j], nums[gola_index]  # Swap
                    break

        # Step 3: Reverse the part of the array after the pivot
        nums[gola_index + 1:] = reversed(nums[gola_index + 1:])  # Reverse in-place
```


Example Walkthrough:

Input:  
`nums = [1, 2, 3]`

1. Step 1: Find the Pivot  
   - Start from the right: Compare `3 > 2`. Found the pivot: `gola_index = 1`.

2. Step 2: Find the Element to Swap  
   - Look for the smallest element larger than `nums[1] (2)` starting from the right:
     - `3 > 2`, so swap `nums[1]` and `nums[2]`.  
     - Result: `nums = [1, 3, 2]`.

3. Step 3: Reverse the Subarray After the Pivot  
   - Reverse `nums[2:]`. Since there's only one element, no change.  
   - Final result: `nums = [1, 3, 2]`.

---

Input:  
`nums = [3, 2, 1]`

1. Step 1: Find the Pivot  
   - Start from the right: No element satisfies `nums[i] > nums[i-1]`.
   - No pivot found; reverse the array.

2. Step 3: Reverse the Entire Array
   - Result: `nums = [1, 2, 3]`.


Complexity Analysis:
1. Time Complexity: O(n)  
   - One traversal to find the pivot.
   - One traversal to find the swap element.
   - One traversal to reverse part of the array.

2. Space Complexity: O(1)  
   - In-place operations with no additional memory usage.


Summary:
This approach ensures we find the **next lexicographical permutation** of the array in optimal time. It is 
efficient, intuitive, and follows the constraints of the problem.
'''