# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        leader = head
        follower = head
        stack = []

        while leader and leader.next:
            leader = leader.next.next
            stack.append(follower.val)
            follower = follower.next
        if leader:
            follower = follower.next
            
        while stack and follower:
            if follower.val == stack[-1]:
                follower = follower.next
                stack.pop()
            else:
                return False

        if stack or follower:
            return False
        else:
            return True
