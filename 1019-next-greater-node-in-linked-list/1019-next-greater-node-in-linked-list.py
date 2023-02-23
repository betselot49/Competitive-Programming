# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        i = 0
        output = []
        stack = []
        
        while head:
            output.append(0)
            while stack and stack[-1][0] < head.val:
                cur = stack.pop()
                output[cur[1]] = head.val
            stack.append([head.val, i])
            head = head.next
            i += 1
            
        return output
