"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        path = []   
        def dfs(node):
            if not node: return 
            for child in node.children:
                dfs(child)
            path.append(node.val)
        dfs(root)
        return path