'''
Problem statement
There is a song concert going to happen in the city. 
The price of each ticket is equal to the number obtained after reversing the bits of a given 32 bits unsigned integer ‘n’.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
0
12
Sample Output 1:
 0
 805306368
Explanation For Sample Input 1 :
For the first test case :
Since the given number N = 0 is represented as 00000000000000000000000000000000 in its binary representation. 
So after reversing the bits, it will become 00000000000000000000000000000000 which is equal to 0 only. 
So the output is 0.     

For the second test case :
Since the given number N = 12 is represented as 00000000000000000000000000001100 in its binary representation. 
So after reversing the bits, it will become 0110000000000000000000000000000, which is equal to 805306368 only. 
So the output is 805306368.

'''

def reverseBits(n):
    y = bin(n)[2:]
    k = y.zfill(32)

    if (n >= 0):
        a = str(k)
        b = list(a)
        c = [eval(i) for i in b]
        d = len(c)
        e = []
        for i in range(d-1,-1,-1):
            e.append(c[i])

        f = ''.join([str(elem) for elem in e])
        g = int(f,2)
        return g

    else:
        k = abs(k)
        a = str(k)
        b = list(a)
        c = [eval(i) for i in b]
        d = len(c)
        e = []
        for i in range(d-1,-1,-1):
            e.append(c[i])

        f = ''.join([str(elem) for elem in e])
        g = int(f,2)
        g = -abs(g)
        return g
    
'''

1. `bin(n)[2:]`: Converts the integer `n` to its binary representation as a string, and `[2:]` is used to remove the '0b' prefix.
2. `y.zfill(32)`: Fills the binary string `y` with leading zeros to make its length 32. This ensures that the binary 
representation is a 32-bit string.

The code then checks if `n` is non-negative or negative and processes accordingly:

3. `str(k)`: Converts the 32-bit binary string `k` back to a regular string.
4. `list(a)`: Converts the string `a` to a list of individual characters.
5. `[eval(i) for i in b]`: Creates a new list `c` by evaluating each character in the list `b`. 
    This converts each character (0 or 1) to an integer.

The code then proceeds to reverse the list of bits:

6. `len(c)`: Gets the length of the list `c`.
7. The `for` loop iterates through the elements of `c` in reverse order and appends them to the list `e`.

After reversing the bits, the code converts the reversed binary string back to an integer:

8. `''.join([str(elem) for elem in e])`: Joins the elements of the list `e` into a single string.
9. `int(f, 2)`: Converts the binary string `f` to an integer using base 2.

Finally, the function returns the reversed integer:

10. For negative integers, the function reverses the bits similarly to the non-negative case and adds a negative sign to the result.

Note: The use of `eval()` in this code is not strictly necessary and may be considered unsafe. 
You can achieve the same result more safely using `int(i)` instead of `eval(i)`.

'''