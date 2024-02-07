'''
Problem statement
You are given two integers 'n', and 'm'.

Calculate 'gcd(n,m)', without using library functions.

Note:
The greatest common divisor (gcd) of two numbers 'n' and 'm' is the largest positive number 
that divides both 'n' and 'm' without leaving a remainder.

Example:
Input: 'n' = 6, 'm' = 4

Output: 2

Explanation:
Here, gcd(4,6) = 2, because 2 is the largest positive integer that divides both 4 and 6.

'''

def calcGDC(n:int, m: int) -> int:

    a = []
    for i in range(1,n+1):
        if(n%i == 0):
            a.append(i)
    b = []
    for j in range(1,m+1):
        if(m%j == 0):
            b.append(j)
    
    a_set = set(a)
    b_set = set(b)
    common_elements = a_set & b_set
    
    if common_elements:
        return max(common_elements) 
    else:
        return 1
    

'''
if common_elements:
        return max(common_elements) 

common elements is an in-built funtion to calculate common elements between 2 sets.

'''