# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(-1)
        merged = head


        while list1 and list2:
            if  list1.val < list2.val: #list 1 is smaller
                merged.next = list1
                list1 = list1.next
            else : # list2 is smaller
                merged.next = list2
                list2 = list2.next
            merged = merged.next
        
        if list1:
            merged.next = list1
        else:
            merged.next = list2
        
        return head.next
        
                
            