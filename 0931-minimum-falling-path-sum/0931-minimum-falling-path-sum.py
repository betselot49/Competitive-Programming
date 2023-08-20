class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N, M = len(matrix), len(matrix[0])
        for row in range(N - 2, -1, -1):
            for col in range(M):
                bottom_left = matrix[row+1][col-1] if col - 1 >= 0 else float("inf")
                bottom = matrix[row+1][col]
                bottom_right = matrix[row+1][col+1] if col + 1 < M else float("inf")
                
                matrix[row][col] = min(bottom_left, bottom, bottom_right) + matrix[row][col]
        return min(matrix[0])
