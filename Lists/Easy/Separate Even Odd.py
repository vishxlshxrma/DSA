'''
Problem Statement:
Given a list arr that contains integers, return two lists, one of even numbers and other of odd numbers.

Example 1:
Input: arr = [54, 43, 2, 5, 14, 17, 18, 9]
Output: 
54 2 14 18
43 5 17 19
Explanation: First line in output contains list of even numbers and second line contains list  of add numbers.

Example 2:
Input: arr = [5, 6, 7, 2, 4, 8, 9]
Output: 
6 2 4 8
5 7 9

Constraints:i
1 ≤ |arr| ≤ 100
0 ≤ arr[i] ≤ 100
'''
def evenOdd(arr):
    even = []
    odd = []
    
    for i in arr:
        if(i % 2 == 0):
            even.append(i)
        else:
            odd.append(i)
    
    return even,odd