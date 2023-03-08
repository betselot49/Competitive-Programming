# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def same(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        
        if node1 and node2 == None or node2 and node1 == None:
            return False
        
        node = node1.val == node2.val
        leftNode = self.same(node1.left, node2.left)
        rightNode = self.same(node1.right, node2.right)
        
        return all([node, leftNode, rightNode])
    
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.same(p, q)