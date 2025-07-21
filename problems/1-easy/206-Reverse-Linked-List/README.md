# LeetCode [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

---

## 1. Problem Description

### Description:
Given the head of a singly linked list, reverse the list and return the reversed list.

---

### Input:
- `head`: The head node of a singly linked list, where each node has an integer value `val` and a pointer `next`.

---

### Output:
- The head node of the reversed linked list.

---

### Example(s):
**Example 1:**
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2:**
```
Input: head = [1,2]
Output: [2,1]
```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```
Input: head = []
Output: []
Explanation: An empty list remains empty after reversal.
```

**Test Case 2:**
```
Input: head = [1]
Output: [1]
Explanation: A single-node list is the same when reversed.
```

</details>

---

## 2. Approach

We use an **in-place iterative reversal** with the Two Pointers pattern:

1. Initialize two pointers:
   - `prev = None`
   - `current = head`
2. Iterate until `current` becomes `None`:
   - Save `next_node = current.next`
   - Reverse the link: `current.next = prev`
   - Move `prev` forward: `prev = current`
   - Move `current` forward: `current = next_node`
3. At the end, `prev` points to the new head of the reversed list. Return `prev`.

Key points:
- We only change the `next` pointers; no new nodes are created.
- This uses constant extra space.
- Alternative approach: recursive reversal, but it uses O(n) call stack.

---

## 3. Algorithm Complexity

- **Time Complexity:** O(n), where n is the number of nodes. Each node is visited exactly once.
- **Space Complexity:** O(1), since we only use a fixed number of pointers.

---

## Solution Code

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev
```