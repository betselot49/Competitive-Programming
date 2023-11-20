class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        startCol, startRow, endCol, endRow = 0, 0, len(matrix[0]), len(matrix)
        
        index1, index2, counter, spiralList = 0, 0, 0, []
       
        while counter < len(matrix[0] * len(matrix)):  # simulate until the cycle ends.
            for index1 in range(startCol, endCol):
                if counter < len(matrix[0] * len(matrix)):
                    spiralList.append(matrix[index2][index1])
                    counter += 1
            startRow += 1

            for index2 in range(startRow, endRow):
                if counter < len(matrix[0] * len(matrix)):
                    spiralList.append(matrix[index2][index1])
                    counter += 1
            endCol -= 1

            for index1 in range(endCol - 1, startCol - 1, -1):
                if counter < len(matrix[0] * len(matrix)):
                    spiralList.append(matrix[index2][index1])
                    counter += 1
            endRow -= 1

            for index2 in range(endRow - 1, startRow - 1, -1):
                if counter < len(matrix[0] * len(matrix)):
                    spiralList.append(matrix[index2][index1])
                    counter += 1
            startCol += 1
        
        return spiralList