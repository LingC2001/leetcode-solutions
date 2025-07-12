# LeetCode [704. Binary Search](https://leetcode.com/problems/binary-search/)

---

## 1. Problem Description

### Description:

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, return the index of `target` if it is in the array.
If it is not present, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

---

### Input:

* `nums`: A list of integers sorted in ascending order.
* `target`: An integer to search for.

---

### Output:

* An integer representing the index of `target` in `nums`, or `-1` if not found.

---

### Example(s):

**Example 1:**

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
```

**Example 2:**

```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**

```
Input: nums = [1], target = 1
Output: 0
Explanation: Only one element and it matches the target.
```

**Test Case 2:**

```
Input: nums = [1,3,5,7], target = 4
Output: -1
Explanation: 4 is not present in the list.
```

</details>

---

## 2. Approach

This problem is a classic application of the **Binary Search** algorithm, which is ideal for searching in a sorted list.

* The key idea is to repeatedly divide the search space in half.
* Begin with two pointers representing the bounds of the current search window.
* At each step:

  * Calculate the middle index.
  * If the middle element is the target, return its index.
  * If the middle element is greater than the target, move the right boundary to the left of mid.
  * If it is smaller, move the left boundary to the right of mid.
* If the search window is exhausted without finding the target, return `-1`.

### Why this works:

* Binary search exploits the ordering property of the array to eliminate half of the remaining elements with each comparison.
* It ensures logarithmic time performance and is highly efficient for large, sorted datasets.

---

## 3. Algorithm Complexity

* **Time Complexity:** O(log n), since the search space is halved on each iteration.
* **Space Complexity:** O(1), as the search is done in-place using constant memory.

---
