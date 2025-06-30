# LeetCode [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

---

## 1. Problem Description

### Description:

You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day.

You want to maximize your profit by choosing a **single day to buy** one stock and choosing a **different day in the future to sell** that stock.

Return the maximum profit you can achieve from this transaction. If no profit is possible, return 0.

---

### Input:

* `prices`: A list of integers representing the stock price on each day.

---

### Output:

* An integer representing the maximum profit achievable. If no profitable transaction exists, return 0.

---

### Example(s):

**Example 1:**

```
Input: prices = [7,1,5,3,6,4]
Output: 5
```

**Example 2:**

```
Input: prices = [7,6,4,3,1]
Output: 0
```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**

```
Input: prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 2.
```

**Test Case 2:**

```
Input: prices = [1,2]
Output: 1
Explanation: Buy on day 1 (price = 1) and sell on day 2 (price = 2), profit = 1.
```

</details>

---

## 2. Approach

The solution uses a **Single-Pass Greedy Strategy** to efficiently track the minimum price seen so far and the maximum profit achievable at each step.

* Iterate through the price list while maintaining the lowest price encountered so far.
* At each step, calculate the profit if you were to sell at the current day's price.
* Continuously update the maximum profit found so far.
* Continuously update the minimum price if a lower price is encountered.

This approach guarantees that each day is processed only once, and ensures the "buy before sell" constraint is satisfied.

---

## 3. Algorithm Complexity

* **Time Complexity:** O(n), where n is the number of days. Each price is processed once.
* **Space Complexity:** O(1), using constant extra space for tracking variables.

---
