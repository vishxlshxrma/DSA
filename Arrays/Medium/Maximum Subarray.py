'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

'''

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur_sum = 0
        max_sum = float('-inf')

        for i in range(len(nums)):
            cur_sum += nums[i]
            max_sum = max(max_sum,cur_sum)

            if cur_sum < 0:
                cur_sum = 0
        
        return max_sum
    
'''
Kadane's Algorithm is an efficient way to find the maximum sum of a contiguous subarray within a 
one-dimensional array of integers. The idea behind this algorithm is to traverse the array while keeping 
track of the current subarray sum and updating the maximum sum encountered so far.

Code Explanation:

The provided code snippet implements Kadane's Algorithm. Let's break it down step-by-step:

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = float('-inf')

        for i in range(len(nums)):
            cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)

            if cur_sum < 0:
                cur_sum = 0
        
        return max_sum
```

Step-by-Step Explanation:

1. Initialization:
   - `cur_sum = 0`: This variable tracks the sum of the current subarray. It starts at 0, meaning no sum has 
   been accumulated initially.
   - `max_sum = float('-inf')`: This variable stores the maximum sum found so far. It is initialized to 
   negative infinity to ensure that any sum encountered will be greater than this initial value.

2. Iterate through the array:
   - The loop runs over each element of the array `nums`.

   For each element `nums[i]`:
   - `cur_sum += nums[i]`: We add the current element to `cur_sum`, extending the subarray.
   - `max_sum = max(max_sum, cur_sum)`: We update `max_sum` to be the larger of the current `max_sum` and the 
   newly computed `cur_sum`.
   - `if cur_sum < 0`: If `cur_sum` becomes negative, it means that continuing the current subarray would 
   only decrease the sum. So, we reset `cur_sum = 0`, effectively starting a new subarray from the next 
   element.

3. Return Result:
   - Once the loop finishes, `max_sum` holds the maximum sum of any contiguous subarray found during the 
   iteration, which is returned as the result.

Walkthrough with Example:

Consider the input array `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`.

1. Initialization:
   - `cur_sum = 0`
   - `max_sum = -∞` (negative infinity)

2. Iteration through the array:

   - Step 1 (`i = 0`, `nums[i] = -2`):
     - `cur_sum += -2 → cur_sum = -2`
     - `max_sum = max(-∞, -2) → max_sum = -2`
     - Since `cur_sum < 0`, reset `cur_sum = 0`.

   - Step 2 (`i = 1`, `nums[i] = 1`):
     - `cur_sum += 1 → cur_sum = 1`
     - `max_sum = max(-2, 1) → max_sum = 1`
     - `cur_sum` is positive, so we don't reset it.

   - Step 3 (`i = 2`, `nums[i] = -3`):
     - `cur_sum += -3 → cur_sum = -2`
     - `max_sum = max(1, -2) → max_sum = 1`
     - Since `cur_sum < 0`, reset `cur_sum = 0`.

   - Step 4 (`i = 3`, `nums[i] = 4`):
     - `cur_sum += 4 → cur_sum = 4`
     - `max_sum = max(1, 4) → max_sum = 4`
     - `cur_sum` is positive, so we don't reset it.

   - Step 5 (`i = 4`, `nums[i] = -1`):
     - `cur_sum += -1 → cur_sum = 3`
     - `max_sum = max(4, 3) → max_sum = 4`
     - `cur_sum` is positive, so we don't reset it.

   - Step 6 (`i = 5`, `nums[i] = 2`):
     - `cur_sum += 2 → cur_sum = 5`
     - `max_sum = max(4, 5) → max_sum = 5`
     - `cur_sum` is positive, so we don't reset it.

   - Step 7 (`i = 6`, `nums[i] = 1`):
     - `cur_sum += 1 → cur_sum = 6`
     - `max_sum = max(5, 6) → max_sum = 6`
     - `cur_sum` is positive, so we don't reset it.

   - Step 8 (`i = 7`, `nums[i] = -5`):
     - `cur_sum += -5 → cur_sum = 1`
     - `max_sum = max(6, 1) → max_sum = 6`
     - `cur_sum` is positive, so we don't reset it.

   - Step 9 (`i = 8`, `nums[i] = 4`):
     - `cur_sum += 4 → cur_sum = 5`
     - `max_sum = max(6, 5) → max_sum = 6`
     - `cur_sum` is positive, so we don't reset it.

3. Return Result:
   - After finishing the loop, the `max_sum` is `6`, which is the maximum sum of any contiguous subarray in 
   `nums`.

Key Points:
- `cur_sum` Reset**: When `cur_sum` drops below 0, it is reset to 0, signaling that starting a new subarray 
from the next index might yield a higher sum.
- `max_sum` Update**: At each step, we ensure `max_sum` stores the maximum subarray sum encountered so far.

Time Complexity:
- Time Complexity**: \(O(n)\), where \(n\) is the number of elements in the array. We only traverse the 
array once.
- Space Complexity**: \(O(1)\), as we use only a constant amount of extra space.

This approach is efficient and works for all kinds of input arrays, including those with negative numbers or 
arrays with only one element.
'''