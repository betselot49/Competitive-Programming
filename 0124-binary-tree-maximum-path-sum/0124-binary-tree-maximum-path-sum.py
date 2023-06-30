# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = -float("inf")
        def dfs(node):
            if not node: return -float("inf")
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.maxPath = max(self.maxPath, node.val, node.val + left, node.val + right, node.val + right + left)
            node.val = max(node.val, node.val + left, node.val + right)
        
            return node.val
        
        dfs(root)
        return self.maxPath