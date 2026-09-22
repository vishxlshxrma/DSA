'''
Problem Statement:
Given a data stream arr[] where integers are read sequentially, find the median of the elements encountered so far after 
each new integer is read.

The median is defined as follows:

Odd number of elements: The median is the middle element when the current set of numbers is sorted.
Even number of elements: The median is the arithmetic mean (average) of the two middle elements when the current set of 
numbers is sorted.

Example 1:
Input: arr[] = [5, 15, 1, 3, 2, 8]
Output: [5.0, 10.0, 5.0, 4.0, 3.0, 4.0] 
Explanation: 
After reading 1st element of stream - 5 -> median = 5.0
After reading 2nd element of stream - 5, 15 -> median = (5+15)/2 = 10.0 
After reading 3rd element of stream - 5, 15, 1 -> median = 5.0
After reading 4th element of stream - 5, 15, 1, 3 ->  median = (3+5)/2 = 4.0
After reading 5th element of stream - 5, 15, 1, 3, 2 -> median = 3.0
After reading 6th element of stream - 5, 15, 1, 3, 2, 8 ->  median = (3+5)/2 = 4.0

Example 2:
Input: arr[] = [2, 2, 2, 2]
Output: [2.0, 2.0, 2.0, 2.0]
Explanation: 
After reading 1st element of stream - 2 -> median = 2.0
After reading 2nd element of stream - 2, 2 -> median = (2+2)/2 = 2.0
After reading 3rd element of stream - 2, 2, 2 -> median = 2.0
After reading 4th element of stream - 2, 2, 2, 2 ->  median = (2+2)/2 = 2.0
'''

import heapq

class Solution:
    def getMedian(self, arr):
        maxHeap = []
        minHeap = []
        result = []
        
        for num in arr:
            if not maxHeap or num <= -maxHeap[0]:
                heapq.heappush(maxHeap, -num)
            else:
                heapq.heappush(minHeap, num)
                
            if len(maxHeap) > len(minHeap) + 1:
                x = -heapq.heappop(maxHeap)
                heapq.heappush(minHeap, x)
                
            if len(minHeap) > len(maxHeap) + 1:
                x = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -x)
                
            if len(maxHeap) == len(minHeap):
                median = (-maxHeap[0] + minHeap[0])/2
            elif len(maxHeap) > len(minHeap):
                median = -maxHeap[0]
            else:
                median = minHeap[0]
                
            result.append(median)
            
        return result


