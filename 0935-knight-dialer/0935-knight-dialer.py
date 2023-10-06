class Solution:
    def knightDialer(self, n: int) -> int:
        dial_pad_nums = [1, 2 ,3, 4, 5, 6, 7, 8, 9, -1, 0, -1]
        MODULO = (10 ** 9) + 7
        grid_dic = {}
        idx = 0
        for i in range(4):
            for j in range(3):
                grid_dic[(i, j)] = dial_pad_nums[idx]
                idx += 1
         
        dp = {}
        def evaluate(row, col, n):
            if row < 0 or col < 0 or row > 3 or col > 2  or grid_dic[(row, col)] == -1: return 0
            return dp[(row, col, n)]
        
        
        DIRECTIONS = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (1,-2), (-1,2), (1,2)]
        for i in range(1, n+1):
            for row, col in list(grid_dic.keys()):
                if grid_dic[(row, col)] == -1: 
                    dp[(row, col, i)] = 0
                    continue
                if i == 1:
                    dp[(row, col, i)] = 1
                    continue
    
                possible_dial = 0
                for r, c in DIRECTIONS:
                    possible_dial += evaluate(row + r , col + c, i-1)
                
                dp[(row, col, i)] = possible_dial
                
        total = 0
        for row, col in list(grid_dic.keys()):
            total += dp[(row, col, n)]
 
        return total % MODULO
                    
                    