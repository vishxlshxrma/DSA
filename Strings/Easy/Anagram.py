'''
Problem Statement:
Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams 
of each other or not.
Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of 
their order.

Example 1:
Input: s1 = "geeks" s2 = "kseeg"
Output: true 
Explanation: Both the string have same characters with same frequency. So, they are anagrams.

Example 2:
Input: s1 = "allergy", s2 = "allergyy" 
Output: false 
Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. Since the frequency of 
characters differs, the strings are not anagrams. 

Example 3:
Input: s1 = "listen", s2 = "lists" 
Output: false 
Explanation: The characters in the two strings are not the same — some are missing or extra. So, they are not anagrams.
'''

class Solution:
    def areAnagrams(self, s1, s2):
        counts1 = {}
        for ch in s1:
            if ch in counts1:
                counts1[ch] += 1
            else:
                counts1[ch] = 1
        
        counts2 = {}
        for i in s2:
            if i in counts2:
                counts2[i] += 1
            else:
                counts2[i] = 1
                
        if (counts1 == counts2):
            return True
        
        else:
            return False