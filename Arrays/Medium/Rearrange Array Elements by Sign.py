'''
Problem statement:
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and 
negative integers.
You should return the array of nums such that the the array follows the given conditions:

1) Every consecutive pair of integers have opposite signs.
2) For all integers with the same sign, the order in which they were present in nums is preserved.
3) The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.


Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not 
satisfy one or more conditions.  
Example 2:

Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].
'''

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos = []
        neg = []

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
            
        ans = []
        for a,b in zip(pos,neg):
            ans.append(a)
            ans.append(b)
        
        return ans
    
'''
The `zip()` function is used to pair elements from the two arrays (`a` and `b`) by their index. It allows us 
to iterate through both arrays simultaneously, combining their elements alternately.

How `zip()` Works Here:

Given:
```python
a = [1, 2, 3]
b = [4, 5, 6]
```

Using `zip(a, b)`:
- It creates pairs: `(1, 4)`, `(2, 5)`, `(3, 6)`.
- These pairs are then used to append the elements alternately into the result array `c`.

Code with `zip()`:

```python
for x, y in zip(a, b):
    result.append(x)  # Add element from 'a'
    result.append(y)  # Add element from 'b'
```

Result:

- Iteration 1: Add `1` from `a` and `4` from `b`.
- Iteration 2: Add `2` from `a` and `5` from `b`.
- Iteration 3: Add `3` from `a` and `6` from `b`.

Output:

```python
c = [1, 4, 2, 5, 3, 6]
```
The `zip()` function simplifies handling the two arrays together, making the code concise and readable.
'''