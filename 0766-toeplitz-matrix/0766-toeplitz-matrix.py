class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diagonal = defaultdict(list)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if len(diagonal[row-col]) == 0:
                    diagonal[row-col].append(matrix[row][col])
                else:
                    if diagonal[row-col][-1] != matrix[row][col]:
                        return False
                    
        return True