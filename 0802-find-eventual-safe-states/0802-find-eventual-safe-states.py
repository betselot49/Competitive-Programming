class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        truth_val = [False] * len(graph)
        answer = set()
        
        def dfs(node, path):
            if not graph[node]:
                answer.add(node)
                return True
            
            if node in path: return False
            
            if truth_val[node]: return True
            
            path.add(node)
            
            truth = True
            for neighbour in graph[node]:
                truth = truth and dfs(neighbour, path.copy())
                
            path.remove(node)
            
            if truth:
                truth_val[node] = True
                answer.add(node)  
                
            return truth
            
        for i in range(len(graph)):
            path = set()
            if i in answer: continue
            dfs(i, path)
            
        answer = list(answer)
        answer.sort()
        return answer