'''
Problem Statement: Given an integer N, print the following pattern : 

Examples:

Input Format: N = 3
Result: 
* 
* * 
* * *

Input Format: N = 6
Result:
* 
* * 
* * *
* * * *
* * * * *
* * * * * *

'''

def nForest(n:int) ->None:
    for row in range(n):
        for col in range(row+1):
            print('* ', end="")
        print('\n', end="")