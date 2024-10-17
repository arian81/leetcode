class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < self.size:
            curr = self.head
            counter = 0
            while curr:
                if counter == index:
                    return curr.val
                counter += 1
                curr = curr.next
        return -1

    def addAtHead(self, val: int) -> None:
        if self.size == 0:
            self.head.val = val
        else:
            new_node = ListNode(val)
            new_node.next = self.head
            self.head = new_node
        
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
           self.head.val = val 
        else:
            new_node = ListNode(val)
            curr = self.head
            while curr.next:
                curr = curr.next
            
            curr.next = new_node
        
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:

        if index == 0:
            self.addAtHead(val)
        elif index == self.size or index == -1:
            self.addAtTail(val)
        else:
            new_node = ListNode(val)
            curr = self.head
            counter = 0
            while counter < self.size:
                if counter == index - 1:
                    old_curr_next = curr.next
                    curr.next = new_node
                    new_node.next = old_curr_next
                    self.size += 1
                    break
                curr = curr.next
                counter += 1
        

    def deleteAtIndex(self, index: int) -> None:
        
        if index < 0 or index >= self.size:
            return
            
        if index == 0:
            self.head = self.head.next
            self.size -= 1
        
        else:
            curr = self.head
            counter = 0
            while curr:
                if counter == index - 1:
                    if curr.next.next:
                        next_next = curr.next.next
                        curr.next = next_next
                    else:
                        curr.next = None
                    self.size -= 1
                curr = curr.next
                counter +=1

    def prettyPrint(self) -> None:
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(5)
obj.addAtHead(3)
obj.addAtTail(10000000)
obj.addAtIndex(-1, 1234)
obj.prettyPrint()
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)