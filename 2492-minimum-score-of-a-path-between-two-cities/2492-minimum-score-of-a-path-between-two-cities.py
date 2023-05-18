class Solution:
    def minScore(self, n: int, edges: List[List[int]]) -> int:
        
        self.rep = defaultdict(int)
        for i in range(1, n + 1):
            self.rep[i] = i
        
        self.size = defaultdict(float)
        for i in range(1, n + 1):
            self.size[i] = 1
        
        self.min = defaultdict(float)
        for i in range(1, n + 1):
            self.min[i] = float(inf)
        
        def find( node):
            
            if self.rep[node] == node:
                return node
            
            parent = find(self.rep[node])
            self.rep[node] = parent
            return parent
    
        def union( node1, node2, weight):
            
            rep1, rep2 = find(node1), find(node2)
            
            if self.size[rep1] >= self.size[rep2]:
                self.size[rep1] += self.size[rep2]
                self.min[rep1] = min(weight, self.min[rep2], self.min[rep1])
                self.rep[rep2] = rep1
            else:
                self.size[rep2] += self.size[rep1]
                self.min[rep2] = min(weight, self.min[rep2], self.min[rep1])
                self.rep[rep1] = rep2
                
        for edge in edges:
            union(edge[0], edge[1], edge[2])
      
        return self.min[find(self.rep[1])]
            