class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        grid = [([0] * n) for _ in range(n)]
        
        # Build the grid
        for i, preference in enumerate(preferences):
            N = len(preference)
            for rank, j in enumerate(preference):
                grid[i][j] = N - rank
            
        pair = {}
        for u, v in pairs:
            pair[u] = v
            pair[v] = u
         
        unhappy_frds = 0
        for i in range(n):
            unhappy = False
            friend = pair[i]
            rank = grid[i][friend]
            if rank == n - 1: continue
                
            for j, j_rank in enumerate(grid[i]):
                if j == i or j_rank < rank or j == friend: continue
                
                
                j_frd = pair[j]
                if grid[j][j_frd] < grid[j][i]:
                    unhappy = True
                    break
             
            if unhappy:
                unhappy_frds += 1
            
                
        return unhappy_frds