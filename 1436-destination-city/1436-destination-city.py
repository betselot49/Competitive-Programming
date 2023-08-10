class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = {}
        for city1, city2 in paths:
            graph[city1] = city2
        
        start = paths[0][0]
        while start in graph:
            start = graph[start]
        return start