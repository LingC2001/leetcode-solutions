from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_copy = {}
        original_to_copy[None] = None

        res = None
        current = head
        while current != None:
            cpy_node = Node(current.val)
            original_to_copy[current] = cpy_node
            current = current.next
        
        current = head
        while current != None:
            res = original_to_copy[current]
            res.next = original_to_copy[current.next]
            res.random = original_to_copy[current.random]
            current=current.next

        return original_to_copy[head]
        


        








        