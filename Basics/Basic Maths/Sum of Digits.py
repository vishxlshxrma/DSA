'''
Problem Statement:
Given a positive number n. Find the sum of all the digits of n.

Example 1:
Input: n = 687
Output: 21
Explanation: Sum of 687's digits: 6 + 8 + 7 = 21

Example 2:
Input: n = 12
Output: 3
Explanation: Sum of 12's digits: 1 + 2 = 3

'''

class Solution:
    def sumOfDigits(self, n):
        sum = 0
        a = str(n)
        
        for i in a:
            sum = sum + int(i)
        return sum