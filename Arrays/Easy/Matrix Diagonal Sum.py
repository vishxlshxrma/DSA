'''
Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that 
are not part of the primary diagonal.

Example 1:
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Example 2:
Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Example 3:
Input: mat = [[5]]
Output: 5
'''
class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        total = 0

        for i in range(n):
            total += mat[i][i]
            
            if (i != n-1-i):
                total += mat[i][n-1-i]

        return total

'''
Code Explanation:
The goal is to calculate the sum of both diagonals of a square matrix without counting the center element twice.
Instead of traversing every element of the matrix using nested loops, we can directly access the diagonal elements 
using their row and column indices.
This allows us to solve the problem using only one loop.

Let's break down the solution step by step.

Step-by-Step Explanation:

Find the Size of the Matrix:

n = len(mat)

len(mat) returns the number of rows in the matrix.

Since the problem guarantees a square matrix, the number of rows and columns is equal.

Therefore, n represents both the number of rows and columns.

For example:

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Here:

n = 3

The matrix has 3 rows and 3 columns.

Initialize the Total Sum:

total = 0

This variable stores the sum of all diagonal elements encountered so far.

Initially, no elements have been processed, so total starts at 0.

Traverse the Matrix Rows:

for i in range(n):

The loop runs from 0 to n - 1.

The variable i represents the current row index.

For each row, we calculate the positions of the primary and secondary diagonal elements.

For a 3 x 3 matrix:

i = 0
i = 1
i = 2

Notice that we do not need nested loops because each row contains exactly one primary diagonal element and one secondary 
diagonal element.

Calculate the Primary Diagonal Sum:

total += mat[i][i]

The primary diagonal runs from the top-left corner to the bottom-right corner.

Its defining property is that the row index equals the column index.

Therefore:

row = i
column = i

For example:

Matrix:

1  2  3
4  5  6
7  8  9

The primary diagonal contains:

mat[0][0] = 1
mat[1][1] = 5
mat[2][2] = 9

Therefore:

Primary diagonal sum = 1 + 5 + 9 = 15

The expression:

mat[i][i]

automatically accesses the correct primary diagonal element during every iteration.

Calculate the Secondary Diagonal Position:

The secondary diagonal runs from the top-right corner to the bottom-left corner.

For the same matrix:

1  2  3
4  5  6
7  8  9

The secondary diagonal contains:

3
5
7

Their positions are:

mat[0][2] = 3
mat[1][1] = 5
mat[2][0] = 7

Notice the pattern:

Row Index     Column Index

    0               2
    1               1
    2               0

As the row index increases, the column index decreases.

Since the last valid column index is n - 1, we calculate the secondary diagonal column using:

n - 1 - i

Therefore, the secondary diagonal element is:

mat[i][n - 1 - i]

For n = 3:

i = 0:

n - 1 - i = 3 - 1 - 0 = 2

mat[0][2] = 3


i = 1:

n - 1 - i = 3 - 1 - 1 = 1

mat[1][1] = 5


i = 2:

n - 1 - i = 3 - 1 - 2 = 0

mat[2][0] = 7

This formula works for every square matrix.

Avoid Counting the Center Element Twice:

if i != n - 1 - i:
    total += mat[i][n - 1 - i]

In an odd-sized square matrix, the primary and secondary diagonals intersect at the center.

The center element belongs to both diagonals.

However, the problem requires us to count it only once.

Consider:

1  2  3
4  5  6
7  8  9

The center element is:

mat[1][1] = 5

During the primary diagonal calculation:

total += mat[1][1]

we already add 5.

If we also execute:

total += mat[1][3 - 1 - 1]

we would add:

mat[1][1]

again.

This would count the same element twice.

Therefore, we check:

if i != n - 1 - i:

For the center element:

i = 1
n = 3

1 != 3 - 1 - 1

1 != 1

False

Since the condition is False, the secondary diagonal element is skipped.

This ensures that the center element is counted only once.

For even-sized matrices, the two diagonals do not share a cell, so this condition never skips an element.

Return the Final Sum:

return total

After processing every row, total contains the sum of all primary and secondary diagonal elements.

Any overlapping center element has been counted only once.

The final sum is returned.

Example Walkthrough:

Consider:

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Initialization:

n = 3
total = 0

First Iteration (i = 0):

Primary diagonal:

total += mat[0][0]

total = 0 + 1 = 1

Check the secondary diagonal condition:

0 != 3 - 1 - 0

0 != 2

True

Therefore:

total += mat[0][2]

total = 1 + 3 = 4

Second Iteration (i = 1):

Primary diagonal:

total += mat[1][1]

total = 4 + 5 = 9

Check the secondary diagonal condition:

1 != 3 - 1 - 1

1 != 1

False

Since the condition is False, we do not add the secondary diagonal element.

This prevents the center element 5 from being counted twice.

total = 9

Third Iteration (i = 2):

Primary diagonal:

total += mat[2][2]

total = 9 + 9 = 18

Check the secondary diagonal condition:

2 != 3 - 1 - 2

2 != 0

True

Therefore:

total += mat[2][0]

total = 18 + 7 = 25

Return Statement:

return total

Final Result:

25

Summary of Iterations:

i

Primary Element

Secondary Element

Running Total

0

1

3

4

1

5

Skipped

9

2

9

7

25

Key Points:

A matrix is represented as a list of lists in Python.

mat[row][column] accesses an individual matrix element.

A square matrix has the same number of rows and columns.

len(mat) gives the number of rows.

The primary diagonal has equal row and column indices.

The primary diagonal element is accessed using mat[i][i].

The secondary diagonal moves from the top-right corner to the bottom-left corner.

The secondary diagonal element is accessed using mat[i][n - 1 - i].

The condition i != n - 1 - i prevents counting the center element twice.

The diagonals overlap only when the matrix has an odd number of rows.

We only need one loop because each row contains at most two distinct diagonal elements.

There is no need to traverse the entire matrix using nested loops.

Complexity Analysis:

Time Complexity: O(n)

The matrix contains n rows and n columns.

The loop executes exactly n times.

During each iteration, we access at most two elements.

Accessing an element using mat[i][j] takes O(1) time.

Therefore, the total time complexity is O(n).

Space Complexity: O(1)

We only use three variables: n, total, and i.

We do not create any additional lists, dictionaries, or matrices.

Therefore, the auxiliary space complexity is O(1).

Final Result:

For:

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

The function returns:

25

Important Matrix Patterns to Remember:

Primary Diagonal:

mat[i][i]

Secondary Diagonal:

mat[i][n - 1 - i]

Avoid Double Counting:

if i != n - 1 - i:

This solution is efficient because it directly accesses the required diagonal elements without traversing every cell of 
the matrix.
The most important concept from this problem is understanding how row and column indices change along the two diagonals.
Once these indexing patterns become familiar, many other matrix problems involving diagonal traversal, diagonal sums, 
and matrix transformations become easier to solve.
'''