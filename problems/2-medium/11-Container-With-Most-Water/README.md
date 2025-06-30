# LeetCode [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

---

## 1. Problem Description

### Description:
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the i-th line are at `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container that holds the most water.

Return the maximum amount of water a container can store.

---

### Input:
- `height`: A list of integers representing the heights of vertical lines.

---

### Output:
- An integer representing the maximum amount of water the container can store.

---

### Example(s):
**Example 1:**
```

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

```

**Example 2:**
```

Input: height = [1,1]
Output: 1

```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```

Input: height = [4,3,2,1,4]
Output: 16
Explanation: Container is formed between lines at index 0 and 4 (4 * distance 4).

```

**Test Case 2:**
```

Input: height = [1,2,1]
Output: 2
Explanation: Container is formed between lines at index 0 and 2 (1 * distance 2).

```

</details>

---

## 2. Approach

The solution uses the **Two-Pointer Technique** to efficiently find the largest possible container.

### General Strategy:
- **Initialize two pointers:** One at the start and one at the end of the array.
- **Calculate the container size:** The amount of water a container can hold is determined by the shorter of the two lines multiplied by the distance between them.
- **Move the pointer of the shorter line:** To potentially find a taller line that may result in a larger container, always move the pointer pointing to the shorter line. Moving the taller line would only decrease the width without guaranteeing more height.
- **Continue until pointers meet:** The process stops when the two pointers cross.

### Why this is optimal:
- The brute-force solution would involve checking all possible pairs, which would take O(n²) time. By using the two-pointer technique, the solution finds the maximum area in O(n) time by eliminating suboptimal possibilities with each pointer move.

---

## 3. Algorithm Complexity

- **Time Complexity:** O(n), where n is the number of elements in the input list. Each element is visited at most once by either pointer.
  
- **Space Complexity:** O(1), no extra space is used beyond a few variables.

---