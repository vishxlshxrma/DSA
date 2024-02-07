'''
Problem statement
You are given a number ’n’.
Find the number of digits of ‘n’ that evenly divide ‘n’.

Note:
A digit evenly divides ‘n’ if it leaves no remainder when dividing ‘n’.

Example:
Input: ‘n’ = 336

Output: 3

Explanation:
336 is divisible by both ‘3’ and ‘6’. Since ‘3’ occurs twice it is counted two times.

'''

def countDigits(n: int) -> int:
    a = str(n)
    b = len(a)
    count = 0
    for i in a:
         if int(i) != 0 and n % int(i) == 0:
            count += 1
    return count