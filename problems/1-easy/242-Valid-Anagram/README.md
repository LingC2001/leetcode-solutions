# LeetCode [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)

---

## 1. Problem Description

### Description:
Given two strings `s` and `t`, determine if `t` is an anagram of `s`. An anagram means both strings contain the same characters with the same frequencies, but possibly in a different order.

---

### Input:
- `s`: A string.
- `t`: Another string.

---

### Output:
- A boolean value `True` if `t` is an anagram of `s`, otherwise `False`.

---

### Example(s):
**Example 1:**
```

Input: s = "anagram", t = "nagaram"
Output: True

```

**Example 2:**
```

Input: s = "rat", t = "car"
Output: False

```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```

Input: s = "", t = ""
Output: True
Explanation: Two empty strings are trivially anagrams.

```

**Test Case 2:**
```

Input: s = "a", t = "aa"
Output: False
Explanation: Different character counts.

```

</details>

---

## 2. Approach

The solution uses a hash map (implemented as a `defaultdict(int)`) to count character frequencies in `s`. Then, it decrements counts based on characters in `t`. If after processing both strings any character count is not zero, the strings are not anagrams.

- Count frequencies of each character in `s`.
- Subtract frequencies based on characters in `t`.
- If any count is non-zero, return `False`.
- Otherwise, return `True`.

This approach efficiently compares the two strings using character counts without sorting.

---

## 3. Algorithm Complexity

- **Time Complexity:** O(n), where n is the length of the strings (both are assumed to be the same length for an anagram).
- **Space Complexity:** O(1), since the character set is fixed (e.g., ASCII alphabets), or O(k) where k is number of unique characters.

---