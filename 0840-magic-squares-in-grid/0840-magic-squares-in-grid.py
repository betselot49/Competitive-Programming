class Solution:
    def distnict(self, matrix):
        sett = {1,2,3,4,5,6,7,8,9}
        seen = set()
        for row in matrix:
            for col in row:
                if col not in sett or col in seen:
                    return False
                seen.add(col)
                
        return True
    
    
    def magicChecker(self, matrix):
        row1, row2, row3 = sum(matrix[0]), sum(matrix[1]), sum(matrix[2])
        column = []
        for col in range(3):
            temp = 0
            for row in matrix:
                temp += row[col]
            column.append(temp)
        col1, col2, col2 = column
        
        diag1, diag2 = matrix[0][0] + matrix[1][1] + matrix[2][2], matrix[2][0] + matrix[1][1] + matrix[0][2]
        
        if row1 == row2 == row3 == col1 == col2 == col2 == diag1 == diag2:
            return 1
        return 0
    
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        
        count = 0
        for col in range(len(grid[0])-2):
            for row in range(len(grid)-2):
                matrix = [grid[row][col:col+3], grid[row+1][col:col+3], grid[row+2][col:col+3]]
                if self.distnict(matrix):
                    count += self.magicChecker(matrix)
        return count