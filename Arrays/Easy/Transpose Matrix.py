'''
Problem Statement:
Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 
'''
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        res = []

        for col in range(cols):
            new_row = []

            for row in range(rows):
                new_row.append(matrix[row][col])
                pass
            
            res.append(new_row)

        return res

'''
Code Explanation:
The goal is to create a new matrix in which the rows of the original matrix become columns and the columns become rows.
We use nested loops to traverse the original matrix column by column.
For every column in the original matrix, we create a new list containing all elements of that column.
This new list becomes a row in the transposed matrix.

The important idea is:

Original Matrix:
matrix[row][col]

Transposed Matrix:
result[col][row] = matrix[row][col]

Instead of directly assigning elements into a preallocated result matrix, our implementation uses append() to build each 
transposed row.

Let's understand the solution step by step.

Step-by-Step Explanation:

Find the Number of Rows:

rows = len(matrix)

len(matrix) returns the number of inner lists in the matrix.

Each inner list represents one row.

Therefore, rows stores the total number of rows in the original matrix.

For example:

matrix = [
    [10, 20, 30],
    [40, 50, 60]
]

Here:

rows = 2

because the matrix contains two inner lists.

Find the Number of Columns:

cols = len(matrix[0])

matrix[0] represents the first row of the matrix.

len(matrix[0]) returns the number of elements in that row.

Since the problem guarantees a non-empty rectangular matrix, every row contains the same number of columns.

Therefore:

cols = 3

for:

matrix = [
    [10, 20, 30],
    [40, 50, 60]
]

Important:

len(matrix)     = number of rows
len(matrix[0])  = number of columns

These values may be different because matrices do not always have to be square.

Initialize the Result Matrix:

res = []

We create an empty list named res.

This list will eventually contain all the rows of the transposed matrix.

Each row of the result will itself be a list.

Initially:

res = []

Traverse the Original Matrix Column by Column:

for col in range(cols):

The outer loop iterates through every column of the original matrix.

The variable col represents the current column index.

We process columns first because each original column will become a new row in the transposed matrix.

For a matrix with 3 columns:

col = 0
col = 1
col = 2

During each iteration, we collect all the elements belonging to that column.

Create a New Row:

new_row = []

At the beginning of each outer-loop iteration, we create a new empty list.

This list will store the elements of the current column.

Once all elements of that column have been collected, new_row will become one row of the transposed matrix.

For example, if the original matrix is:

10  20  30
40  50  60
70  80  90

During the first outer-loop iteration:

col = 0

we want:

new_row = [10, 40, 70]

During the second iteration:

col = 1

we want:

new_row = [20, 50, 80]

Traverse Every Row Within the Current Column:

for row in range(rows):

The inner loop iterates through every row of the original matrix.

The outer loop keeps the column index fixed.

The inner loop changes the row index.

This allows us to move vertically through the matrix.

For example:

col = 0

The inner loop accesses:

matrix[0][0] = 10
matrix[1][0] = 40
matrix[2][0] = 70

Notice that the column index remains 0, while the row index changes.

This is column-wise traversal.

Append the Current Element to the New Row:

new_row.append(matrix[row][col])

matrix[row][col] accesses the element at the current row and column.

append() adds that element to the end of new_row.

For example:

col = 0

First iteration:

row = 0

matrix[0][0] = 10

new_row = [10]

Second iteration:

row = 1

matrix[1][0] = 40

new_row = [10, 40]

Third iteration:

row = 2

matrix[2][0] = 70

new_row = [10, 40, 70]

After the inner loop finishes, new_row contains the entire first column of the original matrix.

Note:

pass

is present in the submitted code, but it performs no operation.

It is a placeholder statement in Python and can be removed without changing the algorithm or its output.

Append the Completed Row to the Result:

res.append(new_row)

Once the inner loop finishes, new_row contains all the elements from one original column.

We append this completed list to res.

This creates one row of the transposed matrix.

For example:

After processing column 0:

res = [
    [10, 40, 70]
]

After processing column 1:

res = [
    [10, 40, 70],
    [20, 50, 80]
]

After processing column 2:

res = [
    [10, 40, 70],
    [20, 50, 80],
    [30, 60, 90]
]

The transpose is now complete.

Return the Transposed Matrix:

return res

After every original column has been processed, res contains the complete transposed matrix.

We return res as the final answer.

The original matrix remains unchanged.

Example Walkthrough:

Consider:

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

Initialization:

rows = 3
cols = 3
res = []

First Outer Loop Iteration (col = 0):

Create:

new_row = []

Inner Loop:

row = 0:

matrix[0][0] = 10

new_row = [10]

row = 1:

matrix[1][0] = 40

new_row = [10, 40]

row = 2:

matrix[2][0] = 70

new_row = [10, 40, 70]

Append the completed row:

res.append(new_row)

Result:

res = [[10, 40, 70]]

Second Outer Loop Iteration (col = 1):

Create:

new_row = []

Inner Loop:

row = 0:

matrix[0][1] = 20

new_row = [20]

row = 1:

matrix[1][1] = 50

new_row = [20, 50]

row = 2:

matrix[2][1] = 80

new_row = [20, 50, 80]

Append the completed row:

res = [
    [10, 40, 70],
    [20, 50, 80]
]

Third Outer Loop Iteration (col = 2):

Create:

new_row = []

Inner Loop:

row = 0:

matrix[0][2] = 30

new_row = [30]

row = 1:

matrix[1][2] = 60

new_row = [30, 60]

row = 2:

matrix[2][2] = 90

new_row = [30, 60, 90]

Append the completed row:

res = [
    [10, 40, 70],
    [20, 50, 80],
    [30, 60, 90]
]

Return Statement:

return res

Final Result:

[[10, 40, 70],
 [20, 50, 80],
 [30, 60, 90]]

Summary of Iterations:

Column

Elements Accessed

New Row Created

0

10, 40, 70

[10, 40, 70]

1

20, 50, 80

[20, 50, 80]

2

30, 60, 90

[30, 60, 90]

Understanding the Difference Between Traversal and Transpose:

A very important distinction is that column-wise traversal and matrix transpose are related, but they are not exactly 
the same operation.

Column-wise traversal:

for col in range(cols):
    for row in range(rows):
        print(matrix[row][col])

This simply visits the elements in column-wise order.

However, it does not create a new matrix.

Matrix transpose:

for col in range(cols):
    new_row = []

    for row in range(rows):
        new_row.append(matrix[row][col])

    res.append(new_row)

This creates a new two-dimensional matrix.

The difference is that each original column becomes a separate inner list in the result.

Key Points:

A matrix is represented as a list of lists in Python.

len(matrix) gives the number of rows.

len(matrix[0]) gives the number of columns for a non-empty rectangular matrix.

Matrix elements are accessed using matrix[row][col].

Transposing a matrix converts rows into columns and columns into rows.

An element at position (row, col) moves to position (col, row).

The original dimensions R x C become C x R.

The outer loop iterates over the original columns.

The inner loop iterates over the original rows.

new_row stores all elements from one original column.

res.append(new_row) adds the completed row to the transposed matrix.

new_row = [] must be inside the outer loop so a fresh row is created for every column.

res.append(new_row) must be outside the inner loop so the row is appended only after it is complete.

The pass statement in the original solution is unnecessary.

The original matrix is not modified.

The algorithm works for both square and rectangular matrices.

Complexity Analysis:

Let:

R = number of rows
C = number of columns

Time Complexity: O(R x C)

The outer loop executes C times.

The inner loop executes R times for each outer-loop iteration.

Therefore, the total number of iterations is R x C.

Every element is visited exactly once.

Each append() operation takes O(1) amortized time.

Therefore:

Time Complexity = O(R x C)

Space Complexity: O(R x C)

The result matrix contains the same number of elements as the original matrix.

We create C inner lists, each containing R elements.

Therefore, the result contains R x C elements.

The temporary new_row contains at most R elements.

No other significant data structures are created.

Therefore:

Space Complexity = O(R x C)

This is the space required for the output matrix. Excluding the output, the algorithm uses O(R) temporary space for the 
current row being constructed.

Final Result:

For:

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

The function returns:

[[10, 40, 70],
 [20, 50, 80],
 [30, 60, 90]]

Important Matrix Patterns to Remember:

Access an Element:

matrix[row][col]

Row-Wise Traversal:

for row in range(rows):
    for col in range(cols):
        print(matrix[row][col])

Column-Wise Traversal:

for col in range(cols):
    for row in range(rows):
        print(matrix[row][col])

Matrix Transpose:

for col in range(cols):
    new_row = []

    for row in range(rows):
        new_row.append(matrix[row][col])

    res.append(new_row)

Core Transpose Relationship:

result[col][row] = matrix[row][col]

The most important concept from this problem is understanding that the outer loop determines which row of the transposed 
matrix we are constructing, while the inner loop collects the corresponding elements from the original matrix.

This solution is efficient because it visits each element exactly once and directly builds the transposed matrix without 
performing unnecessary operations.
'''