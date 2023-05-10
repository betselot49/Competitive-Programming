class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        truth_ans = [False] * numCourses
        
        graph = defaultdict(list)
        for node1, node2 in prerequisites:
            graph[node1].append(node2)
        
        def dfs(node, path):
            if node in path: return False
            
            if truth_ans[node]: return True
            
            if not graph[node]:
                truth_ans[node] = True
                return True
            
            path.add(node)
            for neighbour in graph[node]:
                if not dfs(neighbour, path.copy()): return False
                
            path.remove(node)
            
            truth_ans[node] = True
            return True
        
        for i in range(numCourses):
            path = set()
            if not dfs(i, path): return False
            
        return True