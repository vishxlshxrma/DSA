'''
Problem statement:
You are given an integer 'n'.
Function 'sumOfDivisors(n)' is defined as the sum of all divisors of 'n'.
Find the sum of 'sumOfDivisors(i)' for all 'i' from 1 to 'n'.

Example:
Input: 'n'  = 5

Output: 21

Explanation:
We need to find the sum of 'sumOfDivisors(i)' for all 'i' from 1 to 5. 
'sumOfDivisors(1)' = 1
'sumOfDivisors(2)' = 2 + 1 = 3
'sumOfDivisors(3)' = 3 + 1 = 4
'sumOfDivisors(4)' = 4 + 2 +1 = 7 
'sumOfDivisors(5)' = 5 + 1 = 6
Therefore our answer is sumOfDivisors(1) + sumOfDivisors(2) + sumOfDivisors(3) + sumOfDivisors(4) + sumOfDivisors(5) = 1 + 3 + 4 + 7 + 6 = 21.

'''

def sumOfDivisors(n: int) -> int:
    sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            sum += i
    return sum

def sumOfAllDivisors(n: int) -> int:
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += sumOfDivisors(i)
    return total_sum
    

'''
This function sumOfDivisors(n) calculates the sum of all divisors of the number n. 
It iterates through all numbers from 1 to n, checks if n is divisible by i without 
a remainder (i.e., if n % i == 0), and if so, adds i to the running total sum. 
Finally, it returns the total sum of divisors.

This function sumOfAllDivisors(n) computes the sum of the sum of divisors for all 
numbers from 1 to n. It iterates through all numbers from 1 to n, calculates the sum 
of divisors for each number using the sumOfDivisors function, and accumulates these 
sums into the total_sum variable. Finally, it returns the total sum of the sums of divisors.
'''