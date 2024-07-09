'''
Problem statement:
The task is to complete the insert() function which is used to implement Insertion Sort.
You don't have to read input or print anything. Your task is to complete the function 
insert() and insertionSort() where insert() takes the array, it's size and an index i and 
insertionSort() uses insert function to sort the array in ascending order using insertion 
sort algorithm. 

Example:
Input:
N = 5
arr[] = { 4, 1, 3, 9, 7}

Output:
1 3 4 7 9

'''

class Solution:
    def insert(self, alist, index, n):

        key = alist[index]
        j = index - 1

        while j >= 0 and alist[j] > key:
            alist[j + 1] = alist[j]
            j -= 1
        
        alist[j + 1] = key
        
    def insertionSort(self, alist, n):
        
        for i in range(1, n):
            self.insert(alist, i, n)

#{ 
 # Driver Code Starts

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()


'''
How Insertion Sort Works:

1. Start with the second element (index 1) of the array.
2. Compare this element with the elements before it and insert it into its correct 
position in the sorted part of the array.
3. Repeat the process for the next element, considering the sorted part to include all 
the previous elements.
4. Continue until the entire array is sorted.

Insertion Sort Algorithm

1. Start with the second element.
2. Compare it with the elements before it.
3. Shift the elements one position to the right to make space for the new element.
4. Insert the element into its correct position.
5. Repeat the process for all elements.


Detailed Explanation:

1. Initialization:
   
   ```python
   for i in range(1, len(arr)):
   ```

   - The outer loop iterates over the array starting from the second element (`i = 1`) 
   to the last element (`i = len(arr) - 1`).

2. Key Element:
   
   ```python
   key = arr[i]
   j = i - 1
   ```
   
   - The `key` is the element to be inserted into the sorted part of the array.
   - `j` is the index of the last element in the sorted part of the array.

3. Shift Elements:
   
   ```python
   while j >= 0 and key < arr[j]:
       arr[j + 1] = arr[j]
       j -= 1
   
   ```
   - This `while` loop shifts elements of the sorted part of the array to the right 
   until the correct position for `key` is found.
   - The loop continues as long as `j` is non-negative and `arr[j]` is greater than `key`.

4. Insert Key:
   
   ```python
   arr[j + 1] = key
   
   ```
   - After finding the correct position, `key` is inserted at `arr[j + 1]`.

Example Walkthrough:

For the given list `arr = [13, 24, 46, 20, 9, 52, 28]`:

- Initial Array: `[13, 24, 46, 20, 9, 52, 28]`

- First Iteration (`i = 1`):
  - `key = 24`
  - Compare with `13`, no shift needed.
  - Insert `24` at position 1.
  - Array remains `[13, 24, 46, 20, 9, 52, 28]`.

- Second Iteration (`i = 2`):
  - `key = 46`
  - Compare with `24`, no shift needed.
  - Insert `46` at position 2.
  - Array remains `[13, 24, 46, 20, 9, 52, 28]`.

- Third Iteration (`i = 3`):
  - `key = 20`
  - Compare with `46`, shift `46` to the right.
  - Compare with `24`, shift `24` to the right.
  - Compare with `13`, no shift needed.
  - Insert `20` at position 1.
  - Array becomes `[13, 20, 24, 46, 9, 52, 28]`.

- Fourth Iteration (`i = 4`):
  - `key = 9`
  - Compare with `46`, shift `46` to the right.
  - Compare with `24`, shift `24` to the right.
  - Compare with `20`, shift `20` to the right.
  - Compare with `13`, shift `13` to the right.
  - Insert `9` at position 0.
  - Array becomes `[9, 13, 20, 24, 46, 52, 28]`.

- Fifth Iteration (`i = 5`):
  - `key = 52`
  - Compare with `46`, no shift needed.
  - Insert `52` at position 5.
  - Array remains `[9, 13, 20, 24, 46, 52, 28]`.

- Sixth Iteration (`i = 6`):
  - `key = 28`
  - Compare with `52`, shift `52` to the right.
  - Compare with `46`, shift `46` to the right.
  - Compare with `24`, no shift needed.
  - Insert `28` at position 4.
  - Array becomes `[9, 13, 20, 24, 28, 46, 52]`.

### Final Sorted Array:
- `[9, 13, 20, 24, 28, 46, 52]`

'''