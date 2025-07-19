# LeetCode [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

---

## 1. Problem Description

### Description:  
Suppose an array of unique integers sorted in ascending order is rotated at some pivot unknown to you beforehand. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` (rotated at pivot index 3)  
- `[6,7,0,1,2,4,5]` (rotated at pivot index 5)

Given the rotated array `nums`, return the minimum element of this array. You must write an algorithm that runs in O(log n) time.

---

### Input:  
- `nums`: List[int] – a non-empty list of unique integers, originally sorted in ascending order then rotated.

---

### Output:  
- `int` – the minimum element in the rotated array.

---

### Example(s):

**Example 1:**
```
Input: nums = [3, 4, 5, 1, 2]
Output: 1
```

**Example 2:**
```
Input: nums = [4, 5, 6, 7, 0, 1, 2]
Output: 0
```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```
Input: nums = [1]
Output: 1
Explanation: Only one element, which is the minimum.
```

**Test Case 2:**
```
Input: nums = [2, 1]
Output: 1
Explanation: Rotated at index 0 or 1; minimum is 1.
```

</details>

---

## 2. Approach

We use a modified **Binary Search** (Two Pointers pattern) to achieve O(log n) time:

1. Initialize two pointers:
   - `left = 0`
   - `right = len(nums) - 1`

2. While `left < right`:
   - Compute `mid = (left + right) // 2`.
   - Compare `nums[mid]` with `nums[right]`:
     - If `nums[mid] < nums[right]`, the minimum lies in the left half (including `mid`), so set `right = mid`.
     - Else (`nums[mid] >= nums[right]`), the minimum lies in the right half (excluding `mid`), so set `left = mid + 1`.

3. When `left == right`, the loop ends and `nums[left]` is the minimum.

This works because in a rotated sorted array, one half is always in proper ascending order, and the pivot (minimum) lies in the other half.

**Why this is optimal:**  
- We discard half of the search space at each step, guaranteeing O(log n) runtime.  
- We use only constant extra space.

**Alternative (Brute-Force):**  
Scan the entire array in O(n) time to find the minimum. This is simpler but does not meet the O(log n) requirement.

---

## 3. Algorithm Complexity

- Time Complexity: O(log n), where n = len(nums).  
- Space Complexity: O(1), only pointers and indices are used.

---

## 4. Usage Instructions

Save the solution in a file (e.g., `solution.py`) and run as follows:

```python
from typing import List

def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1
    return nums[left]

if __name__ == "__main__":
    test_arrays = [
        [3, 4, 5, 1, 2],
        [4, 5, 6, 7, 0, 1, 2],
        [1],
        [2, 1]
    ]
    for arr in test_arrays:
        print(f"Minimum in {arr} → {findMin(arr)}")
```

Running this script will output the minimum element for each test case.