# LeetCode [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

---

## 1. Problem Description

### Description:
You are given an array of strings `tokens` that represents an arithmetic expression in Reverse Polish Notation (RPN). Evaluate the expression and return its value. Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression. Division between two integers should truncate toward zero.

---

### Input:
* `tokens`: List of string tokens, where each token is either:
  - An integer in string form (e.g., `"123"`, `"-45"`), or
  - One of the operators: `"+"`, `"-"`, `"*"`, `"/"`.

---

### Output:
* An integer representing the result of evaluating the RPN expression.

---

### Example(s):
**Example 1:**
```
Input: tokens = ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

**Example 2:**
```
Input: tokens = ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```
Input: tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
Step-by-step:
  9 3 +       → 12
  12 -11 *    → -132
  6 / -132    → 0      (truncate toward zero)
  10 * 0      → 0
  0 17 +      → 17
  17 5 +      → 22
```

**Test Case 2:**
```
Input: tokens = ["3", "-4", "+"]
Output: -1
Explanation: 3 + (-4) = -1
```

</details>

---

## 2. Approach

We use a stack to evaluate the RPN expression in one pass:

1. Initialize an empty stack.
2. Iterate through each token in `tokens`:
   - If the token is a number (not one of `+ - * /`), convert it to `int` and push it onto the stack.
   - Otherwise, it is an operator:
     a. Pop the top two numbers from the stack (`b` first, then `a`).
     b. Apply the operator to `a` and `b`:
        - `+`: push `a + b`
        - `-`: push `a - b`
        - `*`: push `a * b`
        - `/`: push `int(a / b)` to truncate toward zero
3. After processing all tokens, the stack contains a single element: the result.

This is optimal for RPN because each token is processed exactly once, and each operation is O(1).

---

## 3. Algorithm Complexity

- **Time Complexity:** O(n), where n is the number of tokens.  
- **Space Complexity:** O(n), for the stack in the worst case (all tokens are numbers).

---

## 4. Usage Instructions

Assuming the solution is defined in `solution.py`, you can run the following:

```python
from solution import evalRPN

tokens1 = ["2", "1", "+", "3", "*"]
print(evalRPN(tokens1))  # Output: 9

tokens2 = ["4", "13", "5", "/", "+"]
print(evalRPN(tokens2))  # Output: 6
```

Ensure you have Python 3.x installed. Save your code in `solution.py` and execute:

```
python solution.py
```