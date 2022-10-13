class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
        

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1

        cur = self.head.next
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        cur = self.head.next
        self.head.next = Node(val)
        self.head.next.next = cur
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        if index < 0 or index > self.length:
            return
        
        cur = self.head
        for i in range(index):
            cur = cur.next
        newNode.next = cur.next
        cur.next = newNode
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        
        cur = self.head
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
