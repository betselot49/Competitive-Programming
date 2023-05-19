class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equal = []
        notEqual = []
        for equetion in equations:
            if equetion[1] == "!":
                notEqual.append(equetion)
            else:
                equal.append(equetion)
        equations = equal + notEqual
        
        
        root = {chr(i+97): chr(i+97) for i in range(26)}
        size = {chr(i+97):1 for i in range(26)}
        
        def union(x, y):       
            rootX = find(x)
            rootY = find(y)
            
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
        
        for equetion in equations:
            if equetion[1] == "!":
                if find(equetion[0]) == find(equetion[-1]): return False
            else:
                union(equetion[0], equetion[-1])
                
        return True