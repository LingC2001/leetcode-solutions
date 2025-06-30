# LeetCode [15. 3Sum](https://leetcode.com/problems/3sum/)

---

## 1. Problem Description

### Description:
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

The solution set must not contain duplicate triplets.

---

### Input:
- `nums`: A list of integers.

---

### Output:
- A list of lists, where each sublist is a unique triplet that sums to zero.

---

### Example(s):
**Example 1:**
```

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1, -1, 2], [-1, 0, 1]]

```

**Example 2:**
```

Input: nums = [0,1,1]
Output: []

```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: Only one unique triplet exists.

```

**Test Case 2:**
```

Input: nums = [-2,0,0,2,2]
Output: [[-2,0,2]]
Explanation: Duplicate handling ensures each triplet is returned only once.

```

</details>

---

## 2. Approach

This solution uses a **Two-Pointer Technique** on a sorted array to efficiently find all unique triplets that sum to zero.

### General Steps:
- **Sort the input array.** This allows the use of the two-pointer method and simplifies duplicate handling.
- **Iterate through each number in the array.** For each number, treat it as the first number of the triplet and search for the remaining two numbers using two pointers (`lo` and `hi`).
- **Skip duplicates.** If the current number is the same as the previous number, continue to the next iteration to avoid duplicate triplets.
- **Adjust pointers.**
    - If the current sum equals the target, record the triplet and move both pointers, skipping any duplicates.
    - If the current sum is less than the target, move the lower pointer up.
    - If the current sum is greater than the target, move the higher pointer down.
- **Return all unique triplets.**

### Why this is optimal:
- This approach avoids the brute-force O(n³) solution by using sorting and the two-pointer technique to achieve O(n²) time complexity.
- Proper duplicate handling ensures the solution meets the unique triplet requirement efficiently.

---

## 3. Algorithm Complexity

- **Time Complexity:** O(n²)  
  Sorting takes O(n log n), and the two-pointer search takes O(n) for each element.
  
- **Space Complexity:** O(1) (excluding the output list)  
  No extra space is used beyond variables for pointers and result storage.

---