'''
Problem statement:
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and 
negative integers.
You should return the array of nums such that the the array follows the given conditions:

1) Every consecutive pair of integers have opposite signs.
2) For all integers with the same sign, the order in which they were present in nums is preserved.
3) The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.


Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not 
satisfy one or more conditions.  
Example 2:

Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].
'''

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        po = 0
        ne = 1

        result = [0] * len(nums)

        for i in nums:
            if (i >= 0):
                result[po] = i
                po += 2
            if (i < 0):
                result[ne] = i
                ne += 2

        return result