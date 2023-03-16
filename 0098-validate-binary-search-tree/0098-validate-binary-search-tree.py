# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.isValid = True
        self.last_visit = float("-inf")
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.validater(root)
        return self.isValid
        
    def validater(self, node):
        if not node: return
        
        self.validater(node.left)
        if self.last_visit >= node.val: 
            self.isValid = False
     
        if self.isValid:
            self.last_visit = node.val
            self.validater(node.right)
        
        return 
    
    
        
    
    
    
        