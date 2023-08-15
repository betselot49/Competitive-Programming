class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1: return 0
        
        N, M = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[-1][-1] = 1        
        for row in range(N - 1, -1, -1):
            for col in range(M - 1, -1, -1):
                if obstacleGrid[row][col] == 1 and (row, col) != (N-1, M-1):
                    obstacleGrid[row][col] = 0
                    continue
                    
                if row + 1 < len(obstacleGrid):
                    obstacleGrid[row][col] += obstacleGrid[row + 1][col]
                    
                if col + 1 < len(obstacleGrid[0]):
                    obstacleGrid[row][col] += obstacleGrid[row][col + 1]
                    
        return obstacleGrid[0][0]
