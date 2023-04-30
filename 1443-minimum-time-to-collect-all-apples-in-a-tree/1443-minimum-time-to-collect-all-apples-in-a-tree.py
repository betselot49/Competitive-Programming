class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        visited = set()
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        def collectApples(node):
            if node in visited: return 0
            visited.add(node)
            
            deep_size = 0
            for neighbour in graph[node]:
                deep_size += collectApples(neighbour)
            if node == 0: return deep_size
            if hasApple[node] or deep_size: return deep_size + 2
            return deep_size
        
        return collectApples(0)