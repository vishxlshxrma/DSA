'''
Problem statement:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority 
element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

# Solution 1 -> Using Dictionary

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        b = {}
        max_element = 0
        for i in nums:
            if (i in b):
                b[i] += 1
            else:
                b[i] = 1
        max_element = max(b, key=b.get)

        return max_element
    
# Solution 2 -> Using Boyer-Moore Voting Algorithm

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None

        for i in nums:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
    

'''
The Boyer-Moore Voting Algorithm is an efficient algorithm to find the majority element in an array. A 
majority element is defined as an element that appears more than ⌊n / 2⌋ times, where `n` is the size of the 
array. This algorithm works in **O(n)** time and uses **O(1)** space, making it optimal for this problem.

Key Idea of Boyer-Moore Voting Algorithm:

The main idea is based on the concept of "voting" — each element can be thought of as voting for itself. If 
the same element keeps appearing, it gains "votes," but when a different element appears, it "cancels out" a 
vote from the majority element. If there's a majority element in the array (appearing more than ⌊n / 2⌋ times), 
it will be the last element remaining with a positive count after all cancellations.

Algorithm Steps:

1. Initialize Count and Candidate:
   - Start with `count = 0` and `candidate = None`.
   - `count` will keep track of the "net votes" for the candidate.
   - `candidate` will be the potential majority element.

2. Traverse the Array:
   - For each element in the array:
     - If `count` is 0, set the `candidate` to the current element and set `count = 1`.
     - If the current element is the same as `candidate`, increment `count` by 1 (representing a vote for the 
     candidate).
     - If the current element is different from `candidate`, decrement `count` by 1 (representing a vote 
     against the candidate).

3. Return the Candidate:
   - After the loop completes, the `candidate` variable will hold the majority element.

Code for Boyer-Moore Voting Algorithm:

```python
def majorityElement(nums):
    count = 0
    candidate = None

    Step 1: Find the candidate for the majority element
    for num in nums:
        if count == 0:
            candidate = num  # Set the current element as the new candidate
        count += (1 if num == candidate else -1)  # Increment or decrement count

    Step 2: Return the candidate as the majority element
    return candidate
```

Example Walkthrough:

Let's go through an example array step-by-step to see how the algorithm works.

```python
nums = [2, 2, 1, 1, 2, 2, 2]
```

1. Initial State:
   - `count = 0`
   - `candidate = None`

2. First Iteration (`num = 2`):
   - `count` is 0, so set `candidate = 2`.
   - Increment `count` to 1.

3. Second Iteration (`num = 2`):
   - `num` is equal to `candidate` (2), so increment `count` to 2.

4. Third Iteration (`num = 1`):
   - `num` is not equal to `candidate` (2), so decrement `count` to 1.

5. Fourth Iteration (`num = 1`):
   - `num` is not equal to `candidate` (2), so decrement `count` to 0.

6. Fifth Iteration (`num = 2`):
   - `count` is 0, so set `candidate = 2`.
   - Increment `count` to 1.

7. Sixth Iteration (`num = 2`):
   - `num` is equal to `candidate` (2), so increment `count` to 2.

8. Seventh Iteration (`num = 2`):
   - `num` is equal to `candidate` (2), so increment `count` to 3.

Final Result:
After iterating through the entire array, the `candidate` is `2`, which is indeed the majority element.

Why Boyer-Moore Works:
- The algorithm relies on canceling out votes between the majority element and all other elements.
- By the end of the array, if a majority element exists, it will be the only one that hasn't been fully 
canceled out, leaving it as the `candidate`.
- This method ensures that we only make a single pass through the array, achieving O(n) time complexity with 
no additional storage for counting elements.

Summary:

- Advantages: Efficient with O(n) time and O(1) space complexity.
- Limitations: Only works when a majority element is guaranteed to exist.
'''