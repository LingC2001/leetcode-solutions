
---

# LeetCode [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/)

---

## 1. Problem Description

### Description:

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

---

### Input:

* A list of integers `nums`

---

### Output:

* An integer representing the length of the longest consecutive sequence.

---

### Example(s):

**Example 1:**

```
Input: [100,4,200,1,3,2]
Output: 4
```

**Example 2:**

```
Input: [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

---

## 2. Approach

* Convert the list to a set for O(1) lookups.
* Iterate over each number in the set.
* Only start counting when `n-1` is not in the set — this ensures you only check the start of each sequence.
* Increment a `length` counter while the consecutive numbers exist (`n+length` in set).
* Keep track of the longest sequence found.

This approach ensures each number is processed at most once, resulting in an efficient solution.

---

## 3. Algorithm Complexity

* **Time Complexity:** O(n), where n is the number of integers in the list.
* **Space Complexity:** O(n), for the set of numbers.

---
