# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        counter = k
        res = None

        def dfs(root):
            nonlocal counter, res
            if not root:
                return
            
            dfs(root.left)
            counter -= 1
            if counter == 0:
                print(root.val)
                res = root.val
            dfs(root.right)
        dfs(root)
        
        return res