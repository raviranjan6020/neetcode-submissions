# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left=self.helper(root.left)
        right=self.helper(root.right)
        if abs(right-left)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def helper(self, root):
        if root is None:
            return 0
        return 1+max(self.helper(root.left), self.helper(root.right))
        