# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        cur = merged
        while list1 or list2:
            val1 = list1.val if list1 else 101
            val2 = list2.val if list2 else 101
            cur.next = ListNode(min(val1, val2))
            if val1 > val2:
                list2 = list2.next
            else:
                list1 = list1.next
            cur = cur.next
        
        return merged.next
