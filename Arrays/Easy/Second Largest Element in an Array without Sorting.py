'''
Problem statement:
Given an array arr, return the second largest distinct element from an array. 
If the second largest element doesn't exist then return -1.

Examples:

Input: arr = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr = [10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element 
does not exist so answer is -1.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

'''

#User function Template for python3
class Solution:
    def print2largest(self, arr):
        largest = 0
        SecLargest = -1
        for i in range (len(arr)):
            if (arr[i] > largest):
                largest = arr[i]
        for j in range (len(arr)):
            if (arr[j] > SecLargest and arr[j] != largest):
                SecLargest = arr[j]
        return SecLargest


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends