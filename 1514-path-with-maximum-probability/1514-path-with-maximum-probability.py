class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for idx, edge in enumerate(edges):
            node1, node2 = edge
            graph[node1].append((succProb[idx], node2))            
            graph[node2].append((succProb[idx], node1))

        min_heap = [(-1, start_node)]
        heapify(min_heap)
        visited = set()
        
        while min_heap:
            prob, node = heappop(min_heap)
            if node == end_node: return prob * -1
            if node in visited: continue
                    
            visited.add(node)
            for next_prob, next_node in graph[node]:
                heappush(min_heap, (prob * next_prob, next_node))
        
        return 0
    