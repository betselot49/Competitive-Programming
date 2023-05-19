class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.root = {}
        for s in s1:
            self.root[s] = s
        for s in s2:
            self.root[s] = s
        for s in baseStr:
            self.root[s] = s
        
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX != rootY:
                if rootX < rootY:
                    self.root[rootY] = rootX
                else:
                    self.root[rootX] = rootY
                    
        def find(x):
            root = x
            # print(self.root)
            while root != self.root[root]:
                root = self.root[root]
                
            while x != root:
                parent = self.root[x]
                self.root[x] = root
                x = parent
            # print(x, root)
            return root
                
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        # print(self.root)
        answer = ''
        for char in baseStr:
            answer += find(char)
            
        return answer
    
            
            
        