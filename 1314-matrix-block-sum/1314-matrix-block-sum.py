class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        mat.insert(0, [0] * len(mat[0]))
        for row in mat:
            row.insert(0, 0)
        
        for row in range(1, len(mat)):
            for col in range(1, len(mat[0])):
                mat[row][col] += mat[row-1][col] + mat[row][col-1] - mat[row-1][col-1]
                
        newMat = [[0] * (len(mat[0])-1) for _ in range(len(mat)-1)]
 
        for row in range(len(newMat)):
            for col in range(len(newMat[0])):
                row2 = row+k+1 if row+k+1 < len(mat) else len(mat)-1
                col2 = col+k+1 if col+k+1 < len(mat[0]) else len(mat[0]) - 1
                row1 = row-k+1 if row-k > 0 else 1
                col1 = col-k+1 if col-k+1 > 0 else 1
             
                newMat[row][col] = mat[row2][col2] - mat[row2][col1-1] - mat[row1-1][col2] + mat[row1-1][col1-1]
                
        return newMat
                
            
        