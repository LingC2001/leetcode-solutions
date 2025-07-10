# LeetCode [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

---

## 1. Problem Description

### Description:

Given a list of daily temperatures, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put `0` instead.

---

### Input:

* `temperatures`: A list of integers representing daily temperatures.

---

### Output:

* A list of integers where each value indicates the number of days until a warmer temperature. If no warmer day exists, the value is `0`.

---

### Example(s):

**Example 1:**

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Example 2:**

```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**

```
Input: temperatures = [30,60,90]
Output: [1,1,0]
Explanation: Every day is followed by a warmer one, except the last.
```

**Test Case 2:**

```
Input: temperatures = [90,80,70,60]
Output: [0,0,0,0]
Explanation: Temperatures keep decreasing; no warmer days ahead.
```

</details>

---

## 2. Approach

This problem is a variation of the "next greater element" pattern, where we need to determine how far ahead in the list a warmer temperature occurs for each day. A **monotonic decreasing stack** is well-suited for this type of problem.

* Iterate through the list of temperatures from left to right.
* Use a stack to store indices of unresolved days in decreasing order of their temperatures.
* For each day:

  * While the current temperature is greater than the temperature at the top of the stack:

    * Pop the index from the stack.
    * Calculate the number of days waited as the difference between current and popped indices.
    * Store the result at the popped index.
* Push the current index onto the stack.
* After processing, the remaining indices in the stack do not have a warmer future day, so their result remains `0`.

### Why this works:

* The stack tracks days waiting for a warmer temperature in an efficient, non-redundant way.
* Each day’s index is pushed and popped at most once, ensuring linear time complexity.
* This approach avoids brute-force nested comparisons and is scalable for large inputs.

---

## 3. Algorithm Complexity

* **Time Complexity:** O(n), where n is the number of elements in the input list. Each index is pushed and popped at most once.
* **Space Complexity:** O(n), for the result list and the stack used to store unresolved indices.

---
