# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:    
    def merger(self, node1, node2):
        if node1 == None or node2 == None:
            return node1 if node1 else node2
        
        
        merged = TreeNode(node1.val + node2.val)
        merged.left = self.merger(node1.left, node2.left)
        merged.right = self.merger(node1.right, node2.right)
        
        return merged
    
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.merger(root1, root2)