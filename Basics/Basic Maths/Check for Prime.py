'''
Problem statement:
A prime number is a positive integer that is divisible by exactly 2 integers, 
1 and the number itself.

You are given a number 'n'.
Find out whether 'n' is prime or not.

Example :
Input: 'n' = 5

Output: YES

Explanation: 5 is only divisible by 1 and 5. 2, 3 and 4 do not divide 5.

'''

n = int(input())
a = 0
if (n == 1):
    print('NO')
else:
    for i in range(2,n):
        if (n % i == 0):
            a += i
    if (a == 0):
        print('YES')
    else:
        print('NO')