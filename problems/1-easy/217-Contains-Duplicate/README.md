# LeetCode [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/)

---

## 1. Problem Description

### Description:
Given an integer array `nums`, determine if any value appears at least twice in the array. Return `True` if any duplicates exist, otherwise return `False`.

---

### Input:
- `nums`: A list of integers.

---

### Output:
- A boolean value `True` if any duplicates exist in `nums`, otherwise `False`.

---

### Example(s):
**Example 1:**
```

Input: nums = [1,2,3,1]
Output: True

```

**Example 2:**
```

Input: nums = [1,2,3,4]
Output: False

```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: True
Explanation: Multiple duplicates exist.

```

**Test Case 2:**
```

Input: nums = []
Output: False
Explanation: Empty list contains no duplicates.

```

</details>

---

## 2. Approach

The solution uses a set to track unique elements encountered while iterating through the list. For each element:

- Check if it already exists in the set.
- If yes, return `True` immediately (duplicate found).
- Otherwise, add the element to the set and continue.

If the loop completes without finding duplicates, return `False`.

**Note:** Your current code has a logic error where `return False` is inside the loop, causing premature termination after the first element. It should be placed outside the loop to ensure the entire list is checked.

---

## 3. Algorithm Complexity

- **Time Complexity:** O(n), where n is the length of `nums`. Each element is processed once.
- **Space Complexity:** O(n), as a set is used to store unique elements.

---