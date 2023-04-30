class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        answer = [0] * n
        graph = defaultdict(list)
        visited = set()
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
    

        def dfs(node, labels):
            if node in visited: return {}
            visited.add(node)
            
            path = defaultdict(int)
            path[labels[node]] += 1
            for neighbour in graph[node]:
                neighbour_path = dfs(neighbour, labels)
                for key, value in neighbour_path.items():
                    path[key] += value
            
            answer[node] = path[labels[node]]
            return path.copy()
        
        dfs(0, labels)
        return answer