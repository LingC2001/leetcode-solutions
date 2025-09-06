from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.dfs(root)
        return root

    def dfs(self, current):
        if current.left:
            self.dfs(current.left)

        if current.right:
            self.dfs(current.right)

        current.left, current.right = current.right, current.left
