'''
Problem Statement:
Given a list arr that contains integers, print the elements of the list with in reverse order with a space between them.

Example 1:
Input: arr = [54, 43, 2, 1, 5]
Output: 5 1 2 43 54
Explanation: Just traverse in reverse and print the numbers.

Example 2:
Input: arr = [324, 5, 2, 2]
Output: 2 2 5 324
Explanation: Just traverse in reverse and print the numbers.

Constraints:
1 ≤ |arr| ≤ 10
1 ≤ arr[i] ≤ 103
'''

def listTraversalReverse(arr):
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=" "if i>0 else "")

'''
Let's break down the solution step-by-step to understand how it traverses and prints the elements of a list
in reverse order.

We are given a list of integers, `arr`. Our goal is to:
1. Start from the last element of the list.
2. Traverse the list backwards.
3. Print every element with a space between them.
4. Avoid modifying the original list.
5. Use O(1) auxiliary space.

Solution Explanation:

Here's the code for reference:

def listTraversalReverse(arr):
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=" " if i > 0 else "")

Step-by-Step Explanation:
1. The function `listTraversalReverse` takes a list `arr` as input.
2. We use a `for` loop to iterate over the indices of the list in reverse order. The `range` function is used to 
generate indices starting from `len(arr) - 1` (the last index) down to `0` (the first index), inclusive.
3. Inside the loop, we access each element of the list using `arr[i]` and print it. The `end` parameter of the `print` 
function is set to a space if the current index `i` is greater than `0`, ensuring that a space is printed after each 
element except for the last one. For the last element (when `i` is `0`), we set `end` to an empty string to avoid 
printing an extra space at the end.
4. This approach does not modify the original list and uses O(1) auxiliary space since we are only using a loop and 
not creating any additional data structures
'''