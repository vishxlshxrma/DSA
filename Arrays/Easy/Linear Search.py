'''
Problem statement:
Given an array arr[] sorted in ascending order of size N and an integer K. 
Check if K is present in the array or not.

Example 1:

Input:
N = 5, K = 6
arr[] = {1,2,3,4,6}
Output: 1
Exlpanation: Since, 6 is present in 
the array at index 4 (0-based indexing),
output is 1.
 

Example 2:

Input:
N = 5, K = 2
arr[] = {1,3,4,5,6}
Output: -1
Exlpanation: Since, 2 is not present 
in the array, output is -1.
'''
#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        count = 0
        for i in range(N):
            if (arr[i] == K):
                return 1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        NK = input().strip().split()
        N = int(NK[0])
        K = int(NK[1])
        A = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.searchInSorted(A, N, K))

# } Driver Code Ends