

---

# LeetCode [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)

---

## 1. Problem Description

### Description:

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

---

### Input:

* A string `s`

---

### Output:

* A boolean `True` if `s` is a valid palindrome, `False` otherwise.

---

### Example(s):

**Example 1:**

```
Input: "A man, a plan, a canal: Panama"
Output: True
```

**Example 2:**

```
Input: "race a car"
Output: False
```

---

## 2. Approach

* Convert the string to lowercase and filter out non-alphanumeric characters.
* Use two pointers: one from the start, one from the end.
* Compare characters at each pointer, moving inward.
* If any mismatch is found, return `False`.
* If all characters match, return `True`.

This approach checks for palindrome properties efficiently while ignoring irrelevant characters.

---

## 3. Algorithm Complexity

* **Time Complexity:** O(n), where n is the length of the input string.
* **Space Complexity:** O(n), for the cleaned string.

---
