'''
Problem statement:
Given an integer array nums sorted in non-decreasing order, remove the duplicates 
in-place such that each unique element appears only once. The relative order of the 
elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to 
do the following things:

Change the array nums such that the first k elements of nums contain the unique 
elements in the order they were present in nums initially. The remaining elements of 
nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums 
being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums 
being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k

'''
The goal is to modify the list such that each element appears only once, and return 
the length of the modified list.

Code Breakdown

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
```

Explanation

1. Check for an Empty List:
   ```python
   if not nums:
       return 0
   ```
   - The function first checks if `nums` is empty.
   - If the list is empty (`not nums` is `True`), the function returns `0` because 
   there are no elements to process.

2. Initialize `k`:
   ```python
   k = 1
   ```
   - We initialize `k` to `1`. This variable `k` will track the position in the list 
   where the next unique element should be placed.
   - Since the first element is always unique by itself, we start `k` at `1`.

3. Iterate Through the List:
   ```python
   for i in range(1, len(nums)):
   ```
   - We start a loop from the second element (`i = 1`) to the end of the list 
   (`len(nums) - 1`).
   - The loop iterates over each element in the list, comparing it with the previous 
   one.

4. Check for Duplicates:
   ```python
   if nums[i] != nums[i - 1]:
       nums[k] = nums[i]
       k += 1
   ```
   - Within the loop, for each element `nums[i]`, we compare it with the previous 
   element `nums[i - 1]`.
   - If the current element `nums[i]` is not equal to the previous element `nums[i - 1]`, 
   it means it is unique (not a duplicate).
   - We then place this unique element at the `k`-th position (`nums[k] = nums[i]`).
   - After placing the unique element, we increment `k` by `1`.

5. Return the Length of the Modified List:
   ```python
   return k
   ```
   - After the loop completes, `k` will hold the number of unique elements in the list.
   - The function returns `k`, which is the length of the modified list with unique elements.

Example Walkthrough

Let's walk through the code with an example:

```python
nums = [1, 1, 2, 3, 3, 4]
```

Step-by-Step Execution:

1. Initialization:
   - `k = 1`
   - The initial list is `[1, 1, 2, 3, 3, 4]`.

2. Loop Iterations:

   - First iteration (`i = 1`):
     - Compare `nums[1] = 1` with `nums[0] = 1`.
     - Since they are equal, this is a duplicate, so we do nothing and continue to the next 
     iteration.
     - `k` remains `1`.

   - Second iteration (`i = 2`):
     - Compare `nums[2] = 2` with `nums[1] = 1`.
     - Since they are not equal, we have found a unique element.
     - Place `2` at position `k = 1` (`nums[1] = 2`).
     - Increment `k` to `2`.
     - The list now looks like `[1, 2, 2, 3, 3, 4]`.

   - Third iteration (`i = 3`):
     - Compare `nums[3] = 3` with `nums[2] = 2`.
     - Since they are not equal, we have found another unique element.
     - Place `3` at position `k = 2` (`nums[2] = 3`).
     - Increment `k` to `3`.
     - The list now looks like `[1, 2, 3, 3, 3, 4]`.

   - Fourth iteration (`i = 4`):
     - Compare `nums[4] = 3` with `nums[3] = 3`.
     - Since they are equal, this is a duplicate, so we do nothing and continue to 
     the next iteration.
     - `k` remains `3`.

   - Fifth iteration (`i = 5`):
     - Compare `nums[5] = 4` with `nums[4] = 3`.
     - Since they are not equal, we have found another unique element.
     - Place `4` at position `k = 3` (`nums[3] = 4`).
     - Increment `k` to `4`.
     - The list now looks like `[1, 2, 3, 4, 3, 4]`.

3. Return Statement:
   - After the loop, `k = 4`, indicating that the modified list has `4` unique elements.
   - The function returns `4`.

Final Result:
The function modifies the input list `nums` in place so that the first `k` elements 
are the unique elements, and it returns the value `k`, which represents the length of 
this list of unique elements.

For the example `nums = [1, 1, 2, 3, 3, 4]`, the function will return `4`, and the 
modified list will look like `[1, 2, 3, 4, 3, 4]`, but only the first `4` elements 
(`[1, 2, 3, 4]`) are considered valid; the rest can be ignored.

Key Points

- The function works in place, meaning it doesn't use any extra space to create a new 
list; instead, it modifies the input list directly.
- The function assumes that the input list is sorted, which is why the duplicate 
elements are always adjacent.
- The time complexity is `O(n)`, where `n` is the number of elements in the list, 
since we only iterate through the list once.

'''