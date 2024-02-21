'''
Problem statement
Given an integer 'n', return first n Fibonacci numbers using a generator function.

Example:
Input: 'n' = 5

Output: 0 1 1 2 3

Explanation: First 5 Fibonacci numbers are: 0, 1, 1, 2, and 3.

Note:
You don't need to print anything. Just implement the given function.

'''

from typing import List

def generateFibonacciNumbers(n: int) -> List[int]: 
    a = [0]
    b = [0,1]
    if (n <= 1):
        return a
    if (n >= 2):
        for i in range(1,n-1):
            b.append(b[i]+b[i-1])
        return b