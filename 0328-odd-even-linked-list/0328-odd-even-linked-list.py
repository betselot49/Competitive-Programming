# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:      
        if head and head.next:
            even = head
            odd = head.next
            
            while odd and odd.next:
                tempOdd = odd.next
                odd.next = odd.next.next

                tempEven = even.next
                even.next = tempOdd
                even = even.next
                even.next = tempEven

                odd = odd.next
        return head
        
        
        
        