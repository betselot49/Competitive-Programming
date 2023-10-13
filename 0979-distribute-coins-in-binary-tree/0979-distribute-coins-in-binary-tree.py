# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.counter = 0
        def dfs(node):
            if not node: return 0
          
            req = node.val + dfs(node.left) + dfs(node.right) - 1
            
            self.counter += abs(req)
            return req
        
        dfs(root)
        return self.counter