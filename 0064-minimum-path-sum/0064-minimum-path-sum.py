class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        for row in range(N-1, -1, -1):
            for col in range(M-1, -1, -1):
                right = grid[row][col+1] if col + 1 < M else float("inf")
                bottom = grid[row + 1][col] if row + 1 < N else float("inf") 
                if (row, col) == (N-1, M-1): continue
                grid[row][col] += min(right, bottom) 
        return grid[0][0]