from typing import List
from collections import defaultdict
from collections import deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for node1, node2 in edges:
            graph[node1].append(node2)
            indegree[node2] += 1
        
        queue = deque([])
        for i in range(1, n+1):
            if indegree[i] ==  0:
                queue.append((i, 1))
                
        min_time = [0] * n
        while queue:
            jop, time = queue.popleft()
            min_time[jop-1] = str(time)
            for neighbour in graph[jop]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append((neighbour, time + 1))
                    
        return " ".join(min_time)
        


