# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = ListNode(0)
        head = total
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            curSum = val1 + val2 + carry
            total.next = ListNode(curSum % 10)
            carry = curSum // 10
            
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            total = total.next
            
        if carry:
            total.next = ListNode(carry)
        return head.next
            
            