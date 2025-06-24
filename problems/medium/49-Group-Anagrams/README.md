
---

# LeetCode [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)

---

## 1. Problem Description

### Description:

Given a list of strings, group them into lists where each group contains strings that are anagrams of each other.

---

### Input:

* A list of strings `strs`

---

### Output:

* A list of lists of strings, where each inner list contains anagrams.

---

### Example(s):

**Example 1:**

```
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
```

**Example 2:**

```
Input: [""]
Output: [[""]]
```

---

## 2. Approach

* Iterate over each string.
* For each string, build a character frequency list of size 26.
* Convert this list into a tuple and use it as a dictionary key.
* Append the string to the list corresponding to that key.
* Finally, return all the lists of anagrams.

This approach uses a dictionary to group anagrams in one pass.

---

## 3. Algorithm Complexity

* **Time Complexity:** O(n \* k), where n is the number of strings and k is the average string length.
* **Space Complexity:** O(n \* k) for storing the output and keys.

---

