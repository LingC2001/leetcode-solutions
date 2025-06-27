# LeetCode [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)

---

## 1. Problem Description

### Description:
Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

---

### Input:
- `s`: A string containing letters, digits, spaces, and special characters.

---

### Output:
- A boolean value `True` if the cleaned string is a palindrome, otherwise `False`.

---

### Example(s):
**Example 1:**
```

Input: s = "A man, a plan, a canal: Panama"
Output: True

```

**Example 2:**
```

Input: s = "race a car"
Output: False

```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```

Input: s = " "
Output: True
Explanation: An empty string or a string with only non-alphanumeric characters is considered a palindrome.

```

**Test Case 2:**
```

Input: s = "0P"
Output: False
Explanation: After cleaning, the string is "0p" which is not a palindrome.

```

</details>

---

## 2. Approach

The approach first preprocesses the input string by converting it to lowercase and filtering out all non-alphanumeric characters, creating a sanitized string `stripped_str`. Then, two pointers `forward_index` and `backward_index` are used to compare characters from the start and end of the string moving inward.

- If characters at both pointers match, pointers move closer to the center.
- If a mismatch is found, return `False` immediately.
- If pointers cross without mismatches, return `True`.

This method efficiently checks palindrome property by ignoring case and non-alphanumeric characters.

---

## 3. Algorithm Complexity

- **Time Complexity:** O(n), where n is the length of the input string `s`. The string is processed twice (filtering and checking), both linear operations.
- **Space Complexity:** O(n), due to the creation of the filtered string.

---