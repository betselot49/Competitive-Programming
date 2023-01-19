class Solution: 
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroLocation = []  # used to hold the location of zeros
        
        for rowInd, row in enumerate(matrix):
            for colInd, col in enumerate(row):
                if col == 0:
                    zeroLocation.append([rowInd, colInd])
        
        for location in zeroLocation:  
            matrix[location[0]] = [0] * len(matrix[0])
            for row in range(len(matrix)):
                matrix[row][location[1]] = 0
                