class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        row, col, ans = 0, 0, []
        ans.append(mat[row][col])
        
        while row < len(mat) - 1 or col < len(mat[0]) - 1: # while there is space right and below
            
            if col < len(mat[0]) - 1: # check space to right
                col += 1
                ans.append(mat[row][col])
            elif row < len(mat) - 1: # check space below
                row += 1
                ans.append(mat[row][col])
        
            while row < len(mat) - 1 and col > 0:  # while there is space below and left
                row += 1
                col -= 1
                ans.append(mat[row][col])
        
            if row < len(mat) - 1:  # check space below 
                row += 1
                ans.append(mat[row][col])
            elif col < len(mat[0]) - 1: # check space right
                col += 1
                ans.append(mat[row][col])
            
            while col < len(mat[0]) - 1 and row > 0:  # while there is space above and right
                col += 1
                row -= 1
                ans.append(mat[row][col])
            
        return ans
               
            