'''
Problem statement
You are given an integer 'n'.
Your task is to return an array containing integers from 'n' to '1' (in decreasing order) without using loops.

Note:
In the output, you will see the array returned by you.

Example:
Input: 'n' = 5

Output: 5 4 3 2 1

Explanation: An array containing integers from 'n' to '1' is [5, 4, 3, 2, 1].

'''

from typing import List

def printNos(x: int) -> List[int]:
    if (x == 1):
        return [x]
    else:
        return [x] + printNos(x-1)