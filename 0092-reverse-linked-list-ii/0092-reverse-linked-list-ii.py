# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseNode(self, node, length):  # function takes node and length of nodes to be reversed.
        pre = node
        cur = node.next 
        pre.next = None
        for _ in range(length):  # reverse only the first {length} nodes.
            Next = cur.next
            cur.next = pre
            pre = cur
            cur = Next
        temp = pre
        while temp.next:   # the unreversed nodes will be appended on the end of reversed nodes.
            temp = temp.next
        temp.next = cur
        return pre
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]: 
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        for _ in range(left-1):
            dummy = dummy.next
            
        dummy.next = self.reverseNode(dummy.next, right - left)  # the next (right - left) nodes will be reversed.
        return head.next
            
        
            