# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #[1,2,3]
        if head and head.next != None:
            prev_node = head #1
            curr_node = head.next #2
            prev_node.next = None
            while curr_node.next != None:
                next_node = curr_node.next #3
                curr_node.next = prev_node # 2 points to 1
                prev_node = curr_node # 1 becomes 2
                curr_node = next_node # current node becomes 3
            curr_node.next = prev_node
            return curr_node
        else:
            return head
