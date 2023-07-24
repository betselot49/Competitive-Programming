# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def dfs(node, dirt):
            if not node: return
            
            if dirt == "LEFT" and (not node.left and not node.right):
                self.sum += node.val
                
            dfs(node.left, "LEFT")
            dfs(node.right, "RIGHT")
            
        dfs(root, "ROOT")
        return self.sum
            