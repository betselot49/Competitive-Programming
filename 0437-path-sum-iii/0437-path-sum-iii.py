# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        seen = defaultdict(int)
        seen[0] += 1
        sum_count = 0
        def recursion(node, pre_sum, targetSum):
            nonlocal sum_count
            if not node: return 
            pre_sum += node.val
            sum_count += seen[pre_sum - targetSum]
            seen[pre_sum] += 1
            recursion(node.left, pre_sum, targetSum)
            recursion(node.right, pre_sum, targetSum)
            seen[pre_sum] -= 1
            
        recursion(root, 0, targetSum)
        return sum_count