# LeetCode [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)

---

## 1. Problem Description

### Description:
Given an array of strings `strs`, group the anagrams together. Anagrams are strings that contain the same characters in any order.

---

### Input:
- `strs`: A list of lowercase strings.

---

### Output:
- A list of lists, where each sublist contains strings that are anagrams of each other.

---

### Example(s):
**Example 1:**
```

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

```

**Example 2:**
```

Input: strs = [""]
Output: [[""]]

```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```

Input: strs = ["abc","bca","cab","xyz","zyx","yxz"]
Output: [["abc","bca","cab"],["xyz","zyx","yxz"]]
Explanation: Strings grouped by identical character counts.

```

**Test Case 2:**
```

Input: strs = ["a"]
Output: [["a"]]
Explanation: Single string forms one group.

```

</details>

---

## 2. Approach

To group anagrams efficiently, the algorithm relies on the fact that anagrams share the same frequency of each character.

Instead of sorting each string (which can be costly), this solution creates a fixed-size character count signature for each string, representing how many times each letter appears.

- For each string, build an array representing counts of each alphabet letter.
- Convert this count array into a tuple (hashable) to serve as a unique key.
- Use a dictionary to map each unique signature to a list of strings matching that pattern.
- Append each string to the correct group based on its signature.
- Finally, return all grouped anagram lists.

This approach avoids the overhead of sorting strings and leverages constant-time dictionary lookups for grouping, resulting in an efficient solution.

---

## 3. Algorithm Complexity

- **Time Complexity:** O(n * k), where n is the number of strings and k is the maximum string length. Counting characters is O(k) per string.
- **Space Complexity:** O(n * k), to store the grouped anagrams and the frequency signatures.

---