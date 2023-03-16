# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.kth_smallest = 0
        
    def call(self, node, curr_rank, target):
        if not node: return curr_rank + 1

        rank = self.call(node.left, curr_rank, target)
        if rank == target:
            self.kth_smallest = node.val
        rank = self.call(node.right, rank, target)  
        return rank

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.call(root, 0, k)
        return self.kth_smallest
            