# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.collector = []
    
    def search(self, node, target):
        if not node.left: return False

        queue = deque([node])
        while queue:
            parent = queue.popleft()
            if parent == None: continue

            if parent.left and parent.left.val == target:
                left = TreeNode()
                right = TreeNode()
                left.left = parent.left.left
                right.left = parent.left.right
                self.collector.append(left)
                self.collector.append(right)
                parent.left = None
                return True

            elif parent.right and parent.right.val == target:
                left = TreeNode()
                right = TreeNode()
                left.left = parent.right.left
                right.left = parent.right.right
                self.collector.append(left) 
                self.collector.append(right)
                parent.right = None
                return True

            queue.append(parent.left)
            queue.append(parent.right)

        return False
    
    
    def delNodes(self, root, to_delete):
        starter = TreeNode()
        starter.left = root
        self.collector = [starter]
        
        for target in to_delete:
            for node in self.collector:
                if self.search(node, target): break
                    
        answer = []
        for node in self.collector:
            if not node.left: continue
            answer.append(node.left)
            
        return answer

        
        
                    
                
                    
                