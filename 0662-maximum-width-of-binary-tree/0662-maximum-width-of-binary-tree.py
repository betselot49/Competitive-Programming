# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        row_dict = defaultdict(list)
        def maxWidth(node, row, col):
            if not node: return
            
            # putting col in dictionary using row as a key.
            if row_dict[row] and row_dict[row][1] < col:
                row_dict[row][1] = col
            else:
                row_dict[row] = [col, col]
                
            # do the same thing for left and right nodes.
            maxWidth(node.left, row+1, (col*2)-1)
            maxWidth(node.right, row+1, col*2)
        
        maxWidth(root, 1, 1)  # one indexed column.
        
        width = 0
        for start, end in row_dict.values():
            width = max(width, end - start + 1)
        return width