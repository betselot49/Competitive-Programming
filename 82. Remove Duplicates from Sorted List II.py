# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode(-101)
        cur.next = head
        head = cur
        while cur.next:
            temp = cur
            count = 0
            while temp.next and temp.next.val == cur.next.val:
                count += 1
                temp = temp.next
            if count > 1:
                cur.next = temp.next
            else:
                cur.next = temp
                cur = cur.next
                
        return head.next
