# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self, root, head, val):
        if not root:
            root = TreeNode(val)
            return root
        elif val >= head.val:
            if head.right == None:
                head.right = TreeNode(val)
                return root
            else:
                return self.insert(root, head.right, val) 
        else:
            if head.left == None:
                head.left = TreeNode(val)
                return root
            else:
                return self.insert(root, head.left, val)
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = None
        for num in preorder:
            head = root
            root = self.insert(root, head, num)
        return root