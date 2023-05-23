class Solution:
    def minScore(self, n: int, edges: List[List[int]]) -> int:
        root = { i : i for i in range(1, n+1) }
        size = { i : 1 for i in range(1, n+1) }
        min_score = { i : float('inf') for i in range(1, n+1) }
        
        def union(x, y, cost):
            rootX = find(x)
            rootY = find(y)
            
            if size[rootX] <= size[rootY]:
                root[rootX] = rootY
                size[rootY] += size[rootX]
                min_score[rootY] = min(cost, min_score[rootX], min_score[rootY])
            else:
                root[rootY] = rootX
                size[rootX] += size[rootY]
                min_score[rootX] = min(cost, min_score[rootX], min_score[rootY])


        def find(x):
            rootX = root[x]
            while rootX != root[rootX]:
                rootX = root[rootX]

            while x != rootX:
                parent = root[x]
                root[x] = rootX
                x = parent

            return rootX
        
        for city1, city2, distance in edges:
            union(city1, city2, distance)
            
        return min_score[find(1)]