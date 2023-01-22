class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        newPosition, n = defaultdict(int), len(matrix)
        
        for row in range(n):
            for col in range(n):
                newPosition[(col, n-row-1)] = matrix[row][col]   
        
        for (row,col), num in newPosition.items():
            matrix[row][col] = num
        