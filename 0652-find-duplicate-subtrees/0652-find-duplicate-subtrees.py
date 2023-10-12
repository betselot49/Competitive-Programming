# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        common = defaultdict(int)
        duplicate = []
        
        def dfs(node, pos):
            if not node: return pos
        
            left = dfs(node.left, "*")
            right = dfs(node.right, "#")
            
            represent = left + "|" + str(node.val) + "|" + right
            
            common[represent] += 1
            if common[represent] == 2:
                duplicate.append(node)
            
            return represent
        
        dfs(root, "")
        return duplicate