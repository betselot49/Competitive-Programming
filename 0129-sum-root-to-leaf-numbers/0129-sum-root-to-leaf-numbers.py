# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.curr = 0
        def pathFinder(node):
            if not node: return 
            if not node.left and not node.right:
                self.curr = self.curr * 10 + node.val
                self.total += self.curr
                self.curr //= 10
                return
            
            self.curr = self.curr * 10 + node.val
            pathFinder(node.left)
            pathFinder(node.right)
            self.curr //= 10 
            
            
        pathFinder(root)
        return self.total
    