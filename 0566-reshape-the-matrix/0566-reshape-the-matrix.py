class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        
        reshape, reshapeRow, colCounter = [], [], 0
        
        for row in mat:
            for col in row:
                reshapeRow.append(col)
                colCounter += 1
                
                if colCounter == c:
                    reshape.append(reshapeRow)
                    reshapeRow, colCounter = [], 0
                    
        return reshape