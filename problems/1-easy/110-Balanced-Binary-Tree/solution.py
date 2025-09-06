from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isbalanced = True
        self.dfs(root)
        return self.isbalanced

    def dfs(self, root):
        if not root:
            return 0

        left_height = self.dfs(root.left)

        right_height = self.dfs(root.right)

        if abs(left_height - right_height) > 1:
            self.isbalanced = False

        return max(left_height, right_height) + 1
