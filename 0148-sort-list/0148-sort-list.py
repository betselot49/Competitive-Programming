# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, node1, node2):
        merged = ListNode()
        dummy = merged
        while node1 and node2:
            if node1.val <= node2.val:
                dummy.next = ListNode(node1.val)
                node1 = node1.next
            else:
                dummy.next = ListNode(node2.val)
                node2 = node2.next
            dummy = dummy.next
            
        dummy.next = node1 if node1 else node2
        return merged.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head) or not(head.next):
            return head
        
        slow = fast = head
        left = dummy = ListNode()
        while fast and fast.next and fast.next.next:
            dummy.next = ListNode(slow.val)
            dummy = dummy.next
            slow = slow.next
            fast = fast.next.next
            
        dummy.next = ListNode(slow.val) if slow else None
        right = slow.next if slow else None
        
        left = self.sortList(left.next)
        right = self.sortList(right)
        
        return self.merge(left, right)
        
        
        