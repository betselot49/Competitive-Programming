class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        answer = [set() for i in range(n)]
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            indegree[node2] += 1
            
        queue = deque([])
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            node = queue.popleft()
            path = answer[node].copy()
            path.add(node)
            for neighbour in graph[node]:
                answer[neighbour].update(path)
                indegree[neighbour] -= 1
                if not indegree[neighbour]:
                    queue.append(neighbour)
                
            
        for i in range(n):
            answer[i] = sorted(list(answer[i]))
        
        return answer