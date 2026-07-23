'''
Problem Statement:
Given a number n find the prime factorization of the number.
Note: Print the prime factors in non-decreasing order.

Example 1:
Input: n = 100
Output: 2 2 5 5
Explanation: 100 = 2 * 2 * 5 * 5

Example 2:
Input: n = 27
Output: 3 3 3
Explanation: 27 = 3 * 3 * 3 

'''

class Solution:
    def printPrimeFactorization(self, n):
        for i in range(2, int(n**0.5) + 1):
            while(n % i == 0):
                print(i, end=" ")
                n = n // i
        
        if (n > 1):
            print(n, end=" ")