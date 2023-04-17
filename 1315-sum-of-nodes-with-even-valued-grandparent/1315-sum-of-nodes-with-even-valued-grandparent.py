# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum = 0
        def dfs(node, parent, grandparent):
            if not node: return 
            if grandparent % 2 == 0:
                self.sum += node.val
            dfs(node.left, node.val, parent)
            dfs(node.right, node.val, parent)
        dfs(root, 1, 1)
        return self.sum
        
        
        
        #  < --------------  Bruteforce   ---------------- >   
        
    
        # def dfs(node):
        #     if not node: return 
        #     if node.val % 2 == 0:
        #         if node.left and node.left.left:
        #             self.sum += node.left.left.val
        #         if node.left and node.left.right:
        #             self.sum += node.left.right.val
        #         if node.right and node.right.left:
        #             self.sum += node.right.left.val
        #         if node.right and node.right.right:
        #             self.sum += node.right.right.val
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # return self.sum