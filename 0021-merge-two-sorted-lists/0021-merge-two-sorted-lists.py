# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merger(self, merged, node1, node2):
        # Merge using recursion.
        if node1 == None or node2 == None:
            merged.next = node1 if node1 else node2
            return 
        
        if node1.val < node2.val:
            merged.next = ListNode(node1.val)
            node1 = node1.next
        else:
            merged.next = ListNode(node2.val)
            node2 = node2.next
        merged = merged.next
        
        self.merger(merged, node1, node2)
            
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode(0)
        merged = newNode
        
        self.merger(merged, list1, list2)
        return newNode.next
    
    
    """
    # Using iteration
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
    """
