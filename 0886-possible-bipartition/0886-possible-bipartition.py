class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        visited = {}
        self.isValid = True
        graph = defaultdict(list)
        for node1, node2 in dislikes:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        def dfs(node, turn):
            if node in visited and visited[node] != turn: return False
            if node in visited: return self.isValid
            visited[node] = turn
            
            for child in graph[node]:
                if self.isValid: 
                    self.isValid = dfs(child, 1 - turn)
            return self.isValid
        
        valid = True
        for node in range(1, n+1):
            if node not in visited and valid:
                valid = dfs(node, 0)
        return valid