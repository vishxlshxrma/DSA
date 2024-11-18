'''
Problem statement:
You are given an array arr of positive integers. Your task is to find all the leaders in the array. An 
element is considered a leader if it is greater than or equal to all elements to its right. The rightmost 
element is always a leader.

Examples:

Input: arr = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.

Input: arr = [10, 4, 2, 4, 1]
Output: [10, 4, 4, 1]
Explanation: Note that both of the 4s are in output, as to be a leader an equal element is also allowed on 
the right side.

Input: arr = [5, 10, 20, 40]
Output: [40]
Explanation: When an array is sorted in increasing order, only the rightmost element is leader.
'''

class Solution:
    def leaders(self, arr):
        max_right = float('-inf')
        n = len(arr)
        b = []
        
        for i in range(n-1,-1,-1):
            if arr[i]>=max_right:
                b.append(arr[i])
                max_right = arr[i]
                
        b.reverse()
        
        return b


#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends