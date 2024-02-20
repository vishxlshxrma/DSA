'''
Problem statement
Given an array 'arr' of size 'n'.
Return an array with all the elements placed in reverse order.

Note:
You don't need to print anything. Just implement the given function.
Example:
Input: n = 6, arr = [5, 7, 8, 1, 6, 3]

Output: [3, 6, 1, 8, 7, 5]

Explanation: After reversing the array, it looks like this [3, 6, 1, 8, 7, 5].

'''

from typing import *

def reverseArray(n: int, nums: List[int]) -> List[int]:
    return nums[::-1]