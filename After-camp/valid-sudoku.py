class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for col in row:
                if col != "." and col in seen:
                    return False
                seen.add(col)
                
        for col in range(len(board)):
            seen = set()
            for row in board:
                if row[col] != "." and row[col] in seen:
                    return False
                seen.add(row[col])
                
        for row3 in range(0, 9, 3):
            for col3 in range(0, 9, 3):
                seen = set()
                for row in range(row3, row3+3):
                    for col in range(col3, col3+3):
                        if board[row][col] != "." and board[row][col] in seen:
                            return False
                        seen.add(board[row][col])
                    
        return True