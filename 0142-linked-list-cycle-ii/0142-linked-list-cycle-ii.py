# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        index = 0
        meet = False
        while fast and fast.next:
            if fast == slow and index:
                meet = True
                break
            fast = fast.next.next
            slow = slow.next
            index += 1
        
        if meet:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return fast
        return None
        
        
        
        # cur = head
        # seen = set()
        # while cur:
        #     if cur in seen:
        #         return cur
        #     seen.add(cur)
        #     cur = cur.next
        # return None