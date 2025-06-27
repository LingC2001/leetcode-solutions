# LeetCode [1. Two Sum](https://leetcode.com/problems/two-sum/description/)

---

## 1. Problem Description

### Description:
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

---

### Input:
- `nums`: A list of integers.
- `target`: An integer representing the target sum.

---

### Output:
- A list containing two integers representing the indices of the two numbers in `nums` that add up to `target`.

---

### Example(s):
**Example 1:**
```

Input: nums = \[2,7,11,15], target = 9
Output: \[1,0]

```

**Example 2:**
```

Input: nums = \[3,2,4], target = 6
Output: \[2,1]

```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```

Input: nums = \[3,3], target = 6
Output: \[1,0]
Explanation: The two elements 3 and 3 sum to 6.

```

**Test Case 2:**
```

Input: nums = \[1,2,3,4,5], target = 9
Output: \[4,3]
Explanation: The elements at indices 4 and 3 (5 + 4) sum to 9.

```

</details>

---

## 2. Approach

The solution uses a hash map (dictionary) to store the values and their indices as we iterate through the list. For each element `nums[i]`, it checks whether `target - nums[i]` has already been seen. If so, the pair of indices that add up to `target` is returned immediately. Otherwise, the current number and its index are stored in the dictionary for future reference.

- We iterate through the list once.
- Use a dictionary to look up complements in O(1) time.
- Return indices as soon as the pair is found.
- This approach is optimal for time complexity compared to brute force, which would check all pairs (O(n²)).

---

## 3. Algorithm Complexity

- **Time Complexity:** O(n), where n is the length of `nums`. Each element is visited once, and dictionary lookups are O(1).
- **Space Complexity:** O(n), as extra space is used to store elements in the dictionary.

---