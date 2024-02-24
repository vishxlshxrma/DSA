'''
Problem statement
You are given an array 'arr' of length 'n' containing integers within the range '1' to 'x'.

Your task is to count the frequency of all elements from 1 to n.

Note:
You do not need to print anything. Return a frequency array as an array in the function such that index 0 represents the 
frequency of 1, index 1 represents the frequency of 2, and so on.
Example:
Input: 'n' = 6 'x' = 9 'arr' = [1, 3, 1, 9, 2, 7]    
Output: [2, 1, 1, 0, 0, 0]
Explanation: Below Table shows the number and their counts, respectively, in the array
Number         Count 
 1                2
 2                1
 3                1
 4                0
 5                0
 6                0

'''

from typing import *
def countFrequency(n: int, x: int, nums: List[int]) -> int:
    freq = [0 for _ in range(n)]

    for i in range(1, n+1):
        for j in range(len(nums)):
            if nums[j] == i:
                freq[i-1] += 1
    return freq

'''
Initialization:
freq = [0 for _ in range(n)]: This line initializes a list called freq with n elements, all set to 0. This list will 
be used to store the frequency of each number from 1 to n.

Nested Loops:
for i in range(1, n+1):: The outer loop iterates over numbers from 1 to n.
for j in range(len(nums)):: The inner loop iterates over the elements in the nums list.

Frequency Counting:
if nums[j] == i:: Inside the inner loop, it checks if the current element in nums is equal to the current number 
from the outer loop (i).
freq[i-1] += 1: If the condition is true, it increments the corresponding frequency count in the freq list. 
The -1 is used because the frequency list is 0-indexed, and the numbers start from 1.

'''