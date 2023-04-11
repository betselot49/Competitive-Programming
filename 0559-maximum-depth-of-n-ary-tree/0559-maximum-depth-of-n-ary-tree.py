"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.counter = 0
        self.max_path = 0
        def dfs(node):
            if not node: return
            self.counter += 1
            self.max_path = max(self.max_path, self.counter)
            for child in node.children:
                dfs(child)
            self.counter -= 1
        dfs(root)
        return self.max_path