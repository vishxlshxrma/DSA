'''
Problem statement:
Given an array, arr. The task is to find the largest element in it.

Examples:

Input: arr = [1, 8, 7, 56, 90]
Output: 90
Explanation: The largest element of the given array is 90.
Input: arr = [5, 5, 5, 5]
Output: 5
Explanation: The largest element of the given array is 5.
Input: arr = [10]
Output: 10
Explanation: There is only one element which is the largest.
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)

Constraints:
1 <= arr.size()<= 106
0 <= arr[i] <= 106

'''


from typing import List


class Solution:
    def largest(self, arr : List[int]) -> int:
        a = arr[0]
        for i in range (1,len(arr)):
            if (arr[i] > a):
                a = arr[i]
        return a
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().split()))

        obj = Solution()
        res = obj.largest(arr)

        print(res)

# } Driver Code Ends