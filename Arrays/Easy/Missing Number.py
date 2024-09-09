'''
Problem statement:
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range 
that is missing from the array.
 
Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number 
in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number 
in the range since it does not appear in nums.
'''
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len (nums)

        s1 = (n)*(n+1)/2

        s2 = sum(nums)

        return int(s1-s2)

'''
Since, the sum of n numbers is n*(n+1)/2, we simply take the sum of n numbers and subtract the corresponding
sum of the array, to get the required missing number.
'''