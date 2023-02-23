class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        matrix.insert(0, [0] * len(matrix[0]))
        for row in matrix:
            row.insert(0, 0)
        self.matrix = matrix
            
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                self.matrix[row][col] += (self.matrix[row-1][col] + self.matrix[row][col-1] - self.matrix[row-1][col-1])
    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2+1][col2+1] - self.matrix[row2+1][col1] - self.matrix[row1][col2+1] + self.matrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)