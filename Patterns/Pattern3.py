'''
Problem Statement: Given an integer N, print the following pattern : 

Examples:

Input Format: N = 3
Result: 
1
1 2 
1 2 3

Input Format: N = 6
Result:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6

'''

def nTriangle(n:int) ->None:
    for row in range(n):
        for col in range(row+1):
            print(col+1, "", end="")
        print('\n', end="")