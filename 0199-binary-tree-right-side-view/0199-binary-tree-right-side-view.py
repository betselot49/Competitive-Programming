# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_row = 0
        self.array = []
        
    def view(self, node, row):            
        if not node: return 

        if row > self.max_row:
            self.array.append(node.val)
            self.max_row = row

        self.view(node.right, row+1)
        self.view(node.left, row+1)
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.view(root, 1)
        return self.array
            