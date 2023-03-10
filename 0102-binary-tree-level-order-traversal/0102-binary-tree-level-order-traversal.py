# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.row_dict = defaultdict(list)
        
    def readByLevel(self, node, row):
        if not node: return 
        
        # put every value in dictionary using row as a key
        self.row_dict[row].append(node.val)
        self.readByLevel(node.left, row+1)
        self.readByLevel(node.right, row+1)
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.readByLevel(root, 1)
        levels = sorted([[row, level] for row, level in self.row_dict.items()])
        return [level[1] for level in levels]
        