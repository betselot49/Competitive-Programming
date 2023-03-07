# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reader(self, root, array):
        if root == None:
            return array
    
        left_array = self.reader(root.left, array)
        left_array.append(root.val)
        right_array = self.reader(root.right, left_array)
        
        return right_array
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.reader(root, [])