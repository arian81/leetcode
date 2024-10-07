# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        prev = None
        ans = ListNode()
        res = ans
        while l1 is not None and l2 is not None:
            res.val += l1.val + l2.val
            rem = ListNode(res.val // 10)
            res.val %= 10
            res.next = rem

            prev = res
            res = res.next
            l1 = l1.next
            l2 = l2.next
        
        if l1 is None:
            l1, l2 = l2, l1
        
        while l1 is not None:
            res.val += l1.val
            rem = ListNode(res.val // 10)
            res.val %= 10
            res.next = rem

            prev = res
            res = res.next
            l1 = l1.next
        
        while res.val != 0:
            rem = ListNode(res.val // 10)
            res.val %= 10
            res.next = rem

            prev = res
            res = res.next

        if prev.next.val == 0:
            prev.next = None

        return ans
        