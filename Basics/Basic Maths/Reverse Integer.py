'''
Problem statement:
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value 
to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

'''

class Solution:
    def reverse(self, x: int) -> int:
        [int_min, int_max] = [-2**31, 2**31 - 1]
        if (int_min < x < int_max):
            if (x >= 0):
                a = str(x)
                b = list(a)
                c = [eval(i) for i in b]
                d = len(c)
                e = []
                for i in range(d-1,-1,-1):
                    e.append(c[i])

                f = ''.join([str(elem) for elem in e])
                g = int(f)
                if (int_min < g < int_max):
                    return g
                else:
                    return 0
            else:
                x = abs(x)
                a = str(x)
                b = list(a)
                c = [eval(i) for i in b]
                d = len(c)
                e = []
                for i in range(d-1,-1,-1):
                    e.append(c[i])

                f = ''.join([str(elem) for elem in e])
                g = int(f)
                g = -abs(g)
                if (int_min < g < int_max):
                    return g
                else:
                    return 0
        else:
            return 0
        
'''

''.join([str(elem) for elem in e]) is used to join the different elements of an array into one single
string.
Example: if array is [1,2,3] then upon applying the function, it'll become '123'.

'''