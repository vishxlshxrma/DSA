'''
Problem Statement:
You are part of a university admissions office and need to keep track of the kth highest test score from applicants in 
real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit 
their scores.
You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously 
returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth 
highest score in the sorted list of all scores.

Implement the KthLargest class:
KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in 
the pool of test scores so far.
 

Example 1:
Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output: [null, 4, 5, 5, 8, 8]
Explanation:
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3); // return 4
kthLargest.add(5); // return 5
kthLargest.add(10); // return 5
kthLargest.add(9); // return 8
kthLargest.add(4); // return 8

Example 2:
Input:
["KthLargest", "add", "add", "add", "add"]
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]
Output: [null, 7, 7, 7, 8]
Explanation:
KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
kthLargest.add(2); // return 7
kthLargest.add(10); // return 7
kthLargest.add(9); // return 7
kthLargest.add(9); // return 8
'''

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for i in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, i)
            else:
                heapq.heappush(self.heap, i)
                heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

'''
The Kth Largest Element in a Stream problem asks us to continuously keep track of the kth largest element as new numbers 
are added to a stream. The key idea is to maintain a min-heap containing only the k largest elements seen so far. Since 
a min-heap keeps the smallest element at the root, the root of the heap represents the kth largest element among all 
elements seen so far.

Code Explanation:
The provided code uses Python's `heapq` module to maintain a min-heap of size at most `k`. Let's break it down 
step-by-step:

```python
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for i in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, i)
            else:
                heapq.heappush(self.heap, i)
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
```

Step-by-Step Explanation:

1. Initialization:

   * `self.k = k`: Stores the value of `k` so that it can be accessed by other methods, especially `add()`.
   * `self.heap = []`: Creates an empty list that will be used as a min-heap.
   * The use of `self` is important because the object must remember the value of `k` and the heap between multiple 
    calls to `add()`.

2. Building the Initial Heap:

   * The loop:

     ```python
     for i in nums:
     ```

     processes each value in the initial list `nums`.

   * If the heap contains fewer than `k` elements:

     ```python
     if len(self.heap) < k:
         heapq.heappush(self.heap, i)
     ```

     we simply add the current element to the heap.

   * If the heap already contains `k` elements:

     ```python
     else:
         heapq.heappush(self.heap, i)
         heapq.heappop(self.heap)
     ```

     we first add the new element and then remove the smallest element.

   * Because `heapq` implements a min-heap, `heapq.heappop()` always removes the smallest element.

   * This ensures that the heap never keeps more than `k` elements and that the heap contains the `k` largest values 
    seen so far.

3. Why We Use a Min-Heap:

   * It may initially seem that we should use a max-heap because the problem asks for the kth largest element.

   * However, a min-heap of size `k` is actually the better choice.

   * Suppose `k = 3` and the three largest values seen so far are:

     ```text
     5, 8, 10
     ```

   * The min-heap contains these three values, and its root is:

     ```text
     5
     ```

   * `5` is the smallest among the three largest values, so it is exactly the 3rd largest element overall.

   * Therefore, we maintain the following invariant:

     ```text
     self.heap = the k largest elements seen so far
     self.heap[0] = the kth largest element
     ```

4. The `add()` Method:

   * The `add()` method is called whenever a new value is added to the stream.

   * First, the new value is inserted into the min-heap:

     ```python
     heapq.heappush(self.heap, val)
     ```

   * If the heap now contains more than `k` elements:

     ```python
     if len(self.heap) > self.k:
         heapq.heappop(self.heap)
     ```

     the smallest element is removed.

   * This keeps only the `k` largest elements in the heap.

   * Because the heap is a min-heap, its smallest element is at index `0`. That element is therefore the kth largest 
    value overall.

5. Returning the Kth Largest Element:

   * The line:

     ```python
     return self.heap[0]
     ```

     returns the smallest element in the min-heap.

   * Since the heap contains the `k` largest elements, the smallest element among them is the kth largest element.

Walkthrough with Example:

Consider:

```python
k = 3
nums = [4, 5, 8, 2]
```

1. Initialization:

   * `self.k = 3`
   * `self.heap = []`

2. Process `4`:

   * Heap size is `0`, which is less than `3`.
   * Push `4`.

   ```text
   heap = [4]
   ```

3. Process `5`:

   * Heap size is `1`, which is less than `3`.
   * Push `5`.

   ```text
   heap = [4, 5]
   ```

4. Process `8`:

   * Heap size is `2`, which is less than `3`.
   * Push `8`.

   ```text
   heap = [4, 5, 8]
   ```

   The heap now contains the three largest values seen so far.

5. Process `2`:

   * The heap already contains `3` elements.
   * Push `2`.

   Conceptually, the four values are:

   ```text
   2, 4, 5, 8
   ```

   * Since there are now more than `k = 3` elements, remove the smallest value, which is `2`.

   The heap becomes:

   ```text
   [4, 5, 8]
   ```

   Therefore:

   ```python
   self.heap[0]
   ```

   is `4`, which is the 3rd largest element.

6. First `add()`:

   ```python
   add(3)
   ```

   * Push `3`.

   ```text
   [3, 4, 5, 8]
   ```

   * The heap has more than `3` elements, so remove the smallest value, `3`.

   ```text
   [4, 5, 8]
   ```

   * Return `4`.

7. Second `add()`:

   ```python
   add(5)
   ```

   * Push `5`.

   ```text
   [4, 5, 5, 8]
   ```

   * Remove the smallest element, `4`.

   ```text
   [5, 5, 8]
   ```

   * Return `5`.

8. Third `add()`:

   ```python
   add(10)
   ```

   * Push `10`.

   ```text
   [5, 5, 8, 10]
   ```

   * Remove the smallest element, `5`.

   ```text
   [5, 8, 10]
   ```

   * Return `5`.

9. Fourth `add()`:

   ```python
   add(9)
   ```

   * Push `9`.
   * Remove the smallest element, `5`.

   ```text
   [8, 9, 10]
   ```

   * Return `8`.

10. Fifth `add()`:

    ```python
    add(4)
    ```

    * Push `4`.
    * The heap becomes larger than `k`.
    * Remove the smallest element, which is `4`.

    ```text
    [8, 9, 10]
    ```

    * Return `8`.

Final Output:

```text
4, 5, 5, 8, 8
```

Key Points:

* `heapq` implements a **min-heap** using a normal Python list.
* A min-heap keeps the smallest value at `heap[0]`.
* For the kth largest problem, we maintain a heap containing only the `k` largest elements.
* Whenever the heap becomes larger than `k`, we remove the smallest element.
* This guarantees that the heap always contains the `k` largest elements seen so far.
* The smallest element among those `k` largest elements is therefore the kth largest element.
* `self.k` and `self.heap` allow the object to maintain state between multiple calls to `add()`.
* The constructor `__init__()` initializes the heap and stores `k`; it does not return the answer.
* The `add()` method updates the existing heap whenever a new value arrives and then returns the current kth largest 
 value.

Complexity Analysis:

* Initialization Time Complexity: O(n log k), where `n` is the number of elements in the initial `nums` list. Each 
element is inserted into a heap whose size never exceeds `k`.

* `add()` Time Complexity: O(log k), because each new value is inserted into a heap of size at most `k`, and at most 
one element is removed.

* Space Complexity: O(k), because the heap stores at most `k` elements.

This solution is efficient because it does not store every value from the stream. Instead, it keeps only the `k` 
largest values that are necessary to determine the kth largest element.

The most important heap pattern to remember from this problem is:

```text
Find kth largest
        ↓
Use a min-heap
        ↓
Keep only k elements
        ↓
If size > k, remove the smallest
        ↓
heap[0] = kth largest
```

'''