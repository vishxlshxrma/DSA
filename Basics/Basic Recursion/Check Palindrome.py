'''
Problem statement
Determine if a given string 'S' is a palindrome using recursion. Return a Boolean value of true 
if it is a palindrome and false if it is not.

Note: You are not required to print anything, just implement the function. 

Example:
Input: s = "racecar"

Output: true

Explanation: "racecar" is a palindrome.

'''

class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(char.lower() for char in s if char.isalnum())
        def helper(start, end):
            if (start >= end):
                return True
            if (s[start] != s[end]):
                return False
            return helper(start + 1, end - 1)
        return helper (0, len(s) - 1)
    
'''
s = ''.join(char.lower() for char in s if char.isalnum())
Keep only alphanumeric and lowercase everything
'''