# LeetCode [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

---

## 1. Problem Description

### Description:
Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix. This matrix has the following properties:
1. Integers in each row are sorted in ascending order from left to right.
2. The first integer of each row is greater than the last integer of the previous row.

Return `true` if `target` is found in the matrix, and `false` otherwise.

---

### Input:
* `matrix`: A list of `m` lists, each containing `n` integers.
* `target`: An integer to search for in the matrix.

---

### Output:
* A boolean value:
  - `true` if `target` exists in the matrix.
  - `false` otherwise.

---

### Example(s):
**Example 1:**
```
Input: matrix = [
  [1,  3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
], target = 3
Output: true
```

**Example 2:**
```
Input: matrix = [
  [1,  3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
], target = 13
Output: false
```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```
Input: matrix = [[1]], target = 1
Output: true
Explanation: Single-element matrix matches the target.
```

**Test Case 2:**
```
Input: matrix = [[1,2,3]], target = 2
Output: true
Explanation: Single row, target in the middle.
```

</details>

---

## 2. Approach

We treat the 2D matrix as a virtual 1D sorted array of length `m * n`, then apply binary search:

1. Compute total elements: `total = m * n`.
2. Initialize two pointers, `left = 0` and `right = total - 1`.
3. While `left <= right`:
   - Compute `mid = (left + right) // 2`.
   - Map `mid` back to 2D indices:
     * `row = mid // n`
     * `col = mid % n`
   - Compare `matrix[row][col]` with `target`:
     - If equal, return `true`.
     - If `target` is smaller, move `right = mid - 1`.
     - Otherwise, move `left = mid + 1`.
4. If the loop ends without finding the target, return `false`.

Key Decisions:
- Flattening avoids two-phase search (first row, then column) and gives a single log-time binary search.
- Space usage remains O(1) since no auxiliary array is built.

Alternative:
- A two-step binary search: first on the first column to locate the candidate row, then binary search within that row. This is also O(log m + log n), comparable in complexity.

Pattern Used:
- Binary Search on a virtual 1D representation.

---

## 3. Algorithm Complexity

- Time Complexity: O(log (m × n)) ≃ O(log m + log n), since we perform binary search over `m*n` elements.
- Space Complexity: O(1), only a handful of integer variables are used.