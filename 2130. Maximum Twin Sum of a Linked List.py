# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        stack = []
        while fast:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            
        maxSum = 0
        curSum = 0
        while slow:
            curSum = stack.pop() + slow.val
            maxSum = max(maxSum, curSum)
            slow = slow.next
        return maxSum
