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
    def sortColors(self, nums: list[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while (mid <= high):
            if (nums[mid] == 0):
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif (nums[mid] == 1):
                mid += 1
            else:
                nums[mid],nums[high] = nums[high],nums[mid]
                high -= 1
        return nums
    

'''
The Dutch-National Flag Algorithm 
We initalize with 3 pointers and work towards sorting the array based on the pointers.
Time Complexity - O(N)
Space Complexity - O(1)

We basically look for 3 possible cases for 3 values of mid here,

Case 1 → Value of mid is 0
Swap it with low because we want all 0's to be before mid.

Case 2 → Value of mid is 1
Increment mid because 1 is at the correct position it should be.

Case 3 → Value of mid is 2
We swap it with high because we want all 2's to be after high.
'''