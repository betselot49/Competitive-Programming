class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        graph = defaultdict(list)
        for row in range(N-1):
            for col in range(row+1, N):
                if isConnected[row][col] == 1:
                    graph[row+1].append(col+1)
                    graph[col+1].append(row+1)
                    
        visited = set()
        print(graph)
        def dfs(node):
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    dfs(child)
                
        groups = 0
        for node in range(1, N+1):
            if node not in visited:
                groups += 1
                dfs(node)
        return groups
                    
            

