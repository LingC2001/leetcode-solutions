# LeetCode [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)

---

## 1. Problem Description

### Description:

Given two strings `s1` and `s2`, return `true` if `s2` contains a **permutation** of `s1`, otherwise return `false`.

---

### Input:

* `s1`: Pattern string.
* `s2`: Search string.

---

### Output:

* Boolean indicating if a permutation of `s1` exists as a substring in `s2`.

---

### Example(s):

**Example 1:**

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: True
```

**Example 2:**

```
Input: s1 = "ab", s2 = "eidboaoo"
Output: False
```

---

<details>
<summary><strong>Additional Test Cases</strong></summary>

**Test Case 1:**

```
Input: s1 = "adc", s2 = "dcda"
Output: True
```

**Test Case 2:**

```
Input: s1 = "hello", s2 = "ooolleoooleh"
Output: False
```

</details>

---

## 2. Approach

Uses a **fixed-size sliding window** and character frequency dictionaries:

* If `len(s1) > len(s2)`, return `False`.
* Create frequency maps for `s1` and the first window in `s2`.
* Slide the window across `s2`, updating the map:
  * Add the new character, remove the old one.
  * Clean up 0-count entries to match dictionary structure.
  * Compare maps — if equal, return `True`.
* Return `False` if no match found.

### 💡 Why direct dict comparison works:

A permutation has the same character counts. Zero-count entries are removed to avoid mismatches from extra keys.

---

## 3. Algorithm Complexity

* **Time:** O(n), where n = len(`s2`)
* **Space:** O(1), limited to 26 lowercase letters

---
