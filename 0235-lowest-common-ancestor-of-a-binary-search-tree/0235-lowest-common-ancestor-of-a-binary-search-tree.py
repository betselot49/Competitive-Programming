# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def LCA(self, node, p, q):
        if p.val <= node.val <= q.val or q.val <= node.val <= p.val:
            return node
        
        if node.val > q.val and node.val > p.val:
            return self.LCA(node.left, p, q)
        else:
            return self.LCA(node.right, p, q)
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.LCA(root, p, q)