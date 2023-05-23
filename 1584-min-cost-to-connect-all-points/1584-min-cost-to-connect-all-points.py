class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        self.min_cost = 0
        root = { tuple(point) : tuple(point) for point in points }
        size = { tuple(point) : 1 for point in points }
        for i in range(len(points)-1):
            point1 = points[i]
            for j in range(i+1, len(points)):
                point2 = points[j]
                manh_dis = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                distances.append([manh_dis, [point1, point2]])
                
        distances.sort()
        def union(x, y, cost):
            rootX = find(x)
            rootY = find(y)
            
            # union them if they are not already connected 
            if rootX != rootY:
                self.min_cost += cost
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
        
        for distance, points in distances:
            union(tuple(points[0]), tuple(points[1]), distance)
            
        return self.min_cost