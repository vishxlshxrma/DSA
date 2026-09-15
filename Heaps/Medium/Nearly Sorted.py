'''
Problem Statement:
Given an array arr[], where each element is at most k positions away from its correct position in the sorted order.
Your task is to restore the sorted order of arr[] by rearranging the elements in place.

Note: Don't use any sort() method.

Example 1:
Input: arr[] = [2, 3, 1, 4], k = 2
Output: [1, 2, 3, 4]
Explanation: All elements are at most k = 2 positions away from their correct positions.
Element 1 moves from index 2 to 0
Element 2 moves from index 0 to 1
Element 3 moves from index 1 to 2
Element 4 stays at index 3

Example 2:
Input: arr[]= [7, 9, 14], k = 1
Output: [7, 9, 14]
Explanation: All elements are already stored in the sorted order.

'''

import heapq

class Solution:
    def nearlySorted(self, arr, k):
        heap = []
        
        for i in range(min(k+1, len(arr))):
            heapq.heappush(heap,arr[i])
        
        index = 0
        
        for i in range(k+1,len(arr)):
            arr[index] = heapq.heappop(heap)
            index += 1
            heapq.heappush(heap,arr[i])
            
        while heap:
            arr[index] = heapq.heappop(heap)
            index += 1