'''
Problem Statement:
You are given a list that contains integers. You need to print the elements of the list with a space between them.
Note: Add a new line at the end.

Example 1:
Input: arr[] = [54, 43, 2, 1, 5]
Output: 54 43 2 1 5
Explanation: Just traverse and print the numbers.

Example 2:
Input: arr[] = [324, 5, 2, 2]
Output: 324 5 2 2
Explanation: Just traverse and print the numbers.
'''

def listTraversal(arr):
    for i in arr:
        print(i, end = " ")
    print()