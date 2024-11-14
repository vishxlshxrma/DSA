'''
Problem statement:
Given an array arr[], with 0-based indexing, select any two indexes, i and j such that i < j. From the 
subarray arr[i...j], select the smallest and second smallest numbers and add them, you will get the score 
for that subarray. Return the maximum possible score across all the subarrays of array arr[].

Examples :

Input : arr[] = [4, 3, 1, 5, 6]
Output : 11
Explanation : Subarrays with smallest and second smallest are:- [4, 3] smallest = 3,second smallest = 4
[4, 3, 1] smallest = 1, second smallest = 3
[4, 3, 1, 5] smallest = 1, second smallest = 3
[4, 3, 1, 5, 6] smallest = 1, second smallest = 3
[3, 1] smallest = 1, second smallest = 3
[3, 1, 5] smallest = 1, second smallest = 3
[3, 1, 5, 6] smallest = 1, second smallest = 3
[1, 5] smallest = 1, second smallest = 5
[1, 5, 6] smallest = 1, second smallest = 5
[5, 6] smallest = 5, second smallest = 6
Maximum sum among all above choices is, 5 + 6 = 11.

'''

# Brute Force Approach is to print all sub-arrays, then select the minimum 2 elements from each subarray and
# then compare all sums and check for the maximum answer.

class Solution:
    def pairWithMaxSum(self, arr):
        maxi = 0
        sub = []
        
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                sub = arr[i:j+1]
                sub.sort()
                if (len(sub)>1):
                    b = int(sub[0] + sub[1])
                else:
                    b = min(sub)
                if maxi<b:
                    maxi = b
        return maxi
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.pairWithMaxSum(a))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends


# More Optimized Solution is to simply calculate the sum of next 2 consecutive elements .

#User function Template for python3

class Solution:
    def pairWithMaxSum(self, arr):
        maxi = 0
        
        for i in range(len(arr) - 1):
            cur_sum = arr[i] + arr[i+1]
            
            if (cur_sum > maxi):
                maxi = cur_sum
        return maxi
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.pairWithMaxSum(a))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends

'''
This approach works because first it is asking for subarray so it must be contiguos and 2nd that as soon 
as we take the subarray size greater than 2 and find the smallest and 2nd smallest their 
sum always< the greater element and its adjacent in that subarray; You can take any array any array and 
dry run you find the logic.
'''