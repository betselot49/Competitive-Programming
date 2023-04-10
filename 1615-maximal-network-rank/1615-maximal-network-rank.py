class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for node1, node2 in roads:
            graph[node1].add(node2)
            graph[node2].add(node1)
            
        max_network = 0   
        for i in range(n):
            for j in range(i+1, n):
                curr = len(graph[i]) + len(graph[j]) - 1 if j in graph[i] else len(graph[i]) + len(graph[j])
                max_network = max(max_network, curr)
                
        return max_network