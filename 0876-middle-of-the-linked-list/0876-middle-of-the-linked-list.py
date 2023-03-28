# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = head
        count = 0
        while dummy:
            count += 1
            dummy = dummy.next
            
        for _ in range(count//2):
            head = head.next
            
        return head