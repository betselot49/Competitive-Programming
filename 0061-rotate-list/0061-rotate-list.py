# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        dummy = head
        while dummy:     # find nodes length
            length += 1
            dummy = dummy.next
            
        k = k % length if length else k
        
        if k == 0 or length == 0:
            return head
        
        fast = slow = head
        for _ in range(k):
            fast = fast.next
            
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            
        newHead = slow.next
        slow.next = None
        
        tempHead = newHead
        while tempHead and tempHead.next:
            tempHead = tempHead.next
            
        tempHead.next = head
        return newHead

        
        
      
        
        
        