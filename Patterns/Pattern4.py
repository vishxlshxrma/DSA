'''
Problem Statement: Given an integer N, print the following pattern : 

Examples:

Input Format: N = 3
Result: 
1
2 2 
3 3 3

Input Format: N = 6
Result:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6

'''

def triangle( n:int) ->None:
    for row in range(n):
        for col in range(row+1):
            print(row+1, "", end="")
        print('\n', end="")