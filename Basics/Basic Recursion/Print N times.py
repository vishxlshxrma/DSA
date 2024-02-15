'''
Problem statement
You are given an integer 'n'.
Print “Coding Ninjas ” 'n' times, without using a loop.

Example:
Input: 'n'  = 4

Output:
Coding Ninjas Coding Ninjas Coding Ninjas Coding Ninjas 

Explanation: “Coding Ninjas” is printed 4 times. 

'''

from  typing import *

def printNtimes(n: int, current=1) -> List[str]:
    if current <= n:
        return ['Coding Ninjas \t'] + printNtimes(n, current + 1)
    else:
        return []
