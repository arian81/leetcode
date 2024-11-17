# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def dfs(root, left, mid, right):
            nonlocal res
            if not root:
                return False
            
            left = dfs(root.left, left, mid, right)
            mid = root.val == p.val or root.val == q.val
            right = dfs(root.right, left, mid, right)

            if left + mid + right >= 2:
                res = root
            
            return mid or left or right 
        
        dfs(root, False, False, False)
        return res
                
