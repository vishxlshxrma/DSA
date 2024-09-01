'''
Problem statement:
Given an array nums, return true if the array was originally sorted in non-decreasing 
order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such 
that A[i] == B[(i+x) % A.length], where % is the modulo operation.


Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of 
value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

'''

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(1,n):
            if (nums[i-1] > nums[i]):
                count += 1
        if (nums[n-1] > nums[0]):
            count += 1

        return count <= 1 
    

'''
Let's go through the code line by line, along with a detailed explanation 
and a walkthrough of an example.

Code:

```python
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                count += 1
        
        if nums[n-1] > nums[0]:
            count += 1
        
        return count <= 1
```

Line-by-Line Explanation

1. Class and Function Definition:
   ```python
   class Solution:
   ```
   - We define a class named `Solution`. This is common in competitive programming and 
   interview settings, where solutions are expected to be part of a class.

   ```python
   def check(self, nums: List[int]) -> bool:
   ```
   - Inside the `Solution` class, we define a method `check`, which takes `self` 
   (the instance of the class) and a list of integers `nums` as arguments.
   - The method is expected to return a boolean (`True` or `False`).

2. Initialize the Counter and Length:
   ```python
   count = 0
   n = len(nums)
   ```
   - `count = 0`: We initialize a variable `count` to 0. This variable will be used to 
   count the number of "drops" in the array (where an element is greater than the next 
   element).
   - `n = len(nums)`: We store the length of the array `nums` in variable `n` for easy 
   reference.

3. Loop Through the Array (1 to n-1):
   ```python
   for i in range(1, n):
   ```
   - We start a loop from `i = 1` to `i = n-1`. This loop will allow us to compare 
   each element with the one before it.

4. Check for a "Drop" in the Array:
   ```python
   if nums[i-1] > nums[i]:
       count += 1
   ```
   - Inside the loop, for each element `nums[i]`, we compare it with the previous 
   element `nums[i-1]`.
   - If `nums[i-1] > nums[i]`, it indicates a "drop," meaning the array is not in 
   non-decreasing order at that point.
   - If a drop is found, we increment the `count` by 1.

5. Check the Last Element Against the First:
   ```python
   if nums[n-1] > nums[0]:
       count += 1
   ```
   - After the loop completes, we perform a special check: we compare the last element 
   `nums[n-1]` with the first element `nums[0]`.
   - This check is crucial because a rotated sorted array might have its maximum 
   element at the end and its minimum element at the beginning.
   - If `nums[n-1] > nums[0]`, we count this as another "drop" and increment `count` 
   by 1.

6. Return the Result:
   ```python
   return count <= 1
   ```
   - Finally, we return `True` if `count` is less than or equal to 1, meaning there 
   is at most one "drop" in the array, which could indicate that the array is sorted 
   or is a rotated version of a sorted array.
   - If `count` is greater than 1, the function returns `False`, indicating that the 
   array cannot be a rotated sorted array.

Example Walkthrough

Let's walk through the code with an example array:

```python
nums = [3, 4, 5, 1, 2]
```

Step-by-Step Execution:

1. Initialization:
   - `count = 0`
   - `n = 5` (since `nums` has 5 elements)

2. Loop Iterations:

   - First iteration (`i = 1`):
     - Compare `nums[0] = 3` with `nums[1] = 4`
     - `3` is not greater than `4`, so `count` remains `0`.

   - Second iteration (`i = 2`):
     - Compare `nums[1] = 4` with `nums[2] = 5`
     - `4` is not greater than `5`, so `count` remains `0`.

   - Third iteration (`i = 3`):
     - Compare `nums[2] = 5` with `nums[3] = 1`
     - `5` is greater than `1`, indicating a drop.
     - Increment `count` by 1 (`count = 1`).

   - Fourth iteration (`i = 4`):
     - Compare `nums[3] = 1` with `nums[4] = 2`
     - `1` is not greater than `2`, so `count` remains `1`.

3. Special Check for Circular Transition:
   - Compare the last element `nums[4] = 2` with the first element `nums[0] = 3`
   - `2` is not greater than `3`, so `count` remains `1`.

4. Return Statement:
   - Check `count <= 1`
   - `count` is `1`, which satisfies `count <= 1`.
   - The function returns `True`.

Conclusion

In this example, the array `[3, 4, 5, 1, 2]` is a rotated version of the sorted array 
`[1, 2, 3, 4, 5]`. The function correctly identifies this and returns `True`.

If there had been more than one "drop" in the array, the function would have returned 
`False`, indicating that the array is not a rotated sorted array.
'''