'''
Problem Statement:

The Find Median from Data Stream problem asks us to find the median after each number is processed from
the input array. The median is the middle value when all numbers seen so far are arranged in sorted order.

To efficiently find the median without sorting the entire collection after every new number, we maintain
two heaps:

1. A max-heap containing the smaller half of the numbers.
2. A min-heap containing the larger half of the numbers.

The two heaps are kept balanced so that their sizes differ by at most 1. The top elements of the two heaps
are therefore the values closest to the middle, allowing the median to be calculated efficiently.

Code Explanation:

The provided code uses Python's `heapq` module. Since `heapq` provides a min-heap, negative values are used
to simulate a max-heap for the smaller half.

```python
import heapq

class Solution:
    def getMedian(self, arr):
        maxHeap = []
        minHeap = []
        result = []
        
        for num in arr:
            if not maxHeap or num <= -maxHeap[0]:
                heapq.heappush(maxHeap, -num)
            else:
                heapq.heappush(minHeap, num)
                
            if len(maxHeap) > len(minHeap) + 1:
                x = -heapq.heappop(maxHeap)
                heapq.heappush(minHeap, x)
                
            if len(minHeap) > len(maxHeap) + 1:
                x = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -x)
                
            if len(maxHeap) == len(minHeap):
                median = (-maxHeap[0] + minHeap[0]) / 2
            elif len(maxHeap) > len(minHeap):
                median = -maxHeap[0]
            else:
                median = minHeap[0]
                
            result.append(median)
            
        return result
```

Step-by-Step Explanation:

1. Initialize the Two Heaps:

   * `maxHeap = []`: This heap represents the lower half of the numbers.

   * Because Python's `heapq` is a min-heap, the numbers are stored as negative values to simulate a max-heap.

   * The largest number in the lower half can therefore be accessed using:

     ```python
     -maxHeap[0]
     ```

   * `minHeap = []`: This heap represents the upper half of the numbers.

   * This uses Python's normal min-heap behavior, so `minHeap[0]` is the smallest number in the upper half.

   * `result = []`: Stores the median after each number is processed.

2. Decide Which Heap Should Receive the New Number:

   * For every number in `arr`:

     ```python
     for num in arr:
     ```

   * We first check:

     ```python
     if not maxHeap or num <= -maxHeap[0]:
     ```

   * If `maxHeap` is empty, the number is placed there.

   * Otherwise, we compare the new number with the largest value currently in the lower half:

     ```python
     -maxHeap[0]
     ```

   * If the new number is smaller than or equal to that value, it belongs in the lower half and is inserted
     into `maxHeap` as a negative value:

     ```python
     heapq.heappush(maxHeap, -num)
     ```

   * Otherwise, the number belongs in the upper half and is inserted normally:

     ```python
     heapq.heappush(minHeap, num)
     ```

3. Balance the Two Heaps:

   * After insertion, one heap may contain too many elements.

   * We want the sizes of the two heaps to differ by at most 1.

   * If the lower-half heap is too large:

     ```python
     if len(maxHeap) > len(minHeap) + 1:
     ```

     we remove its largest actual value:

     ```python
     x = -heapq.heappop(maxHeap)
     ```

     and move it into the upper-half min-heap:

     ```python
     heapq.heappush(minHeap, x)
     ```

   * If the upper-half heap is too large:

     ```python
     if len(minHeap) > len(maxHeap) + 1:
     ```

     we remove its smallest value:

     ```python
     x = heapq.heappop(minHeap)
     ```

     and move it into the lower-half max-heap as a negative value:

     ```python
     heapq.heappush(maxHeap, -x)
     ```

   * This maintains the important invariant:

     ```text
     |len(maxHeap) - len(minHeap)| <= 1
     ```

4. Calculate the Median:

   * Once the heaps are balanced, the median depends on their sizes.

   * If both heaps have the same size:

     ```python
     if len(maxHeap) == len(minHeap):
     ```

     the total number of elements is even.

   * The two middle values are:

     ```text
     -maxHeap[0]
     minHeap[0]
     ```

   * Therefore, the median is their average:

     ```python
     median = (-maxHeap[0] + minHeap[0]) / 2
     ```

   * If `maxHeap` has one more element:

     ```python
     elif len(maxHeap) > len(minHeap):
     ```

     the total number of elements is odd, and the median is:

     ```python
     -maxHeap[0]
     ```

   * If `minHeap` has one more element:

     ```python
     else:
         median = minHeap[0]
     ```

     so the median is the smallest value in the upper half.

5. Store the Median:

   * After calculating the current median:

     ```python
     result.append(median)
     ```

   * This stores the median for the current prefix of the stream.

   * The process then continues with the next incoming number.

6. Return All Medians:

   * After all numbers have been processed:

     ```python
     return result
     ```

   * The returned list contains the median after every element is added.

Walkthrough with Example:

Consider:

```python
arr = [5, 15, 1, 3, 2, 8]
```

1. Process `5`:

   * `maxHeap` is empty, so `5` goes into the lower half.

   ```text
   maxHeap = [-5]
   minHeap = []
   ```

   * `maxHeap` has one more element.

   * Median:

   ```text
   5
   ```

   Result:

   ```text
   [5.0]
   ```

2. Process `15`:

   * `15 > 5`, so it goes into `minHeap`.

   ```text
   maxHeap = [-5]
   minHeap = [15]
   ```

   * Both heaps have the same size.

   * Median:

   ```text
   (5 + 15) / 2 = 10
   ```

   Result:

   ```text
   [5.0, 10.0]
   ```

3. Process `1`:

   * `1 <= 5`, so it goes into `maxHeap`.

   ```text
   maxHeap = [-5, -1]
   minHeap = [15]
   ```

   * `maxHeap` contains one extra element.

   * Median:

   ```text
   5
   ```

   Result:

   ```text
   [5.0, 10.0, 5.0]
   ```

4. Process `3`:

   * `3 <= 5`, so it is added to `maxHeap`.

   * The lower half temporarily has too many elements, so the largest value from the lower half (`5`)
     is moved to `minHeap`.

   The heaps become conceptually:

   ```text
   lower half → [1, 3]
   upper half → [5, 15]
   ```

   * Both heaps now have the same size.

   * Median:

   ```text
   (3 + 5) / 2 = 4
   ```

   Result:

   ```text
   [5.0, 10.0, 5.0, 4.0]
   ```

5. Process `2`:

   * `2 <= 3`, so it belongs to the lower half.

   * The lower half gets one extra element.

   * Its largest value is `3`, so the heaps conceptually become:

   ```text
   lower half → [1, 2]
   upper half → [3, 5, 15]
   ```

   After balancing, the actual split is maintained so that the two heap sizes differ by at most 1.

   * Median:

   ```text
   3
   ```

   Result:

   ```text
   [5.0, 10.0, 5.0, 4.0, 3.0]
   ```

6. Process `8`:

   * `8` is larger than the largest value in the lower half, so it goes into the upper half.

   * The heaps are balanced.

   * The two middle values are `3` and `5`.

   * Median:

   ```text
   (3 + 5) / 2 = 4
   ```

   Final Result:

   ```text
   [5.0, 10.0, 5.0, 4.0, 3.0, 4.0]
   ```

Key Points:

* Two heaps are used to divide the numbers into two halves.
* `maxHeap` stores the lower half of the numbers.
* `minHeap` stores the upper half of the numbers.
* Python's `heapq` is a min-heap, so negative values are used to simulate a max-heap.
* `-maxHeap[0]` gives the largest value in the lower half.
* `minHeap[0]` gives the smallest value in the upper half.
* The heaps are balanced so their sizes differ by at most 1.
* If the heaps have equal sizes, the median is the average of their two roots.
* If one heap contains one additional element, its root is the median.
* A new median is calculated and stored after every number arrives.
* We never need to fully sort all numbers after each insertion.

The most important invariant to remember is:

```text
maxHeap = lower half
minHeap = upper half

largest(lower half) <= smallest(upper half)

|len(maxHeap) - len(minHeap)| <= 1
```

This is what allows the median to always be available from the top of the two heaps.

Complexity Analysis:

* Each number is inserted into one of the two heaps.

* Each insertion takes `O(log n)` time in the worst case.

* Rebalancing also requires at most one heap removal and one heap insertion.

* Therefore, processing all `n` numbers takes:

  ```text
  O(n log n)
  ```

  time.

* The two heaps together store all `n` numbers, so the space complexity is:

  ```text
  O(n)
  ```

* The `result` list also stores `n` medians.

Therefore:

* Time Complexity: O(n log n)
* Auxiliary Space Complexity: O(n)

This two-heaps technique is one of the most important patterns for streaming-data problems because it allows us
to maintain the middle of a dynamically changing collection without repeatedly sorting all the values.

'''