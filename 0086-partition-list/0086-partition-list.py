# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        runner = ListNode(0)
        runner.next = head  
        head = runner
        while runner.next and runner.next.val < x:  # run util you reach a node that its next node has less value than x.
            runner = runner.next
            
        collector = runner
        while collector.next:
            if collector.next.val < x:
                temp1 = collector.next      #  Going to be the next of runner
                collector.next = collector.next.next   
                temp2 = runner.next         # Going to be the next of next of runner
                runner.next = temp1
                runner = runner.next
                runner.next = temp2
            else:
                collector = collector.next   
                
                
        return head.next
        
