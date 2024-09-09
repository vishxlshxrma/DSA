'''
Problem statement:
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n 
        
        if k == 0:
            return
        
        temp = nums[-k:]
        
        for i in range(n - 1, k - 1, -1):
            nums[i] = nums[i - k]
        
        for j in range(k):
            nums[j] = temp[j]
        
        return nums
    
'''
Code Breakdown:

1. `class Solution:`
   - Defines a class named `Solution`. This is typical for organizing code, especially when submitting 
   solutions on platforms like LeetCode.

2. `def rotate(self, nums: List[int], k: int) -> None:`  
   - This line defines a method `rotate` inside the `Solution` class.
   - `nums: List[int]` specifies that `nums` is expected to be a list of integers.
   - `k: int` specifies that `k` is an integer.
   - `-> None` indicates that the method does not return a value (it modifies `nums` in place).

3. `n = len(nums)`
   - Calculates the length of the list `nums` and stores it in the variable `n`.
   - Example: If `nums = [1, 2, 3, 4, 5, 6, 7]`, then `n = 7`.

4. `k = k % n`
   - This handles cases where `k` (the number of rotations) is greater than the length of the list. 
   - The `%` operator calculates the remainder when `k` is divided by `n`.
   - Example: If `k = 10` and `n = 7`, then `k = 10 % 7 = 3`. So, rotating by 10 is the same as rotating by 3.

5. `if k == 0:`  
   - This checks if `k` is 0 after the modulo operation.
   - If `k` is 0, no rotation is needed, so the function returns immediately.
   - Example: If `k = 0`, there's no need to rotate, so the function exits.

6. `temp = nums[-k:]`
   - This line extracts the last `k` elements of the list `nums` and stores them in the list `temp`.
   - `nums[-k:]` is a slicing operation that takes elements from the end of the list.
   - Example: If `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, then `temp = [5, 6, 7]`.

7. `for i in range(n - 1, k - 1, -1):` 
   - This loop iterates backward over the indices of the list `nums`, starting from `n-1` (the last index) 
   and ending at `k-1`.
   - Purpose: Shift the elements of `nums` to the right by `k` positions.
   - Example: With `n = 7` and `k = 3`, the loop runs from `i = 6` to `i = 3`.

8. `nums[i] = nums[i - k]`
   - For each index `i`, this line sets `nums[i]` to the value of `nums[i - k]`.
   - This effectively shifts the elements in `nums` to the right by `k` positions.
   - Example:
     - `i = 6`: `nums[6] = nums[3]` (i.e., `nums[6]` becomes `4`)
     - `i = 5`: `nums[5] = nums[2]` (i.e., `nums[5]` becomes `3`)
     - `i = 4`: `nums[4] = nums[1]` (i.e., `nums[4]` becomes `2`)
     - `i = 3`: `nums[3] = nums[0]` (i.e., `nums[3]` becomes `1`)

9. `for j in range(k):`
   - This loop iterates over the first `k` indices (i.e., from `0` to `k-1`).
   - Purpose: Place the `k` elements stored in `temp` at the beginning of `nums`.
   - Example: With `k = 3`, this loop will run for `j = 0`, `1`, and `2`.

10. `nums[j] = temp[j]` 
    - For each index `j`, this line sets `nums[j]` to the corresponding element in `temp`.
    - Example:
      - `j = 0`: `nums[0] = temp[0]` (i.e., `nums[0]` becomes `5`)
      - `j = 1`: `nums[1] = temp[1]` (i.e., `nums[1]` becomes `6`)
      - `j = 2`: `nums[2] = temp[2]` (i.e., `nums[2]` becomes `7`)

11. `return nums`
    - This line is unnecessary since the method is supposed to modify `nums` in place and return `None`. 
    However, it won't cause any harm if left in, but it can be removed to align with the function's intended 
    purpose.

Example Walkthrough:

Input:
```python
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
```

1. Initial Setup:
   - `n = 7`
   - `k = k % n = 3 % 7 = 3`
   - `temp = nums[-3:] = [5, 6, 7]`

2. Shifting Elements:
   - `nums[6] = nums[3]` → `nums = [1, 2, 3, 4, 5, 6, 4]`
   - `nums[5] = nums[2]` → `nums = [1, 2, 3, 4, 5, 3, 4]`
   - `nums[4] = nums[1]` → `nums = [1, 2, 3, 4, 2, 3, 4]`
   - `nums[3] = nums[0]` → `nums = [1, 2, 3, 1, 2, 3, 4]`

3. Placing `temp` at the beginning:
   - `nums[0] = temp[0]` → `nums = [5, 2, 3, 1, 2, 3, 4]`
   - `nums[1] = temp[1]` → `nums = [5, 6, 3, 1, 2, 3, 4]`
   - `nums[2] = temp[2]` → `nums = [5, 6, 7, 1, 2, 3, 4]`

Final Output:
```python
nums = [5, 6, 7, 1, 2, 3, 4]
```

This result corresponds to rotating the original array `[1, 2, 3, 4, 5, 6, 7]` by 3 positions to the right.

'''