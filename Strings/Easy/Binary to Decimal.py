'''
Problem Statement:
Given a string b representing a binary number, return its decimal equivalent as an integer.

Example 1:
Input : b = 111
Output : 7
Explanation : The decimal equivalent of the binary number 111 is 22 + 21 + 20 = 7.

Example 2:
Input : b = 1010
Output : 10
Explanation : The decimal equivalent of the binary number 1010 is 23 + 21 = 10.

Example 3:
Input: b = 100001
Output: 33
Explanation : The decimal equivalent of the binary number 100001 is 25 + 20 = 33.

Constraints:
1 <= number of bits in binary number  <= 16
'''

class Solution:
    def binaryToDecimal(self, b):
        ans = 0
        for num in b:
            ans = ans * 2 + int(num)
        return ans