'''
Problem statement
You are given an integer 'n'.
Your task is to return a sorted array (in increasing order) containing all the 
factorial numbers which are less than or equal to 'n'.
The factorial number is a factorial of a positive integer, like 24 is a factorial number, 
as it is a factorial of 4.

Note:
In the output, you will see the array returned by you.
Example:
Input: 'n' = 7

Output: 1 2 6

Explanation: Factorial numbers less than or equal to '7' are '1', '2', and '6'.

'''

from typing import *
import math

def factorialNumbers(n: int) -> List[int]:
    a = []
    i = 1
    while (math.factorial(i) <= n):
        a.append(math.factorial(i))
        i += 1
    return a

'''

math.factorial(i) is an inbuilt function to calculate the factorial of number 'i'.
It is in the module 'math'.

'''