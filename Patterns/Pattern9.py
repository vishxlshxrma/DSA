'''
Problem Statement: Given a number n, print Floyd's triangle with n lines.

Floyd’s Triangle is a pattern of consecutive natural numbers arranged in rows, where the i-th row contains i numbers.

Examples:

Input: n = 4
Output:
1
2 3
4 5 6
7 8 9 10
Explanation: The triangle has 4 rows. Numbers start from 1 and increase sequentially across rows, and each row i contains i elements.

Input: n = 5 
Output:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
Explanation: The triangle has 4 rows, and each row i contains i numbers.
Constraints:
1 <= n <= 100

'''

n = int(input())

# code here
a = 1
for row in range(n):
    for col in range(row+1):
        print(a, "", end="")
        a+=1
    print('\n',end="")