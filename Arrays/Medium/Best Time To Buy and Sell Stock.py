'''
Problem statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in 
the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit
    
'''
Let's break down the solution step-by-step to understand how it efficiently finds the maximum profit from the 
list of stock prices.
We are given a list of stock prices, `prices`, where `prices[i]` represents the price of a stock on 
the i'th day. Our goal is to:
1. Buy the stock on one day.
2. Sell it on a future day (after the day we bought it).
3. Maximize the profit (selling price - buying price).
4. If no profit is possible, return `0`.

Solution Explanation:

Here's the code for reference:

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            # Update min_price if the current price is lower than the previous min_price
            min_price = min(min_price, price)
            # Calculate profit if we sold at the current price
            profit = price - min_price
            # Update max_profit if this profit is greater than the previous max_profit
            max_profit = max(max_profit, profit)

        return max_profit
```

Key Concepts:

1. Tracking the Minimum Price (`min_price`):
   - To maximize profit, we want to buy at the lowest price possible and sell at the highest price after the 
   buy day.
   - `min_price` will store the minimum price seen so far as we iterate through the list.
   - Initially, `min_price` is set to `float('inf')`, which is a large value, to ensure that any price in the 
   list will be lower than this initial value.

2. Calculating Profit on Each Day:
   - As we move through each day, we assume that we could potentially sell on that day. So, we calculate the 
   profit we would get if we bought at `min_price` (the lowest price seen so far) and sold at the current 
   day's price.
   - The potential profit on any given day is calculated as:
     ```python
     profit = price - min_price
     ```

3. Updating Maximum Profit (`max_profit`):
   - After calculating the profit for the current day, we check if this profit is higher than the previously 
   recorded `max_profit`.
   - If it is, we update `max_profit` with the new value. This ensures that by the end of the loop, 
   `max_profit` contains the highest possible profit we can achieve by buying and selling once.
   - If the profit is negative or zero on any day, `max_profit` remains unchanged, ensuring that we don't 
   end up with a negative profit.

4. Edge Case - No Profit:
   - If prices are in a strictly decreasing order, there's no way to make a profit. In this case, `max_profit` 
   will remain `0`, as we initialize it with `0` and only update it with positive values.

Example Walkthrough:

Let's take an example `prices = [7, 1, 5, 3, 6, 4]`.

| Day | `price` | `min_price` (so far) | `profit` (current) | `max_profit` (so far) |
|-----|---------|-----------------------|---------------------|------------------------|
| 1   | 7       | 7                     | 0                   | 0                      |
| 2   | 1       | 1                     | 0                   | 0                      |
| 3   | 5       | 1                     | 4                   | 4                      |
| 4   | 3       | 1                     | 2                   | 4                      |
| 5   | 6       | 1                     | 5                   | 5                      |
| 6   | 4       | 1                     | 3                   | 5                      |

- On Day 2, we find `1` as the new minimum price.
- On Day 3, selling at `5` after buying at `1` gives a profit of `4`, so we update `max_profit` to `4`.
- On Day 5, selling at `6` after buying at `1` gives a profit of `5`, which becomes our new `max_profit`.

Complexity Analysis:
- Time Complexity: O(n), where n is the number of days (length of the `prices` list). We only pass 
through the list once.
- Space Complexity: O(1), as we only use a few variables (`min_price`, `max_profit`, and `profit`) to keep 
track of the necessary values.

This solution is optimal because it finds the maximum profit in one pass without the need for nested loops or 
additional data structures.
'''