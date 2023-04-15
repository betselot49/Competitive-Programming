class Solution:
    def __init__(self):
        self.curr = 0
        self.max_denoted = 1
        
    def dfs(self, bomb, denoted, graph):
        denoted.add(bomb)
        self.curr += 1
        for neighbour in graph[bomb]:
            if neighbour not in denoted:
                self.dfs(neighbour, denoted, graph)
                
    def maximumDetonation(self, bombs: List[List[int]]) -> int:     
        graph = defaultdict(list)
        for main in range(len(bombs)):
            main_x, main_y, main_radius = bombs[main][0], bombs[main][1], bombs[main][2]
            for bomb in range(len(bombs)):
                x_axis, y_axis, radius = bombs[bomb][0], bombs[bomb][1], bombs[bomb][2]
                if main == bomb: continue
                if ((main_x - x_axis) ** 2 + (main_y - y_axis) ** 2) ** 0.5 <= main_radius:
                    graph[main].append(bomb)

        bombs = list(graph.keys())
        for bomb in bombs:
            self.curr = 0
            denoted = set()
            self.dfs(bomb, denoted, graph)
            self.max_denoted = max(self.curr, self.max_denoted)
        return self.max_denoted
            