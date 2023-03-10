# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0

    def average(self, node):
        if not node: return (0, 0)

        # add current, left and right
        curr_val = node.val
        left_sum, left_count = self.average(node.left)
        right_sum, right_count = self.average(node.right)

        curr_sum = curr_val + left_sum + right_sum
        curr_count = 1 + left_count + right_count

        # validate the condition which is curr == average
        if curr_sum // curr_count == curr_val:
            self.count += 1
            
        # return total sum and number of nodes below the current node including itself to the caller.
        return (curr_sum, curr_count)
        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.average(root)
        return self.count