class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        maxRow = []
        length = len(grid) - 2
        
        for row in grid:
            temp = []
            for index in range(length):
                temp.append(max(row[index],row[index+1], row[index+2]))
            maxRow.append(temp)
            
        maxGrid = []
        for row in range(length):
            temp = []
            for col in range(length):
                temp.append(max(maxRow[row][col], maxRow[row+1][col], maxRow[row+2][col]))
            maxGrid.append(temp)
            
        return maxGrid