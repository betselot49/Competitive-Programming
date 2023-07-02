class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for idx, num in enumerate(parent):
            graph[num].append(idx)
                              
        self.longest_path = 1
        def dfs(node):
            if node not in graph: return 1
            
            best_path = 0
            two_best = []
            for neighbour in graph[node]:
                curr = dfs(neighbour)
                if s[neighbour] != s[node]:
                    if len(two_best) < 2:
                        two_best.append(curr)
                    else:
                        if two_best[0] < two_best[1]:
                            two_best[0] = max(two_best[0], curr)
                        else:
                            two_best[1] = max(two_best[1], curr)
                            
                    best_path = max(best_path, curr)
                    
            self.longest_path = max(self.longest_path, best_path + 1, sum(two_best) + 1)
            return best_path + 1
        
        dfs(0)
        return self.longest_path