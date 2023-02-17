# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = ListNode(0)
        node.next = head
        leader = node
        follower = node
        for i in range(n + 1):
            leader = leader.next
            i += 1
        while leader:
            leader = leader.next
            follower = follower.next
            
        follower.next = follower.next.next
        return node.next