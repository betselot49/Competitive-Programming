class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        root = { tuple(stone) : tuple(stone) for stone in stones }
        size = { tuple(stone) : 1 for stone in stones }
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX != rootY:
                if rootX[0] == rootY[0] or rootX[1] == rootY[1] or x[0] == y[0] or x[1] == y[1]:
                    if size[rootX] < size[rootY]:
                        root[rootX] = rootY
                        size[rootY] += size[rootX]
                    else:
                        root[rootY] = rootX
                        size[rootX] += size[rootY]
        
        def find(x):
            rootX = root[x]
            while rootX != root[rootX]:
                rootX = root[rootX]
            
            while x != rootX:
                parent = root[x]
                root[x] = rootX
                x = parent
                
            return rootX
        
        for i in range(len(stones)-1):
            for j in range(i+1, len(stones)):
                union(tuple(stones[i]), tuple(stones[j]))
                
        count = 0
        for stone in stones:
            if find(tuple(stone)) != tuple(stone):
                count += 1
        return count
                
                
        
        