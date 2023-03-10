# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max = 0
        self.mode_dict = defaultdict(int)
        
    def mode(self, node):
        if not node: return 

        self.mode_dict[node.val] += 1
        self.max = max(self.max, self.mode_dict[node.val])

        self.mode(node.left)
        self.mode(node.right)
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.mode(root)
        ans = []
        for num in self.mode_dict:
            if self.mode_dict[num] == self.max:
                ans.append(num)
        return ans
            
            
            