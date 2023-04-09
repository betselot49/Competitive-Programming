# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,node):
        if not node:
            return -1
        return max(self.height(node.left),self.height(node.right))+1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        
        lh = self.height(root.left)
        rht = self.height(root.right)
        
        if abs(lh-rht)>=2:
            return False
        return left and right