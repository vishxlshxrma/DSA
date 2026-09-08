'''
Problem Statement:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]
'''

import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap = []

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num,count in freq.items():
            if (len(heap) < k):
                heapq.heappush(heap, (count, num))
            else:
                heapq.heappush(heap, (count, num))
                heapq.heappop(heap)

        result = []
        
        for count, num in heap:
            result.append(num)

        return result        


'''

The Top K Frequent Elements problem asks us to find the `k` elements that occur most frequently in an array.

The key idea is to first count the frequency of every number using a dictionary and then maintain a min-heap
of size `k`. Each heap entry stores both the frequency and the number in the form `(frequency, number)`.

Since Python's `heapq` implements a min-heap, the element with the smallest frequency will always be at the
top of the heap. Whenever the heap grows larger than `k`, we remove the element with the smallest frequency.

By the end, the heap contains only the `k` most frequent elements.

Code Explanation:

The provided code uses a frequency dictionary and a min-heap. Let's break it down step-by-step:

```python
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, count in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            else:
                heapq.heappush(heap, (count, num))
                heapq.heappop(heap)

        result = []

        for count, num in heap:
            result.append(num)

        return result

Step-by-Step Explanation:

Initialize the Heap:
heap = []: Creates an empty list that will be used as a min-heap.
The heap will eventually contain at most k elements.

Instead of storing only the number, each heap entry will store:

(frequency, number)

For example:

(3, 1)

means that the number 1 occurs 3 times.

Create the Frequency Dictionary:

We initialize an empty dictionary:

freq = {}

Then traverse every number in nums:

for num in nums:
    freq[num] = freq.get(num, 0) + 1
freq.get(num, 0) means:
If num already exists in the dictionary, return its current frequency.
If num does not exist, return 0.
We then add 1 to the frequency.

For example, if:

nums = [1, 1, 1, 2, 2, 3]

the frequency dictionary becomes:

{
    1: 3,
    2: 2,
    3: 1
}

This means:

Number    Frequency
  1           3
  2           2
  3           1
Traverse the Frequency Dictionary:

We use:

for num, count in freq.items():
freq.items() gives us both the number and its frequency.

For the previous example, the iterations are conceptually:

num = 1, count = 3
num = 2, count = 2
num = 3, count = 1
Store (Frequency, Number) in the Heap:

We push:

(count, num)

into the heap.

For example:

(3, 1)
(2, 2)
(1, 3)
The frequency is placed first because Python compares tuples from left to right.

Therefore, in:

(count, num)

count determines the priority of the heap.

Since heapq is a min-heap, the tuple with the smallest frequency will be removed first.
Maintain a Heap of Size k:

If the heap currently contains fewer than k elements:

if len(heap) < k:
    heapq.heappush(heap, (count, num))

we simply insert the current (frequency, number) pair.

If the heap already contains k elements:

else:
    heapq.heappush(heap, (count, num))
    heapq.heappop(heap)

we first insert the new pair.

The heap temporarily contains k + 1 elements.

We then call:

heapq.heappop(heap)
Since this is a min-heap, the element with the smallest frequency is removed.
Therefore, the heap always keeps only the k elements with the highest frequencies.
Why a Min-Heap Works:

Suppose:

k = 2

And the frequencies are:

1 → 3 times
2 → 2 times
3 → 1 time

The heap entries are:

(3, 1)
(2, 2)
(1, 3)
Since we only want k = 2 elements, one element must be removed.

The min-heap removes:

(1, 3)
This represents number 3, which appears only once.

The remaining heap contains:

(2, 2)
(3, 1)

These correspond to:

2 → appears 2 times
1 → appears 3 times
Therefore, 1 and 2 are the two most frequent elements.
Extract the Numbers from the Heap:

At this point, the heap contains tuples:

(frequency, number)
However, the problem only asks us to return the numbers.

Therefore, we create:

result = []

Then traverse the heap:

for count, num in heap:
    result.append(num)
We ignore count and add only num to the result.

Finally:

return result

returns the k most frequent elements.

Walkthrough with Example:

Consider:

nums = [1, 1, 1, 2, 2, 3]
k = 2

Create Frequency Dictionary:

After traversing nums:

freq = {
    1: 3,
    2: 2,
    3: 1
}

Process Number 1:

num = 1
count = 3

Heap size is less than k.

Push:

(3, 1)

Heap:

[(3, 1)]

Process Number 2:

num = 2
count = 2

Heap size is still less than k.

Push:

(2, 2)

The heap now contains:

(2, 2)
(3, 1)

Heap size is now exactly 2.

Process Number 3:

num = 3
count = 1

The heap already contains k = 2 elements.

Push:

(1, 3)

The heap temporarily contains:

(1, 3)
(2, 2)
(3, 1)

Now remove the smallest-frequency element using:

heapq.heappop(heap)

The removed tuple is:

(1, 3)

The heap now contains:

(2, 2)
(3, 1)

Extract the Numbers:

We traverse the heap and take only the second value from each tuple:

(2, 2) → 2
(3, 1) → 1

Result:

[2, 1]

The problem allows the answer in any order, so [2, 1] and [1, 2] are both valid.

Key Points:

A dictionary is used to count how many times each number occurs.
freq[num] = freq.get(num, 0) + 1 is a common frequency-counting pattern.
freq.items() allows us to access both the number and its frequency.

Each heap entry is stored as:

(frequency, number)
Frequency comes first because it determines the priority in the heap.
Python's heapq implements a min-heap.
The heap is maintained at a maximum size of k.
Whenever the heap would contain more than k elements, the element with the smallest frequency is removed.
Therefore, after processing all unique numbers, the heap contains the k most frequent elements.
The final loop extracts only the numbers from the (frequency, number) tuples.
The order of the returned elements does not matter for this problem.

Complexity Analysis:

Let:

n = total number of elements in nums
m = number of unique elements
Building the Frequency Dictionary:
We traverse all n elements once.

Time Complexity:

O(n)
Building and Maintaining the Heap:
We process each of the m unique elements.
The heap contains at most k elements.

Each heappush() and heappop() operation takes:

O(log k)

Therefore:

O(m log k)
Building the Result:
The heap contains k elements.

Extracting them takes:

O(k)

Overall Time Complexity:

O(n + m log k)

Since m <= n, this is commonly written as:

O(n log k)

Space Complexity:

Frequency dictionary:

O(m)

Heap:

O(k)

Result:

O(k)

Therefore, the auxiliary data structures require:

O(m + k)

which is O(n) in the worst case.

The most important pattern to remember from this problem is:

Top K Frequent Elements
        ↓
Count frequencies using a dictionary
        ↓
Store (frequency, number) in a min-heap
        ↓
Maintain heap size k
        ↓
Smallest frequency gets removed
        ↓
Heap contains k highest-frequency elements
        ↓
Extract and return the numbers

This is the same Top-K heap pattern used in Kth Largest Element, but instead of using the number itself as
the heap priority, we use its frequency.
'''