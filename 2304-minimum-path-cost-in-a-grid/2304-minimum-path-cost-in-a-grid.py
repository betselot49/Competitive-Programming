class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        for row in range(N-2, -1, -1):
            for col in range(M):
                curr = grid[row][col]
                grid[row][col] += (grid[row+1][col] + moveCost[curr][col])
                for next_col in range(M):
                    grid[row][col] = min(grid[row][col], curr + grid[row+1][next_col] + moveCost[curr][next_col])
                    
        return min(grid[0])