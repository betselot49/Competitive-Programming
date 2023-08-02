class Solution:
    def knightProbability(self, n: int, move: int, row: int, col: int) -> float:
        DIRECTIONS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
        dp = {}
        
        def find(n, move, row, col):
            if row < 0 or col < 0 or row >= n or col >= n: return 0
            if move == 0: return 1
            
            if (move, row, col) in dp: return dp[(move, row, col)]
            
            probability = 0
            for drc in DIRECTIONS:
                probability += find(n, move-1, row + drc[0], col + drc[1]) / 8
            
            dp[(move, row, col)] = probability
            return probability
        
        return find(n, move, row, col)