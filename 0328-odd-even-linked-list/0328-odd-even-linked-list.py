# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
#         if head and head.next:
#             dummy = head
#             runner = head.next
            
#         while runner and runner.next:
#             tempR = runner.next
#             tempR.next = None
#             runner.next = runner.next.next
#             tempD = dummy.next
#             dummy.next= tempR
#             dummy = dummy.next
#             dummy.next = tempD

#             runner = runner.next
            
#         return head


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        oddHead = ListNode(0)
        evenHead = ListNode(0)
        odd = oddHead
        even = evenHead
        isOdd = True

        while head:
            if isOdd:
                odd.next = head
                odd = head
            else:
                even.next = head
                even = head
            head = head.next
            isOdd = not isOdd

        even.next = None
        odd.next = evenHead.next
        return oddHead.next

