'''
Problem statement
You are given an integer 'n'.
Your task is determining the sum of the first 'n' natural numbers and returning it.



Example:
Input: 'n' = 3

Output: 6

Explanation: The sum of the first 3 natural numbers is 1 + 2 + 3, equal to 6.

'''

from typing import List

class Solution:
    sum = 0
    def NnumbersSum(self, N):
        if (N <= 0):
            return 0
        return N + self.NnumbersSum(N-1)