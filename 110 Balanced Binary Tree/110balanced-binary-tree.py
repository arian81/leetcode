# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root):
        if not root:
            return 0
        
        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)

        return 1 + max(leftDepth, rightDepth)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        balanced  = abs(self.depth(root.left) - self.depth(root.right)) <= 1

        return balanced and self.isBalanced(root.left) and self.isBalanced(root.right)
    