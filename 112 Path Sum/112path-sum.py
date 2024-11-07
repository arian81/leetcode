# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def sol(root, target, sum):
            if not root:
                return False
            print("current root val: ", root.val, "current sum: ", sum)
            if not root.left and not root.right:
                return root.val + sum == target
            if sol(root.left, target, sum + root.val):
                return True
            if sol(root.right, target, sum + root.val):
                return True
            return False
        
        return sol(root, targetSum, 0)