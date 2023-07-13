class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        grid = matrix
        for i in range(1, len(grid)):
            for j in range(len(grid[i])):
                if i-1 >= 0 and j-1 >= 0:
                    p1 = grid[i-1][j-1]
                else:
                    p1 = float('inf')

                if i-1 >= 0:
                    p2 = grid[i-1][j]
                else:
                    p2 = float('inf')

                if i-1 >= 0 and j+1 <= len(grid[0])-1:
                    p3 = grid[i-1][j+1]
                else:
                    p3 = float('inf')

                grid[i][j] += min(p1,p2,p3)

        return min(grid[len(grid)-1])
