'''
Problem Statement: Given an integer N, print the following pattern : 

Examples:

Input Format: N = 3
Result: 
*****  
 ***
  *  

Input Format: N = 6
Result:     
***********
 *********
  *******
   ***** 
    ***    
     *

'''

def nStarTriangle(n: int) -> None:
    for row in range(0,n):
        for col in range(0,row):
            print(' ', end="")
        for col in range(0,(2*n-(2*row +1))):
            print('*', end="")
        for col in range(0,row):
            print(' ', end="")
        print()

'''
Note: 
    Imagine the pyramid as a combination of gap-star-gap pattern.
    
    After every line the gap increases by 2 and the number of stars decreases.

    The first loop (for row in range(0, n)) iterates through each row of the triangle, where n is the specified height of the triangle.

    The second loop (for col in range(0, row)) prints spaces before the first '*' in each row. The number of spaces is equal to the current row number.

    The third loop (for col in range(0, (2 * n - (2 * row + 1)))) prints the '' characters in each row. The number of '' characters is determined by the formula 2 * n - (2 * row + 1). 
    This formula creates a pattern where the number of '*' characters decreases as the row number increases.

    The fourth loop (for col in range(0, row)) prints spaces after the '*' characters in each row. The number of spaces is equal to the current row number.

    Finally, print() is used to move to the next line after printing each row, creating the triangular pattern.
    
'''