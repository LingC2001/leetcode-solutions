# LeetCode [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

---

## 1. Problem Description

### Description:

Given an array `nums` and an integer `k`, return the maximum value in every contiguous subarray of size `k`.

---

### Input:

* `nums`: List of integers.
* `k`: Size of the sliding window.

---

### Output:

* List of integers representing the max of each sliding window.

---

### Example(s):

**Example 1:**

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```

---

<details>
<summary><strong>Additional Test Cases</strong></summary>

**Test Case 1:**

```
Input: nums = [9,10,9,-7,-4,-8,2,-6], k = 5
Output: [10,10,9,2]
```

**Test Case 2:**

```
Input: nums = [4,3,11,2,1,5], k = 2
Output: [4,11,11,2,5]
```

</details>

---

## 2. Approach

Uses a **double ended queue (deque)** to track potential maximums in each window:

* Maintain a deque (`max_deque`) where elements are in decreasing order.
* For each new element:
  * Remove smaller elements from the back.
  * Append the new element.
* The front of the deque is always the current window's maximum.
* If the outgoing element equals the deque front, pop it.

This ensures we get O(1) access to the max for each window while keeping all operations efficient.

---

### 💡 Why the deque works:

The deque keeps track of **candidates for the max** in order. Elements that can no longer be maximums are removed as we move the window, ensuring efficiency and correctness.

---

## 3. Algorithm Complexity

* **Time:** O(n), where n = len(`nums`). Each element is pushed and popped at most once.
* **Space:** O(k), for the deque.

---
