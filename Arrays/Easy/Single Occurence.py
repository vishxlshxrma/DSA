'''
Problem statement:
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

'''
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        n = len(nums)
        dt = {}

        for i in nums:
            if (i in dt):
                dt[i] += 1
            else:
                dt[i] = 1
            
        for key in dt:
            if (dt[key] == 1):
                return key