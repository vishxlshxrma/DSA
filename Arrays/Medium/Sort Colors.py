'''
Problem statement:
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of 
the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.


Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n-1,0,-1):
            for j in range(i):
                if (nums[j]>nums[j+1]):
                    nums[j],nums[j+1] = nums[j+1],nums[j]

        return nums