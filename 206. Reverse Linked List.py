# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverseNode = ListNode()
        if not head:
            return reverseNode.next
        reverseNode.val = head.val
        head = head.next
        while head:
            cur = ListNode(head.val)
            cur.next = reverseNode
            reverseNode = cur
            head = head.next
        return reverseNode
        
