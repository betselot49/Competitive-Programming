class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def explore(row, col):
            rowInbound = 0 <= row < len(board)
            colInbound = 0 <= col < len(board[0])
            if not rowInbound or not colInbound or board[row][col] == "X": return 
            if row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1:
                self.surrounded = False
            self.path.append((row, col))
            board[row][col] = "X"
            for cord1, cord2 in self.DIRECTIONS:
                explore(row + cord1, col + cord2)
                
        
        self.boarder = []
        self.DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.surrounded = True
                self.path = []
                explore(row, col)
                if not self.surrounded and self.path:
                    self.boarder.append(self.path)
        for region in self.boarder:
            for row, col in region:
                board[row][col] = "O"
        
        
       