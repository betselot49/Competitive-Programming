# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        index = 0
        while fast and fast.next:
            if fast == slow and index:
                return True
            slow = slow.next
            fast = fast.next.next
            index += 1
            
        return False