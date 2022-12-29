class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
           [1,  2,  3]
              
         
           [4,  5,  6]
          
        
     row = [7,  8,  9]
            col
          
         
         row = 0
         col = 0
         
         ans = 1, 2, 4
        
        append, if row == 0 => col += 1 => append while row != 0 => <-------------------------|                         
                                                                                              |
        row += 1 ans col -= 1 then append, if col == 0 => row += 1 appen while row != 0 =>    |
                                                                                              |
        row -= 1 and col += 1 then appen, if row == 0 => col += 1 => append while  -----------|
        
        """
        
        row, col, ans = 0, 0, []
        ans.append(mat[row][col])
        
        while row < len(mat) - 1 or col < len(mat[0]) - 1:
            
            if col < len(mat[0]) - 1:
                col += 1
                ans.append(mat[row][col])
            elif row < len(mat) - 1:
                row += 1
                ans.append(mat[row][col])
        
            while row < len(mat) - 1 and col > 0:
                row += 1
                col -= 1
                ans.append(mat[row][col])
        
            if row < len(mat) - 1:
                row += 1
                ans.append(mat[row][col])
            elif col < len(mat[0]) - 1:
                col += 1
                ans.append(mat[row][col])
            
            while col < len(mat[0]) - 1 and row > 0:
                col += 1
                row -= 1
                ans.append(mat[row][col])
            
        return ans
               
            