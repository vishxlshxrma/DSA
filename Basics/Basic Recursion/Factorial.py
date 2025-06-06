'''
Problem statement
Given a positive integer, n. Find the factorial of n.
The factorial number is a factorial of a positive integer, like 24 is a factorial number, 
as it is a factorial of 4.

Example:
Input: n = 5
Output: 120
Explanation: 1 x 2 x 3 x 4 x 5 = 120
'''

class Solution:
    def factorial (self, n):
        if (n <= 1):
            return 1
        return n * self.factorial(n-1)