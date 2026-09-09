'''
Problem Statement:
You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. 
You are also given an integer k.
Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order. The answer is guaranteed to be unique(except for the order in which the points 
are returned.)

Example 1:
Input: points = [[0,2],[2,2]], k = 1
Output: [[0,2]]
Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).


Example 2:
Input: points = [[0,2],[2,0],[2,2]], k = 2
Output: [[0,2],[2,0]]
Explanation: The output [2,0],[0,2] would also be accepted.
'''

from email.mime import text
import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []

        for point in points:
            x = point[0]
            y = point[1]

            distance = x * x + y * y

            if len(heap) < k:
                heapq.heappush(heap, (-distance, point))
            else:
                heapq.heappush(heap, (-distance, point))
                heapq.heappop(heap)

        result = []

        for distance, point in heap:
            result.append(point)

        return result

'''
The K Closest Points to Origin problem asks us to find the `k` points that are closest to the origin `(0, 0)`.

The key idea is to calculate the distance of every point from the origin and maintain a max-heap containing
only the `k` closest points seen so far.

Since Python's `heapq` implements a min-heap, we store the negative of each distance. This makes the point
with the largest distance behave like the smallest value in the heap, allowing us to remove the farthest
point whenever the heap grows larger than `k`.

Code Explanation:

The provided code uses Python's `heapq` module and stores each point together with its negative squared
distance. Let's break it down step-by-step:

```python
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x = point[0]
            y = point[1]

            distance = x * x + y * y

            if len(heap) < k:
                heapq.heappush(heap, (-distance, point))
            else:
                heapq.heappush(heap, (-distance, point))
                heapq.heappop(heap)

        result = []

        for distance, point in heap:
            result.append(point)

        return result
````

Step-by-Step Explanation:

1. Initialize the Heap:

   * `heap = []`: Creates an empty list that will be used as a heap.

   * Our goal is to keep at most `k` points inside this heap.

   * Each heap element will have the form:

     ```text
     (-distance, point)
     ```

   * For example:

     ```text
     (-10, [1, 3])
     ```

     means that point `[1, 3]` has squared distance `10` from the origin.

2. Traverse Every Point:

   * We iterate through all points:

     ```python
     for point in points:
     ```

   * If:

     ```python
     point = [1, 3]
     ```

     then:

     ```python
     x = point[0]
     y = point[1]
     ```

     gives:

     ```text
     x = 1
     y = 3
     ```

3. Calculate the Distance:

   * The Euclidean distance between `(x, y)` and `(0, 0)` is:

     ```text
     sqrt(x² + y²)
     ```

   * However, we do not actually need to calculate the square root.

   * We only need to compare which point is closer.

   * Therefore, we use the squared distance:

     ```python
     distance = x * x + y * y
     ```

   * For example:

     ```text
     point = [1, 3]

     distance = 1² + 3²
              = 1 + 9
              = 10
     ```

   * If one squared distance is smaller than another, its actual Euclidean distance will also be smaller.

   * Therefore, avoiding the square root gives us the same ordering while keeping the calculation simpler.

4. Why We Use Negative Distance:

   * Python's `heapq` implements a min-heap.

   * Normally, the smallest value is removed by:

     ```python
     heapq.heappop(heap)
     ```

   * But in this problem, when we have more than `k` points, we want to remove the FARTHEST point.

   * Suppose the distances are:

     ```text
     2
     5
     10
     ```

   * If we stored these directly in a min-heap, `2` would be removed first.

   * But `2` represents the closest point, which is exactly the point we want to keep.

   * Therefore, we negate the distances:

     ```text
     Actual Distance      Stored Priority

           2                   -2
           5                   -5
          10                  -10
     ```

   * Now the smallest value is:

     ```text
     -10
     ```

   * But `-10` represents the largest actual distance, `10`.

   * Therefore:

     ```python
     heapq.heappop(heap)
     ```

     removes the farthest point.

   * This allows Python's min-heap to behave like a max-heap based on distance.

5. Add Points to the Heap:

   * If the heap contains fewer than `k` points:

     ```python
     if len(heap) < k:
         heapq.heappush(heap, (-distance, point))
     ```

     we simply add the current point.

   * The heap entry contains:

     ```text
     (-distance, point)
     ```

   * For example:

     ```python
     heapq.heappush(heap, (-10, [1, 3]))
     ```

6. Maintain a Heap of Size `k`:

   * If the heap already contains `k` points:

     ```python
     else:
         heapq.heappush(heap, (-distance, point))
         heapq.heappop(heap)
     ```

   * We first insert the new point.

   * The heap temporarily contains:

     ```text
     k + 1 points
     ```

   * We then remove one point using:

     ```python
     heapq.heappop(heap)
     ```

   * Because we stored negative distances, the point with the largest actual distance is removed.

   * Therefore, after every iteration:

     ```text
     heap = k closest points seen so far
     ```

7. Extract the Points:

   * After processing every point, the heap contains tuples of the form:

     ```text
     (-distance, point)
     ```

   * But the problem only asks us to return the points.

   * Therefore:

     ```python
     result = []
     ```

   * Then:

     ```python
     for distance, point in heap:
         result.append(point)
     ```

   * We ignore the stored distance and add only the point to the result.

   * Finally:

     ```python
     return result
     ```

Walkthrough with Example:

Consider:

```python
points = [[1, 3], [-2, 2]]
k = 1
```

1. Initialization:

   ```text
   heap = []
   ```

2. Process `[1, 3]`:

   ```text
   x = 1
   y = 3

   distance = 1² + 3²
            = 10
   ```

   Store:

   ```text
   (-10, [1, 3])
   ```

   Heap:

   ```text
   [(-10, [1, 3])]
   ```

3. Process `[-2, 2]`:

   ```text
   x = -2
   y = 2

   distance = (-2)² + 2²
            = 4 + 4
            = 8
   ```

   Store:

   ```text
   (-8, [-2, 2])
   ```

   The heap temporarily represents:

   ```text
   (-10, [1, 3])
   (-8, [-2, 2])
   ```

   But:

   ```text
   k = 1
   ```

   so we can only keep one point.

4. Remove the Farthest Point:

   * `heapq.heappop()` removes the smallest stored value:

     ```text
     -10
     ```

   * `-10` represents actual squared distance `10`.

   * Therefore, `[1, 3]` is removed.

   * The heap now contains:

     ```text
     (-8, [-2, 2])
     ```

5. Extract the Point:

   * Ignore the distance and take the point:

     ```python
     [-2, 2]
     ```

Final Result:

```python
[[-2, 2]]
```

Key Points:

* The squared Euclidean distance from `(x, y)` to `(0, 0)` is:

  ```text
  x² + y²
  ```

* We do not need `sqrt()` because square root does not change the ordering of non-negative distances.

* Each heap entry stores:

  ```text
  (-distance, point)
  ```

* Python's `heapq` is a min-heap.

* Negating the distance makes it behave like a max-heap with respect to the original distances.

* When the heap becomes larger than `k`, `heappop()` removes the farthest point.

* Therefore, the heap always contains the `k` closest points seen so far.

* At the end, we extract only the points and ignore their stored distances.

Complexity Analysis:

Let `n` be the total number of points.

1. Traversing the Points:

   * Every point is processed once.

2. Heap Operations:

   * The heap contains at most `k` points.

   * `heappush()` takes:

     ```text
     O(log k)
     ```

   * `heappop()` also takes:

     ```text
     O(log k)
     ```

   * We perform these operations for up to `n` points.

Overall Time Complexity:

```text
O(n log k)
```

Space Complexity:

* The heap contains at most `k` points:

  ```text
  O(k)
  ```

* The result contains `k` points as required by the output.

Therefore, the auxiliary heap space is:

```text
O(k)
```

The most important pattern to remember from this problem is:

```text
K Closest Points
        ↓
Calculate x² + y²
        ↓
Store (-distance, point)
        ↓
Negative distance simulates max-heap behavior
        ↓
Maintain heap size k
        ↓
When size > k, remove farthest
        ↓
Heap contains k closest points
        ↓
Extract and return the points
```

This uses the same Top-K heap pattern as Kth Largest and Top K Frequent Elements, but here the priority is
the point's distance from the origin.
'''