# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not list or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                ListNode1 = lists[i]
                ListNode2 = lists[i+1] if i+1 < len(lists) else None
                mergedList.append(self.mergeList(ListNode1, ListNode2))
            lists = mergedList
        return lists[0]
        
        
    def mergeList(self, ListNode1, ListNode2):
        dummy = ListNode(0)
        cur = dummy

        while ListNode1 or ListNode2:
            val1 = ListNode1.val if ListNode1 else 10_001
            val2 = ListNode2.val if ListNode2 else 10_001
            if val1 < val2:
                cur.next = ListNode(val1)
                ListNode1 = ListNode1.next
            else:
                cur.next = ListNode(val2)
                ListNode2 = ListNode2.next
            cur = cur.next
        return dummy.next
      
      
