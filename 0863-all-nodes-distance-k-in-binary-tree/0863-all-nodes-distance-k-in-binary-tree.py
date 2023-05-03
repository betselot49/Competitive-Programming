# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def buildGraph(parent, node):
            if not node: return 
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
                
            buildGraph(node, node.left)
            buildGraph(node, node.right)
            
        buildGraph(None, root)
        k_closest = []
        queue = deque([(target.val, 0)])
        visited = set()
        while queue:
            num, level = queue.popleft()
            if num in visited: continue
            visited.add(num)
            if level == k:
                k_closest.append(num)
            if level > k: return k_closest

            for neighbour in graph[num]:
                if neighbour not in visited:
                    queue.append((neighbour, level+1))
        
        return k_closest
                