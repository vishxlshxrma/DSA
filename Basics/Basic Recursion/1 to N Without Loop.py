'''
Problem statement
You are given an integer 'n'.
Your task is to return an array containing integers from 1 to 'n' (in increasing order) without using loops.

Example:
Input: 'n' = 5

Output: 1 2 3 4 5

Explanation: An array containing integers from '1' to 'n' is [1, 2, 3, 4, 5].

'''

from typing import List
a = 1
b = []
def printNos(x: int) -> List[int]: 
    global a
    if a != x+1:
        b.append(a)
        a += 1
        printNos(x)
    return b