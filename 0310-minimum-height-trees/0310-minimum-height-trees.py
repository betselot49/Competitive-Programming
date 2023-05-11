class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = defaultdict(int)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            degree[node1] += 1
            degree[node2] += 1
            
        queue = deque([])
        queue_set = set()
        
        for i in range(n):
            if degree[i] == 1:
                queue.append((i, 0))
                queue_set.add(i)
    
        while queue:
            node, level = queue.popleft()
            print(node, level)
            queue_set.remove(node)
            degree[node] -= 1
            for neighbour in graph[node]:
                degree[neighbour] -= 1
                if neighbour in queue_set:
                    core_node, core_level = queue.popleft()
                    if core_level == level: return [core_node, node]
                    return [core_node]
        
                if degree[neighbour] == 1:
                    queue.append((neighbour, level + 1))
                    queue_set.add(neighbour)
        return [0]