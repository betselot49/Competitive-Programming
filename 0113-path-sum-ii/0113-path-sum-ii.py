# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []
        def dfs(node, running_sum, path, target_sum):
            if node == None: return
            
            running_sum += node.val
            path.append(node.val)
            node.val = running_sum
            
            if node.left == None and node.right == None:
                if running_sum == target_sum:
                    output.append(path[:])
                    
            dfs(node.left, running_sum, path, target_sum)
            dfs(node.right, running_sum, path, target_sum)
            
            popped = path.pop()
            running_sum -= popped
        
        dfs(root, 0, [], targetSum)
        return output
            