class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1] * n for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = 0
                
        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = matrix[row-1][col] + matrix[row][col-1]
        
        return matrix[-1][-1]
        
        