# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        -5001,  1  ,5,6,7,   2,   8,6,9,7,4,2,5,1
               temp     cur  
        
        while cur.next:
        
        find place for cur.next
        
        temp = head
        
        check if temp.next is less than cur.next
        
        for the first time check only once
        
        initiate i = 1
        
        if j == i:
            cur = cur.next
        if temp.next >= cur.next:
            newNode = ListNode(cur.next.val)
            newNode.next = temp.next
            temp.next = newNode
            cur.next = cur.next.next
        
        
        """
        
        
        cur = ListNode(-5001)
        cur.next = head
        head = cur
        i = 1
        cur = head.next
        while cur.next:
            temp = head
            j = 0
            while j < i and temp.next.val < cur.next.val:
                temp = temp.next
                j += 1
            if j == i:
                cur = cur.next
            elif temp.next.val >= cur.next.val:
                newNode = ListNode(cur.next.val)
                newNode.next = temp.next
                temp.next = newNode
                cur.next = cur.next.next
            i += 1
        return head.next
