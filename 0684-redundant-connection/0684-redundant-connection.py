class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        visited = set()
        path = []
        def cycle_path(node, parent):
            path.append(node)
            if node in visited: return True
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour == parent: continue
                if cycle_path(neighbour, node): return True
            path.pop()
            visited.remove(node)
            return False
    
        cycle_path(1, None)
        cycle = set()
        cycle_node = path.pop()
        
        while True:
            curr = path.pop()
            cycle.add(curr)
            if curr == cycle_node:
                break
            
        for node1, node2 in edges[::-1]:
            if node1 in cycle and node2 in cycle:
                return [node1, node2]