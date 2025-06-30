# LeetCode [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)

---

## 1. Problem Description

### Description:
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

You must solve it **without using division** and in O(n) time.

---

### Input:
- `nums`: A list of integers.

---

### Output:
- A list of integers where each element is the product of all other elements in `nums` except the one at the same index.

---

### Example(s):
**Example 1:**
```

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

```

**Example 2:**
```

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```

Input: nums = [2,3,4,5]
Output: [60,40,30,24]

```

**Test Case 2:**
```

Input: nums = [0,0]
Output: [0,0]
Explanation: Multiple zeros cause all products except self to be zero.

```

</details>

---

## 2. Approach

The core idea is to calculate the product of all elements except for the current one without using division, which can be challenging when zeros are present.

To achieve this efficiently, the algorithm uses two passes to compute prefix and suffix products:

- **Prefix products:** For each position, calculate the product of all elements before it.
- **Suffix products:** For each position, calculate the product of all elements after it.

Once both prefix and suffix products are computed, the final product for any index can be obtained by multiplying the prefix product just before it with the suffix product just after it.

This method avoids recalculating products multiple times and handles edge cases naturally, such as zeros in the input. It runs in linear time with extra linear space for the prefix and suffix arrays.

---

## 3. Algorithm Complexity

- **Time Complexity:** O(n), where n is the length of `nums`. The array is traversed multiple times, but all operations remain linear.
- **Space Complexity:** O(n), due to the additional arrays used for prefix products, suffix products, and the result.

---