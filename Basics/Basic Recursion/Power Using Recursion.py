'''
Problem Statement:
You are given two numbers n and p. You need to find np.

Example 1:
Input: n = 9, p = 9 
Output: 387420489
Explanation: 9 raised to power 9 is 387420489.

Example 2:
Input: n = 2, p = 9
Output: 512
Explanation: 2 raised to power 9 is 512.
'''

class Solution:
    def recursivePower(self, n, p):
        if (p == 0):
            return 1
        
        return n * self.recursivePower(n,p-1)