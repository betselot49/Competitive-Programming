class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        def pathFinder(node, path, destination):
            path.append(node)
            if node == destination:
                paths.append(path[:])
                path.pop()
                return
            
            for neighbour in graph[node]:
                pathFinder(neighbour, path, destination)
            path.pop()
        
        pathFinder(0, [], len(graph)-1)
        return paths
        
        
        
        