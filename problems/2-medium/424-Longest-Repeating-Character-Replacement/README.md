# LeetCode [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

---

## 1. Problem Description

### Description:

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operation.

---

### Input:

* `s`: A string consisting of only uppercase English letters.
* `k`: An integer representing the maximum number of character replacements allowed.

---

### Output:

* An integer representing the length of the longest valid substring after at most `k` replacements.

---

### Example(s):

**Example 1:**

```
Input: s = "ABAB", k = 2
Output: 4
```

**Example 2:**

```
Input: s = "AABABBA", k = 1
Output: 4
```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**

```
Input: s = "AAAA", k = 2
Output: 4
Explanation: All characters are already the same.
```

**Test Case 2:**

```
Input: s = "ABBB", k = 2
Output: 4
Explanation: Replace 'A' with 'B' to get "BBBB".
```

</details>

---

## 2. Approach

The solution uses a **Sliding Window Strategy**:

* Use a window defined by `left` and `right` pointers to scan the string.
* Maintain a frequency map of characters within the current window.
* Track the count of the most frequent character in the window.
* If the number of characters to replace (window size - max frequency) exceeds `k`, shrink the window from the left.
    *   The max frequency determines the length of the window.
    *    We do not update max frequency if the new max is lower because we dont need to check windows that are smaller than the max length we have currently found.
* The maximum window size seen during this process is the result.

This approach ensures the substring always requires at most `k` replacements to be uniform.

---

## 3. Algorithm Complexity

* **Time Complexity:** O(n), where n is the length of the string. Each character is processed at most twice.
* **Space Complexity:** O(1), since the character set is limited to 26 uppercase English letters.

---
