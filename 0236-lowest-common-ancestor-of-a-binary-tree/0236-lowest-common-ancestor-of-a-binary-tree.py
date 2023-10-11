# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: None}
        marked_common = defaultdict(bool)
        
        def find_node(num):
            queue = deque([root])
            while queue:
                node = queue.popleft()
          
                if node.val == num.val: return node
                if node.left:
                    parent[node.left] = node
                    queue.append(node.left)
                if node.right:
                    parent[node.right] = node
                    queue.append(node.right)
                    
        
        q_node = find_node(q)
        p_node = find_node(p)
        
        
        while q_node or p_node:
            if q_node:
                if marked_common[q_node]:
                    return q_node
                else:
                    marked_common[q_node] = True
                    q_node = parent[q_node]
                    
            if p_node:
                 if marked_common[p_node]:
                    return p_node
                 else:
                    marked_common[p_node] = True
                    p_node = parent[p_node]
                    
                    
                


            