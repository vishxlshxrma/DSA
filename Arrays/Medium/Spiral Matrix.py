'''
Problem Statement:
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

'''

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        row = len(matrix)
        col = len(matrix[0])

        left = 0
        right = col - 1
        top = 0
        bottom = row - 1

        res = []

        while ( top <= bottom and left <= right):

            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            for j in range(top, bottom + 1):
                res.append(matrix[j][right])
            right -= 1

            if (top <= bottom):
                for k in range(right, left - 1, -1):
                    res.append(matrix[bottom][k])
                bottom -= 1

            if (left <= right):
                for l in range(bottom, top - 1, -1):
                    
                    res.append(matrix[l][left])
                left += 1
        
        return res


'''
Code Explanation:

The goal is to traverse a matrix in spiral order without visiting any element more than once.

Unlike normal row-wise or column-wise traversal, spiral traversal changes direction repeatedly.

Therefore, instead of using simple nested loops over every row and column, we maintain four boundaries that represent 
the portion of the matrix that has not yet been processed.

These boundaries are:

top: The first unprocessed row.

bottom: The last unprocessed row.

left: The first unprocessed column.

right: The last unprocessed column.

During each iteration, we traverse the outer boundary of the remaining matrix and then move the boundaries inward.

Let's understand the solution step by step.

Step-by-Step Explanation:

Find the Matrix Dimensions:

row = len(matrix)
col = len(matrix[0])

len(matrix) returns the number of rows.

len(matrix[0]) returns the number of columns in the first row.

The problem guarantees a non-empty rectangular matrix.

For example:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Here:

row = 3
col = 3

These dimensions are used to initialize the traversal boundaries.

Initialize the Four Boundaries:

left = 0
right = col - 1
top = 0
bottom = row - 1

left = 0: The first column of the matrix.

right = col - 1: The last column of the matrix.

top = 0: The first row of the matrix.

bottom = row - 1: The last row of the matrix.

For a 3 x 3 matrix:

left = 0
right = 2
top = 0
bottom = 2

Initially, these boundaries surround the entire matrix.

Conceptually:

        left       right
          ↓          ↓
       1   2   3   ← top
       4   5   6
       7   8   9   ← bottom

As elements are processed, the boundaries move inward.

Initialize the Result List:

res = []

res stores the matrix elements in the exact order they are visited.

Every visited element is appended to this list.

After traversal finishes, res contains all matrix elements in spiral order.

Continue While Valid Boundaries Exist:

while top <= bottom and left <= right:

This condition ensures that there are still unprocessed rows and columns.

top <= bottom means at least one unprocessed row remains.

left <= right means at least one unprocessed column remains.

If either condition becomes False, the remaining region is empty.

Therefore, the traversal stops.

The loop continues processing one layer of the matrix at a time.

First Direction — Left to Right:

for i in range(left, right + 1):
    res.append(matrix[top][i])

top += 1

We traverse the current top row from the left boundary to the right boundary.

The row index remains fixed at top.

The column index i increases.

For example:

1 → 2 → 3
4   5   6
7   8   9

The accessed elements are:

matrix[0][0] = 1
matrix[0][1] = 2
matrix[0][2] = 3

The result becomes:

res = [1, 2, 3]

Why right + 1?

Python's range() excludes the stopping value.

Therefore:

range(left, right + 1)

ensures that the element at the right boundary is included.

After processing the entire top row:

top += 1

moves the top boundary one row downward.

The processed top row will not be visited again.

Second Direction — Top to Bottom:

for j in range(top, bottom + 1):
    res.append(matrix[j][right])

right -= 1

We traverse the current rightmost column from top to bottom.

The column index remains fixed at right.

The row index j increases.

After processing the top row, the traversal continues downward:

1 → 2 → 3
        ↓
4   5   6
        ↓
7   8   9

The new elements are:

matrix[1][2] = 6
matrix[2][2] = 9

The result becomes:

res = [1, 2, 3, 6, 9]

After processing the rightmost column:

right -= 1

moves the right boundary one column to the left.

The processed rightmost column will not be visited again.

Third Direction — Right to Left:

if top <= bottom:
    for k in range(right, left - 1, -1):
        res.append(matrix[bottom][k])

    bottom -= 1

We traverse the current bottom row from right to left.

The row index remains fixed at bottom.

The column index k decreases.

For example:

1   2   3
4   5   6
7 ← 8 ← 9

Since the rightmost column has already been processed, we begin from the updated right boundary.

The new elements are:

matrix[2][1] = 8
matrix[2][0] = 7

The result becomes:

res = [1, 2, 3, 6, 9, 8, 7]

Understanding the range:

range(right, left - 1, -1)

The general syntax is:

range(start, stop, step)

Here:

start = right: Begin at the right boundary.

stop = left - 1: Stop just before the left boundary.

step = -1: Move backwards by one column.

For example:

range(2, -1, -1)

generates:

2, 1, 0

The condition:

if top <= bottom:

is necessary because the top-to-bottom traversal may have already processed the final remaining row.

Without this check, the bottom-row traversal could visit elements twice.

After completing the bottom row:

bottom -= 1

moves the bottom boundary one row upward.

Fourth Direction — Bottom to Top:

if left <= right:
    for l in range(bottom, top - 1, -1):
        res.append(matrix[l][left])

    left += 1

We traverse the current leftmost column from bottom to top.

The column index remains fixed at left.

The row index l decreases.

For example:

1   2   3
↑       ↓
4   5   6
↑       ↓
7 ← 8 ← 9

Since the bottom row has already been processed, we start from the updated bottom boundary.

For the 3 x 3 example, the new element is:

matrix[1][0] = 4

The result becomes:

res = [1, 2, 3, 6, 9, 8, 7, 4]

Understanding the range:

range(bottom, top - 1, -1)

Start at the bottom boundary.

Move upward using step -1.

Include the current top boundary.

The condition:

if left <= right:

ensures that an unprocessed column still exists.

Without this condition, the left-column traversal could revisit elements when only one column remained.

After processing the leftmost column:

left += 1

moves the left boundary one column to the right.

Notice that we use left += 1, not left -= 1, because the unprocessed region is shrinking inward.

Repeat the Process for the Inner Matrix:

After completing all four directions, the outer layer has been processed.

The updated boundaries now surround the remaining inner region.

For the 3 x 3 example:

top = 1
bottom = 1
left = 1
right = 1

Only the center element remains:

5

The while condition is still True:

top <= bottom → 1 <= 1 → True
left <= right → 1 <= 1 → True

Therefore, another iteration begins.

The left-to-right traversal adds:

matrix[1][1]

which is:

5

The result becomes:

res = [1, 2, 3, 6, 9, 8, 7, 4, 5]

The boundaries are then updated.

Since no unprocessed rows or columns remain, the loop terminates.

Return the Result:

return res

After the while loop finishes, every matrix element has been visited exactly once.

The elements have been collected in spiral order.

The completed result list is returned.

Example Walkthrough:

Consider:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Initialization:

row = 3
col = 3

left = 0
right = 2
top = 0
bottom = 2

res = []

First Direction — Left to Right:

matrix[0][0] = 1
matrix[0][1] = 2
matrix[0][2] = 3

Result:

[1, 2, 3]

Update:

top = 1

Second Direction — Top to Bottom:

matrix[1][2] = 6
matrix[2][2] = 9

Result:

[1, 2, 3, 6, 9]

Update:

right = 1

Third Direction — Right to Left:

matrix[2][1] = 8
matrix[2][0] = 7

Result:

[1, 2, 3, 6, 9, 8, 7]

Update:

bottom = 1

Fourth Direction — Bottom to Top:

matrix[1][0] = 4

Result:

[1, 2, 3, 6, 9, 8, 7, 4]

Update:

left = 1

Second While-Loop Iteration:

Remaining boundaries:

top = 1
bottom = 1
left = 1
right = 1

Only one element remains:

matrix[1][1] = 5

Add it to the result:

[1, 2, 3, 6, 9, 8, 7, 4, 5]

After updating the boundaries, the while condition becomes False.

Return Statement:

return res

Final Result:

[1, 2, 3, 6, 9, 8, 7, 4, 5]

Summary of Traversal:

Step

Direction

Elements Added

Result

1

Left to Right

1, 2, 3

[1, 2, 3]

2

Top to Bottom

6, 9

[1, 2, 3, 6, 9]

3

Right to Left

8, 7

[1, 2, 3, 6, 9, 8, 7]

4

Bottom to Top

4

[1, 2, 3, 6, 9, 8, 7, 4]

5

Inner Layer

5

[1, 2, 3, 6, 9, 8, 7, 4, 5]

Understanding the Four Boundary Updates:

Direction

Fixed Index

Changing Index

Boundary Update

Left to Right

top row

Column increases

top += 1

Top to Bottom

right column

Row increases

right -= 1

Right to Left

bottom row

Column decreases

bottom -= 1

Bottom to Top

left column

Row decreases

left += 1

Why Boundary Checks Are Important:

Consider a matrix containing only one row:

1  2  3  4

After the left-to-right traversal, all four elements have already been visited.

The top boundary is increased:

top = 1
bottom = 0

Therefore:

top > bottom

If we attempted to traverse the bottom row again, we would add duplicate elements.

The condition:

if top <= bottom:

prevents this.

Similarly, if only one column remains, the condition:

if left <= right:

prevents the left-column traversal from visiting already processed elements.

These checks ensure that the algorithm works correctly for:

Square matrices.

Rectangular matrices.

Matrices containing only one row.

Matrices containing only one column.

Matrices with odd or even dimensions.

Common Mistakes:

Forgetting that range() excludes the stop value.

Incorrect:

range(left, right)

Correct:

range(left, right + 1)

Forgetting the negative step during reverse traversal.

Incorrect:

range(right, left)

Correct:

range(right, left - 1, -1)

Reversing row and column indices.

Incorrect:

matrix[k][bottom]

Correct:

matrix[bottom][k]

Remember:

matrix[row][column]

Updating the left boundary in the wrong direction.

Incorrect:

left -= 1

Correct:

left += 1

The left boundary must move inward after its column is processed.

Forgetting boundary checks.

Without checking top <= bottom and left <= right before the final two directions, elements may be visited more than once.

Key Points:

Spiral traversal processes the matrix one outer layer at a time.

Four boundaries are maintained: top, bottom, left, and right.

The traversal follows four directions in a clockwise order.

After each direction, the corresponding boundary moves inward.

Horizontal movement changes the column index while keeping the row fixed.

Vertical movement changes the row index while keeping the column fixed.

matrix[row][col] must always be used in the correct order.

Reverse traversal requires a negative step in range().

Boundary checks prevent duplicate traversal.

The algorithm works for both square and rectangular matrices.

Every matrix element is visited exactly once.

Complexity Analysis:

Let:

m = number of rows
n = number of columns

Time Complexity: O(m x n)

The matrix contains m x n elements.

Every element is visited exactly once.

Each element is appended to the result list in O(1) amortized time.

Although multiple loops are used, they collectively process each element only once.

Therefore:

Time Complexity = O(m x n)

Space Complexity:

The four boundary variables require O(1) space.

The loop variables require O(1) space.

The result list stores all m x n matrix elements.

Therefore:

Auxiliary Space Complexity = O(1), excluding the output.

Total Space Complexity = O(m x n), including the output list.

Important Matrix Patterns to Remember:

Matrix Element Access:

matrix[row][col]

Left to Right:

for i in range(left, right + 1):
    res.append(matrix[top][i])

Top to Bottom:

for j in range(top, bottom + 1):
    res.append(matrix[j][right])

Right to Left:

for k in range(right, left - 1, -1):
    res.append(matrix[bottom][k])

Bottom to Top:

for l in range(bottom, top - 1, -1):
    res.append(matrix[l][left])

Boundary Updates:

top += 1
right -= 1
bottom -= 1
left += 1

Main Loop Condition:

while top <= bottom and left <= right:

The Most Important Pattern:

Spiral Matrix
↓
Initialize four boundaries
↓
Traverse top row → Move top downward
↓
Traverse right column → Move right leftward
↓
Traverse bottom row → Move bottom upward
↓
Traverse left column → Move left rightward
↓
Repeat for the inner layer
↓
Stop when boundaries cross
↓
Return the spiral traversal

This solution is efficient because it traverses every matrix element exactly once without requiring a visited array or 
any additional matrix.
The most important concept from this problem is understanding how four boundaries can be used to control traversal 
direction and prevent revisiting previously processed elements.
This boundary-based traversal pattern is useful in many matrix problems involving spiral traversal, matrix rotation, 
layer processing, and two-dimensional simulations.
'''