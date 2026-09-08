'''
Problem Statement:
Given an integer array arr[] and an integer k, find and return the kth smallest element in the given array.
Note: The kth smallest element is determined based on the sorted order of the array.

Example 1:
Input: arr[] = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
Output: 5
Explanation: 4th smallest element in the given array is 5.

Example 2:
Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output: 7
Explanation: 3rd smallest element in the given array is 7.

'''

import heapq

class Solution:
    
    def kthSmallest(self, arr, k):
        heapq.heapify(arr)
        
        while k > 1:
            heapq.heappop(arr)
            k -= 1
            
        return arr[0]
