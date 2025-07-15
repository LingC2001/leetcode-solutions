# LeetCode [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

---

## 1. Problem Description

### Description:
You are given an `m x n` matrix of integers where each row is sorted in ascending order, and the first integer of each row is greater than the last integer of the previous row. Write a function that returns `True` if a given target integer exists in the matrix, or `False` otherwise.

---

### Input:
- `matrix`: List[List[int]] – a 2D list of integers with dimensions `m x n`.  
- `target`: int – the integer value to search for.

---

### Output:
- `bool` – `True` if `target` is found in `matrix`, `False` otherwise.

---

### Example(s):
**Example 1:**
```
Input:
matrix = [
  [1,  3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]
target = 3

Output: True
```

**Example 2:**
```
Input:
matrix = [
  [1,  3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]
target = 13

Output: False
```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```
Input:
matrix = [[1]]
target = 1

Output: True
Explanation: Single-element matrix matching the target.
```

**Test Case 2:**
```
Input:
matrix = [[1, 2, 3]]
target = 4

Output: False
Explanation: Single row that does not contain the target.
```

</details>

---

## 2. Approach

We treat the entire 2D matrix as a sorted 1D array of length `m * n` and perform a binary search:

1. Let `m` = number of rows, `n` = number of columns.
2. Initialize two pointers:
   - `left = 0`
   - `right = m * n - 1`
3. While `left <= right`:
   - Compute `mid = (left + right) // 2`.
   - Map `mid` back to 2D indices:
     - `row = mid // n`
     - `col = mid % n`
   - Compare `matrix[row][col]` with `target`:
     - If equal, return `True`.
     - If `target` is less, move `right = mid - 1`.
     - If `target` is greater, move `left = mid + 1`.
4. If loop completes without finding the target, return `False`.

Key decisions:
- We never build an explicit 1D list; we compute indices on the fly.
- Binary search yields O(log(m*n)) time, optimal for search in sorted data.

Alternative:
- Two-phase search: first locate row, then binary search within row — also O(log m + log n) ≈ O(log (m n)), but more code.

---

## 3. Algorithm Complexity

- Time Complexity: O(log(m * n)), since we halve the search space each iteration.  
- Space Complexity: O(1), only constant extra space for pointers and indices.

---

## 4. Usage Instructions

To use the `searchMatrix` function, import or include it in your Python script:

```python
from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        row, col = divmod(mid, n)
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Example usage:
if __name__ == "__main__":
    mat = [
        [1,  3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    print(searchMatrix(mat, 3))   # True
    print(searchMatrix(mat, 13))  # False
```

- Ensure your environment has Python 3.x installed.
- Run `python your_script.py` to see the results.