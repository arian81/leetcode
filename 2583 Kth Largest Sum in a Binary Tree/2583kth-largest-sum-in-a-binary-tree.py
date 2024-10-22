# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = {}
        def dfs(root, level):
            if root:
                if level in res:
                    res[level] += root.val
                else:
                    res[level] = root.val
                
                dfs(root.left, level+1)
                dfs(root.right, level+1)
        dfs(root, 0)
        if (k > len(res)):
            return -1
        sorted_sums = sorted(res.values(), reverse=True)
        return sorted_sums[k-1]
        
        