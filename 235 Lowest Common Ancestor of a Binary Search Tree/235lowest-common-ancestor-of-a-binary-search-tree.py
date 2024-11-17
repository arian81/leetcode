# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ppath = []
        qpath = []
        pptr = root
        qptr = root

        while pptr:
            ppath.insert(0, pptr)
            
            if pptr.val == p.val:
                break
            elif pptr.val < p.val:
                pptr = pptr.right
            else:
                pptr = pptr.left

        while qptr:
            qpath.insert(0, qptr)
            
            if qptr.val == q.val:
                break
            elif qptr.val < q.val:
                qptr = qptr.right
            else:
                qptr = qptr.left
        set_qpath = set(qpath)

        for i in ppath:
            print(i)
            if i in set_qpath:
                return i

            
            
        