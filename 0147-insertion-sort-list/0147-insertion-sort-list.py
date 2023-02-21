# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        
        dummy 1 2 3 4 5 6 7 8 8 
                      |
                |
        
        remove 3
        start from dummy and find place for 3 (by next)
    `   
        """
        
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        
       
        finder = dummy.next
        
        while finder and finder.next:
            if finder.val <= finder.next.val:
                finder = finder.next
            else:
                holder = ListNode(finder.next.val)
                finder.next = finder.next.next

                placer = dummy
                while placer.next.val < holder.val:
                    placer = placer.next

                holder.next = placer.next
                placer.next = holder
            
        return head.next
        
