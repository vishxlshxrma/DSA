'''
Problem statement
Given an array 'v' of 'n' numbers.
Your task is to find and return the highest and lowest frequency elements.

If there are multiple elements that have the highest frequency or lowest frequency, pick the smallest element.

Example:
Input: 'n' = 6, 'v' = [1, 2, 3, 1, 1, 4]

Output: 1 2

Explanation: The element having the highest frequency is '1', and the frequency is 3. The elements with the lowest frequencies are '2', '3', and '4'. 
Since we need to pick the smallest element, we pick '2'. Hence we return [1, 2].

'''

from collections import Counter
from typing import List

def getFrequencies(v: List[int]) -> List[int]:
    
    freq = Counter(v)

    maxFreq = 0
    minFreq = float('inf')
    maxElement = 0
    minElement = float('inf')
    
 
    for element, count in freq.items():
        if count > maxFreq:
          
            maxElement = element
            maxFreq = count
        elif count == maxFreq:
           
            maxElement = min(maxElement, element)
        
        if count < minFreq:
            
            minElement = element
            minFreq = count
        elif count == minFreq:
            
            minElement = min(minElement, element)
    
    ans = [maxElement, minElement]
    return ans


'''
The function `getFrequencies` takes a list of integers `v` and returns a list containing two elements: the integer that occurs 
most frequently and the integer that occurs least frequently.
Here's a breakdown of how the function works:

1. It imports the `Counter` class from the `collections` module, which is used to count the occurrences of elements in the list.
2. It initializes variables `maxFreq`, `minFreq`, `maxElement`, and `minElement` to keep track of the maximum and minimum 
frequencies and their corresponding elements.
3. It uses the `Counter` class to count the frequencies of elements in the list `v`.
4. It iterates through the items in the frequency dictionary (`freq`).
5. For each element, it updates `maxElement` and `maxFreq` if the count is greater than the current maximum frequency, 
or if the count is equal to the current maximum frequency, it updates `maxElement` to the smaller of the two elements.
6. Similarly, it updates `minElement` and `minFreq` if the count is less than the current minimum frequency, 
or if the count is equal to the current minimum frequency, it updates `minElement` to the smaller of the two elements.
7. It constructs a list `ans` containing `maxElement` and `minElement` and returns it.

The function effectively finds the elements with the highest and lowest frequencies in the input list `v` and 
returns them in a list.

'''