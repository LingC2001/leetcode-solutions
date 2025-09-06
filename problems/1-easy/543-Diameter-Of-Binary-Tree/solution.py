from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        
        self.maxDiameter(root)

        return self.res
        
    def maxDiameter(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDiameter(root.left)

        right_depth = self.maxDiameter(root.right)

        self.res = max(left_depth + right_depth, self.res)

        return max(left_depth,right_depth) + 1