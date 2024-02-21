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

def isPalindrome(string: str) -> bool:
    res = string[::-1]
    if (res == string):
        return True
    else:
        return False