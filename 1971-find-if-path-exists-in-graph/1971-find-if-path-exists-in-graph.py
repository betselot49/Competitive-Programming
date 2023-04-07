class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)            
            graph[node2].append(node1)
        
        visited = set()
        def validPathFinder(source, destination):
            if source == destination: return True
            
            visited.add(source)
            for neighbour in graph[source]:
                if neighbour not in visited:
                    found = validPathFinder(neighbour, destination)
                    if found: return True
            
            return False
    
        return validPathFinder(source, destination)