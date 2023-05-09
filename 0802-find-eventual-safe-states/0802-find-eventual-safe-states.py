class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.stack = []
        n = len(graph)

        self.color = [0 for i in range(n)]
        
        for node in range(n):
            if self.color[node] == 0:
                self.topologicalSort(graph,node)
                
            
            
        return sorted(self.stack)
    
    
    def topologicalSort(self,graph,node):
        
        if self.color[node] == 1:
            return False
        
        self.color[node] = 1
        for neig in graph[node]:
            if self.color[neig] == 2:
                continue

            if not self.topologicalSort(graph,neig):
                return False

        self.color[node] = 2
        self.stack.append(node)
        return True