class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for node1, node2, time in times:
            graph[node1].append((time, node2))
            
        queue = [(0, k)]
        heapify(queue)
        total_nodes = 0
        total_time = 0
        visited = set()
        while queue:
            time, node = heappop(queue)
            if node in visited: continue
                
            total_nodes += 1
            total_time = max(total_time, time)
            visited.add(node)
            
            for next_time, next_node in graph[node]:
                heappush(queue, (next_time + time, next_node))
                
        return -1 if total_nodes != n else total_time