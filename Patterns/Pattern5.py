'''
Problem Statement: Given an integer N, print the following pattern : 

Examples:

Input Format: N = 3
Result: 
* * *
* * 
*

Input Format: N = 6
Result:
* * * * * *
* * * * * 
* * * * 
* * * 
* * 
* 

'''

def seeding(n: int) -> None:
    for row in range(n):
        for col in range(n-row):
            print('* ', end="")
        print('\n', end="")