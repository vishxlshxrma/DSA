'''
Problem Statement:
Geekina got stuck on an island. There is only one shop on this island and it is open on all days of the week except for 
Sunday. Consider following constraints:

N - The maximum unit of food you can buy each day.
S - Number of days you are required to survive.
M - Unit of food required each day to survive.
Currently, it's Monday, and she needs to survive for the next S days, initially she has no food.
Find the minimum number of days on which you need to buy food from the shop so that she can survive the next S days. If it 
is not possible to survive for S days then return -1.

Example 1:
Input: S = 10, N = 16, M = 2
Output: 2
Explaination: One possible solution is to buy a box on the first day (Monday), it's sufficient to eat from this box up to 
8th day (Monday) inclusive. Now, on the 9th 
day (Tuesday), you buy another box and use the chocolates in it to survive the 9th and 10th day.

Example 2:
Input: S = 10, N = 9, M = 8
Output: -1
Explaination: Let's start by detailing the days of the week and the net number of food units available after purchasing and 
consuming them:
Monday - Net 1 food unit available.
Tuesday - Net 2 food units available.
Wednesday - Net 3 food units available.
Thursday - Net 4 food units available.
Friday - Net 5 food units available.
Saturday - Net 6 food units available.
Sunday - 6 food units available and that is not sufficient amount of food units to survive and you can't buy more on Sunday.

'''

class Solution:
    def minimumDays(self, S, N, M):
        if N < M:
            return -1
        
        if S > 6 and 6 * N < 7 * M:
            return -1
        
        return (S * M + N - 1) // N
    
'''
The goal is to determine the **minimum number of days** on which Geekina needs to buy food so that she
can survive for the next `S` days. The shop is closed every Sunday, so we must first determine whether
survival is even possible. If it is, we use a greedy approach to minimize the number of shopping days.

Greedy Idea:

- Whenever we buy food, we should always buy the **maximum amount possible (`N` units)**.
- Buying less than `N` units can never reduce the number of shopping days because every visit to the shop
  has the same maximum purchase limit.
- Therefore, once we know survival is possible, the minimum number of shopping days is simply the total
  food required divided by the maximum food that can be bought in one shopping day.

Code Breakdown:

```python
class Solution:
    def minimumDays(self, S, N, M):

        # If one day's purchase is not enough to survive one day
        if N < M:
            return -1

        # If surviving an entire week is impossible,
        # then survival for S days is impossible.
        if S > 6 and 6 * N < 7 * M:
            return -1

        # Minimum shopping days required
        return (S * M + N - 1) // N
```

Explanation:

1. Check if One Day's Purchase is Enough to Survive One Day:
   ```python
   if N < M:
       return -1
   ```
   - `N` represents the maximum amount of food that can be bought in one day.
   - `M` represents the amount of food required to survive for one day.
   - If `N < M`, then even on a day when the shop is open, Geekina cannot buy enough food to survive that
     single day.
   - Therefore, surviving for `S` days is impossible, so we immediately return `-1`.

2. Check if Survival Across a Full Week is Possible:
   ```python
   if S > 6 and 6 * N < 7 * M:
       return -1
   ```
   - This is the most important observation in the problem.
   - In every week:
     - The shop is open for **6 days (Monday to Saturday)**.
     - The shop is closed on **Sunday**.
   - Therefore, during one week:
     - Maximum food that can be purchased:
       ```python
       6 * N
       ```
     - Total food required to survive:
       ```python
       7 * M
       ```
   - If:
     ```python
     6 * N < 7 * M
     ```
     then even after buying the maximum possible food on every available shopping day,
     Geekina still cannot collect enough food to survive the week.
   - Since every future week follows the same pattern, surviving for `S` days becomes impossible.
   - We only perform this check when `S > 6` because if the survival period is 6 days or less,
     Sunday is never encountered.

3. Calculate the Minimum Shopping Days:
   ```python
   return (S * M + N - 1) // N
   ```
   - First calculate the total food required:
     ```python
     total_food_required = S * M
     ```
   - Every shopping day allows purchasing at most:
     ```python
     N units
     ```
   - Since our greedy strategy is to always buy the maximum amount of food whenever we visit the shop,
     the minimum number of shopping days is:
     ```python
     ceil(total_food_required / N)
     ```
   - Since Python integer division truncates toward zero, we compute the ceiling using:
     ```python
     (total_food_required + N - 1) // N
     ```
   - This gives the minimum number of shopping days needed.

Example Walkthrough:

Let's go through an example to understand how the algorithm works.

```python
S = 10
N = 16
M = 2
```

Step-by-Step Execution:

1. Check Daily Survival:
   - Can we buy enough food for one day?
   - `N = 16`
   - `M = 2`
   - Since:
     ```python
     16 >= 2
     ```
     the first condition is satisfied.

2. Check Weekly Survival:
   - Since `S > 6`, Sunday will occur.
   - Maximum food that can be purchased in one week:
     ```python
     6 * 16 = 96
     ```
   - Food required during one week:
     ```python
     7 * 2 = 14
     ```
   - Since:
     ```python
     96 >= 14
     ```
     surviving the week is possible.

3. Calculate Total Food Required:
   ```python
   total_food_required = 10 * 2 = 20
   ```

4. Calculate Minimum Shopping Days:
   ```python
   ceil(20 / 16)
   ```
   Using integer arithmetic:
   ```python
   (20 + 16 - 1) // 16
   = 35 // 16
   = 2
   ```

5. Return Answer:
   - The function returns:
     ```python
     2
     ```

Another Example:

```python
S = 10
N = 26
M = 23
```

1. Daily Survival:
   ```python
   26 >= 23
   ```
   Daily survival is possible.

2. Weekly Survival:
   Maximum food purchasable:
   ```python
   6 * 26 = 156
   ```
   Food required:
   ```python
   7 * 23 = 161
   ```
   Since:
   ```python
   156 < 161
   ```
   Geekina cannot collect enough food before Sunday arrives.

3. Therefore:
   ```python
   return -1
   ```

Key Points

- This problem is solved using a **Greedy Approach**.
- The greedy choice is to **always buy the maximum possible amount of food (`N` units)** whenever a purchase is made.
- Before applying the greedy strategy, we first verify that survival is actually possible by checking:
  - Whether one day's purchase can satisfy one day's food requirement (`N >= M`).
  - Whether enough food can be collected before every Sunday (`6 * N >= 7 * M`).
- Once survival is confirmed, the answer reduces to finding the minimum number of shopping days, which is:
  ```python
  ceil((S * M) / N)
  ```
- Time Complexity: **O(1)** because only a few arithmetic operations are performed.
- Space Complexity: **O(1)** because no extra data structures are used.
'''