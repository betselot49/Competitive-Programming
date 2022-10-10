class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        leader = head
        follower = head
        while leader and leader.next:
            leader = leader.next.next
            follower = follower.next
        return follower
