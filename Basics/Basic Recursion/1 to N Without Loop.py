'''
Problem statement
You are given an integer 'n'.
Your task is to return an array containing integers from 1 to 'n' (in increasing order) without using loops.

Example:
Input: 'n' = 5

Output: 1 2 3 4 5

Explanation: An array containing integers from '1' to 'n' is [1, 2, 3, 4, 5].

'''

class Solution:
    def printTillN(self, n):
        if (n == 0):
            return 0
        
        self.printTillN(n-1)
        print(n, end=" ")