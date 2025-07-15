# LeetCode [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

---

## 1. Problem Description

### Description:
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid. An input string is valid if:

- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Every closing bracket has a corresponding open bracket of the same type.

---

### Input:
A single string `s` consisting of the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`.

---

### Output:
Return `true` if the string is valid; otherwise, return `false`.

---

### Example(s):
**Example 1:**
```
Input: s = "()"
Output: true
```

**Example 2:**
```
Input: s = "()[]{}"
Output: true
```

**Example 3:**
```
Input: s = "(]"
Output: false
```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```
Input: s = ""
Output: true
Explanation: An empty string is considered valid.
```

**Test Case 2:**
```
Input: s = "([{}])"
Output: true
Explanation: Properly nested pairs.
```

**Test Case 3:**
```
Input: s = "([)]"
Output: false
Explanation: Closing brackets are out of order.
```

</details>

---

## 2. Approach

We employ a **Stack** to track opening brackets and verify matches with closing brackets:

1. Define a mapping `pairs` for closing→opening:
   ```python
   pairs = {')': '(', ']': '[', '}': '{'}
   ```
2. Initialize an empty stack `stack = []`.
3. Iterate over each character `c` in `s`:
   - If `c` is not in `pairs` (i.e., it's an opening bracket), push it onto `stack`.
   - Else (`c` is a closing bracket):
     - Check if `stack` is non-empty and `stack[-1] == pairs[c]`.  
       - If yes, pop the stack.
       - Otherwise, return `False` immediately (mismatch or no opening bracket).
4. After processing all characters, return `True` if `stack` is empty (all brackets matched); otherwise, `False`.

Why this works:
- The stack’s LIFO order ensures the most recent opening bracket is closed first.
- Immediate failure on mismatch or missing opening bracket.

Alternative approaches:
- Recursive parsing can also validate pairs but is less direct and uses call-stack.
- Repeated string replacement of valid pairs is O(n²), so suboptimal.

---

## 3. Algorithm Complexity

- Time Complexity: O(n), where n = len(s). Each character is pushed or popped at most once.
- Space Complexity: O(n) in the worst case, for the stack holding all opening brackets.

---

## 4. Usage Instructions

1. Save the solution code below into a file named `solution.py`:
   ```python
   def isValid(s: str) -> bool:
       pairs = {')': '(', ']': '[', '}': '{'}
       stack = []
       for char in s:
           if char not in pairs:
               stack.append(char)
           elif stack and stack[-1] == pairs[char]:
               stack.pop()
           else:
               return False
       return not stack
   ```
2. Ensure you have Python 3 installed.
3. To run standalone tests, you can add at the bottom of `solution.py`:
   ```python
   if __name__ == "__main__":
       test_cases = ["()", "()[]{}", "(]", "([{}])", "([)]", ""]
       for s in test_cases:
           print(f"isValid({s!r}) -> {isValid(s)}")
   ```
4. Execute in your terminal:
   ```
   python solution.py
   ```
5. Or import and use the function in another module:
   ```python
   from solution import isValid
   print(isValid("{[]}"))  # True
   ```

Enjoy validating parentheses with O(n) efficiency!