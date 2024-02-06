'''
Problem Statement: Given an integer N, print the following pattern : 

Examples:

Input Format: N = 3
Result: 
  *  
 *** 
*****   

Input Format: N = 6
Result:
     *     
    ***    
   *****   
  *******  
 ********* 
***********

'''

def nStarTriangle(n: int) -> None:
    gap = n - 1
    stars = 1
    for i in range(n):
        for j in range(gap):
            print(' ', end="")
        for j in range(gap, gap+stars):
            print('*', end="")
        print()
        gap -= 1
        stars += 2

'''
Note: 
    Imagine the pyramid as a combination of gap-star-gap pattern.
    After every line the gap reduces by 2 and the number of stars increases.
    
    Initialization:
        gap: Initially set to n - 1, representing the number of spaces before the stars in the first row.
        stars: Initially set to 1, representing the number of stars in the first row.
    Outer Loop (`for i in range(n)'):
        This loop controls the number of rows in the triangle. It iterates n times.
        
    Leading Spaces (`for j in range(gap)'):
        This loop prints leading spaces before the stars. The number of spaces (gap) decreases with each row.

    Stars (`for j in range(gap, gap + stars)'):
        This loop prints the stars. It starts from gap and goes up to gap + stars - 1.

    Newline (print()):
        After printing the spaces and stars for a row, a newline is printed to move to the next row.

    Adjusting gap and stars:
        gap is decreased by 1 after each row to adjust the spacing.
        stars is increased by 2 after each row to add more stars in the next row.

'''