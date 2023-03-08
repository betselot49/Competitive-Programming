# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def symetry(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        if (node1 and node2 == None) or (node2 and node1 == None):
            return False
        
        node = node1.val == node2.val
        leftNode = self.symetry(node1.left, node2.right)
        rightNode = self.symetry(node1.right, node2.left)
        
        return all([node, leftNode, rightNode])
    
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root:
            root1 = TreeNode(root.val)
            root2 = TreeNode(root.val)
            root1.left = root.left
            root1.right = None
            root2.left = None
            root2.right = root.right
        else:
            root1 = None
            root2 = None
   
        return self.symetry(root1, root2)