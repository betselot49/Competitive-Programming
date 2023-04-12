# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        path = []
        def dfs(node):
            if not node:
                path.append(")")
                return 
                
            path.append(str(node.val))
            path.append("(")
            dfs(node.left)
            if node.right:
                path.append("(")
                dfs(node.right)
            else:
                if not node.left:
                    path.pop()
                    path.pop()
            path.append(")")
            
        dfs(root)
        path.pop()
        return "".join(path)
            
            
            