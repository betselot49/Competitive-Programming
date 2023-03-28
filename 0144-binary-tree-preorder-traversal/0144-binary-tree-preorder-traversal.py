# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        self.array = []
        def traversal(node):
            if not node: return
            
            self.array.append(node.val)
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        return self.array