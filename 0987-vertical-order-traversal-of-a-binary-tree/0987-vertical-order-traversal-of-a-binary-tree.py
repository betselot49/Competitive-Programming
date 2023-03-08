# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        index = defaultdict(list)
        queue.append([root, (0, 0)])
        
        while queue:
            for _ in range(len(queue)):
                inter = queue.popleft()
                
                if inter[0]:
                    index[inter[1][0]].append((inter[1][1], inter[0].val))
                    queue.append([inter[0].left, (inter[1][0]-1, inter[1][1]+1)])
                    queue.append([inter[0].right, (inter[1][0]+1, inter[1][1]+1)])
                    
        min_key = min(index.keys())
        answer = [0] * len(index)
        
        for key in index.keys():
            level = []
            for k in sorted(index[key]):
                level.append(k[1])
                
            answer[key - min_key] = level
            
        return answer
                    