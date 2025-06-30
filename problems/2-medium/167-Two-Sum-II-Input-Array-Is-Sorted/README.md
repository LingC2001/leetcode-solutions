# LeetCode [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

---

## 1. Problem Description

### Description:
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Return the indices of the two numbers (1-indexed) as an integer array `[index1, index2]` of length 2.

---

### Input:
- `numbers`: A sorted list of integers.
- `target`: An integer representing the target sum.

---

### Output:
- A list of two integers representing the 1-based indices of the two numbers that add up to `target`.

---

### Example(s):
**Example 1:**
```

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Return indices 1 and 2.

```

**Example 2:**
```

Input: numbers = [2,3,4], target = 6
Output: [1,3]

```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: -1 + 0 = -1

```

**Test Case 2:**
```

Input: numbers = [1,2,3,4,4,9,56,90], target = 8
Output: [4,5]
Explanation: 4 + 4 = 8

```

</details>

---

## 2. Approach

The solution uses the two-pointer technique, leveraging the sorted property of the input array:

- Initialize two pointers: `lower_index` at the start and `higher_index` at the end.
- Calculate the sum of elements at both pointers.
- If the sum is greater than the target, decrement the higher pointer to reduce the sum.
- If the sum is less than the target, increment the lower pointer to increase the sum.
- If the sum equals the target, return the 1-based indices.
- This approach efficiently finds the pair in a single pass.

---

## 3. Algorithm Complexity

- **Time Complexity:** O(n), where n is the length of the input list. Each element is visited at most once.
- **Space Complexity:** O(1), as only pointers and variables are used, no extra space proportional to input size.

---
