class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        degree = defaultdict(int)
        graph = defaultdict(list)
        
        for node1, node2 in adjacentPairs:
            graph[node1].append(node2)
            graph[node2].append(node1)
            degree[node1] += 1
            degree[node2] += 1
            
        queue = deque([])
        for key in list(degree.keys()):
            if degree[key] == 1:
                queue.append(key)
        
        last_element = queue.pop()
        answer = []       
        while queue:
            curr = queue.popleft()
            answer.append(curr)
            degree[curr] -= 1
            for neighbour in graph[curr]:
                degree[neighbour] -= 1
                if degree[neighbour] == 1:
                    queue.append(neighbour)
                    
        answer.append(last_element)
        return answer
        
        