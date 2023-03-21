# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.seen = defaultdict(int)
        self.seen[0] += 1
        self.sum_count = 0
        def recursion(node, pre_sum, targetSum):
            if not node: return 
            pre_sum += node.val
            self.sum_count += self.seen[pre_sum - targetSum]
            self.seen[pre_sum] += 1
            recursion(node.left, pre_sum, targetSum)
            recursion(node.right, pre_sum, targetSum)
            self.seen[pre_sum] -= 1
            
        recursion(root, 0, targetSum)
        return self.sum_count