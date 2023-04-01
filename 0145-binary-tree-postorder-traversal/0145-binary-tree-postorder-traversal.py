# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        self.array = []
        def postOrder(node):
            if not node: return
            postOrder(node.left)
            postOrder(node.right)
            self.array.append(node.val)
        postOrder(root)
        return self.array