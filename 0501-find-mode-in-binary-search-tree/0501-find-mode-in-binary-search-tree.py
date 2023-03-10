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

        # put the node.val and its count in the global dictionary and update the maximum count.
        self.mode_dict[node.val] += 1
        self.max = max(self.max, self.mode_dict[node.val])

        # do the same thing for both left and right nodes.
        self.mode(node.left)
        self.mode(node.right)
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.mode(root)
        ans = []
        # collect all numbers with only value equal to max_count into ans 
        for num in self.mode_dict:
            if self.mode_dict[num] == self.max:
                ans.append(num)
        return ans
            
            
            