# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.paths = []
        
        
    def binary(self, node, array):
        if not node: return 
        
        array.append(str(node.val))
        if not node.left and not node.right:
            self.paths.append("->".join(array))
        self.binary(node.left, array)
        self.binary(node.right, array)
        array.pop()
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.binary(root, [])
        return self.paths