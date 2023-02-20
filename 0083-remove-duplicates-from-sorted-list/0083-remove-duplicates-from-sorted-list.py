# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1 = head
        while head1:
            cur = head1
            while cur and (cur.val == head1.val):
                cur = cur.next
            head1.next = cur
            head1 = head1.next
        return head