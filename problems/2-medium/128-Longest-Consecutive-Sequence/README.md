# LeetCode [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/)

---

## 1. Problem Description

### Description:
Given an unsorted array of integers `nums`, find the length of the longest consecutive elements sequence.

---

### Input:
- `nums`: A list of integers.

---

### Output:
- An integer representing the length of the longest consecutive elements sequence.

---

### Example(s):
**Example 1:**
```

Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4].

```

**Example 2:**
```

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```

Input: nums = []
Output: 0
Explanation: Empty list has no consecutive sequence.

```

**Test Case 2:**
```

Input: nums = [10]
Output: 1
Explanation: Single element sequence.

```

</details>

---

## 2. Approach

The solution uses a set for O(1) lookups and identifies the start of a consecutive sequence by checking if the previous number `(n - 1)` is not in the set. For each sequence start, it counts the length of consecutive numbers by incrementing from `n` until the sequence ends.

- Convert the list to a set for fast membership testing.
- Iterate over the set:
  - For each number, check if it is the start of a sequence.
  - If yes, count consecutive numbers incrementally.
- Track and update the maximum sequence length found.
- Return the maximum length after processing all numbers.

This approach avoids sorting and achieves linear time complexity.

---

## 3. Algorithm Complexity

- **Time Complexity:** O(n), where n is the number of elements in `nums`. Each element is processed at most twice.
- **Space Complexity:** O(n), used by the set to store the elements.

---