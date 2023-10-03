class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def notValid(row, col):
            return row < 0 or col < 0 or row >= N or col >= N or grid[row][col] == -1
        
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0 ,-1)]
        N = len(grid)
        
        queue = [(grid[0][0], (0, 0), grid[0][0])]
        heapify(queue)
        
        while queue:
            curr, position, max_val = heappop(queue)
            if position == (N-1, N-1): return max_val
            
            row, col = position
            grid[row][col] = -1
            
            for r, c in DIRECTIONS:
                if notValid(row + r, col + c):
                    continue
                
                _next = grid[row+r][col+c]
                next_max = max(max_val, _next)
                heappush(queue, (_next, (row + r, col + c), next_max))
      
    
                
        