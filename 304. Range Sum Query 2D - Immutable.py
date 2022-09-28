class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        column = len(matrix[0])
        self.preSumMat = [[0] * (column + 1) for r in range(row + 1)]

        for r in range(row):
            pre_sum = 0
            for c in range(column):
                pre_sum += matrix[r][c]
                area_above = self.preSumMat[r][c + 1]
                self.preSumMat[r + 1][c + 1] = pre_sum + area_above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.preSumMat[row2 + 1][col2 + 1]
        region_above = self.preSumMat[row1][col2 + 1]
        region_left = self.preSumMat[row2 + 1][col1]
        region_top_left = self.preSumMat[row1][col1]
        return total - region_left - region_above + region_top_left
