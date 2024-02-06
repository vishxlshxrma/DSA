'''
Problem Statement: Given an integer N, print the following pattern : 

Examples:

Input Format: N = 3
Result: 
1 2 3
1 2
1

Input Format: N = 6
Result:
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1

'''

def nNumberTriangle(n: int) -> None:
    for row in range(n):
        for col in range(n-row):
            print(col+1, "", end="")
        print('\n', end="")