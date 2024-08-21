'''
Problem Statement:
The task is to complete the `insert()` function, which is used to implement Insertion 
Sort. You don't have to read input or print anything. Your task is to complete the 
function `insert()` and `insertionSort()` where `insert()` takes the array, its size, 
and an index `i`, and `insertionSort()` uses the `insert` function to sort the array 
in ascending order using the insertion sort algorithm.

Example:
Input:

N = 5
arr[] = { 4, 1, 3, 9, 7 }

Output:

1 3 4 7 9

How Insertion Sort Works:
1. Start with the first element (index 0) of the array.
2. Compare this element with the elements before it (if any) and insert it into its 
correct position in the sorted part of the array.
3. Repeat the process for the next element, considering the sorted part to include all 
the previous elements.
4. Continue until the entire array is sorted.

Insertion Sort Algorithm:
1. Start with the first element.
2. Compare it with the elements before it.
3. Shift the elements one position to the right to make space for the new element if 
needed.
4. Insert the element into its correct position.
5. Repeat the process for all elements.

'''
arr = [13, 24, 46, 20, 9, 52, 28]
n = len(arr)

for i in range(n):
    j = i
    while (j>0 and arr[j-1]> arr[j]):
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1

print(arr)

'''
Detailed Explanation:

1. Initialization:
   
   ```python
   for i in range(n):
   ```

   - The outer loop iterates over the array starting from the first element (`i = 0`) 
   to the last element (`i = n - 1`).

2. Key Element:
   
   ```python
   j = i
   ```
   
   - The `j` variable is used to traverse and compare the current element with the 
   sorted part of the array.

3. Shift Elements:
   
   ```python
   while j > 0 and arr[j - 1] > arr[j]:
       arr[j], arr[j - 1] = arr[j - 1], arr[j]
       j -= 1
   ```

   - This `while` loop compares the current element `arr[j]` with the elements before 
   it in the sorted part of the array.
   - If the previous element `arr[j - 1]` is greater than the current element `arr[j]`, 
   they are swapped.
   - The loop continues until `j` becomes `0` or until the correct position for the 
   current element is found.

4. Insert Key:
   
   ```python
   arr[j], arr[j - 1] = arr[j - 1], arr[j]
   ```

   - The swapping mechanism within the loop effectively inserts the element into its 
   correct position in the sorted part of the array.

Example Walkthrough:

For the given list `arr = [13, 24, 46, 20, 9, 52, 28]`:

- Initial Array: `[13, 24, 46, 20, 9, 52, 28]`

- First Iteration (`i = 0`):
  - `j = 0`
  - No comparison is needed since this is the first element.
  - Array remains `[13, 24, 46, 20, 9, 52, 28]`.

- Second Iteration (`i = 1`):
  - `j = 1`
  - Compare with `13`, no swap needed.
  - Array remains `[13, 24, 46, 20, 9, 52, 28]`.

- Third Iteration (`i = 2`):
  - `j = 2`
  - Compare with `24`, no swap needed.
  - Array remains `[13, 24, 46, 20, 9, 52, 28]`.

- Fourth Iteration (`i = 3`):
  - `j = 3`
  - Compare with `46`, swap `46` and `20`.
  - Compare with `24`, swap `24` and `20`.
  - Compare with `13`, no swap needed.
  - Array becomes `[13, 20, 24, 46, 9, 52, 28]`.

- Fifth Iteration (`i = 4`):
  - `j = 4`
  - Compare with `46`, swap `46` and `9`.
  - Compare with `24`, swap `24` and `9`.
  - Compare with `20`, swap `20` and `9`.
  - Compare with `13`, swap `13` and `9`.
  - Array becomes `[9, 13, 20, 24, 46, 52, 28]`.

- Sixth Iteration (`i = 5`):
  - `j = 5`
  - Compare with `46`, no swap needed.
  - Array remains `[9, 13, 20, 24, 46, 52, 28]`.

- Seventh Iteration (`i = 6`):
  - `j = 6`
  - Compare with `52`, swap `52` and `28`.
  - Compare with `46`, swap `46` and `28`.
  - Compare with `24`, no swap needed.
  - Array becomes `[9, 13, 20, 24, 28, 46, 52]`.

Final Sorted Array:
- `[9, 13, 20, 24, 28, 46, 52]`

'''