'''
Problem Statement: Given an integer N, print the following pattern.

Example 1:
Input: N = 3
Output: 
* * *
* * *
* * *

Example 2:
Input: N = 6
Output:
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *

'''

def nForest(n: int) -> None:
    for row in range(n):
        for col in range(n):
            print('* ', end="")
        print('\n',end="")