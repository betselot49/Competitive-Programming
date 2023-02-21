# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        pre = head
        cur = head.next
        pre.next = None
        while cur:
            Next = cur.next
            cur.next = pre
            pre = cur
            cur = Next

        return pre
    
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        slow.next = self.reverse(slow.next)
        slow = slow.next
        maxSum = 0
        behind = head
        
        while slow:
            maxSum = max(slow.val + behind.val, maxSum)
            slow = slow.next
            behind = behind.next
        
        return maxSum