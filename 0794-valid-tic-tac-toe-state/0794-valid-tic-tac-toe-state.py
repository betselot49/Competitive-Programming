class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        numOfX, numOfO, winnerO, winnerX, diagonal1, diagonal2= 0, 0, 0, 0, "", ""

        count = 2
        for index, row in enumerate(board):
            diagonal1 += row[index]
            diagonal2 += row[count]
            count -= 1
            if row == "OOO":
                winnerO = 1
            elif row == "XXX":
                winnerX = 1
            for col in row:
                if col == "X":
                    numOfX += 1
                elif col == "O":
                    numOfO += 1
        if diagonal1 == "XXX" or diagonal2 == "XXX":
            winnerX = 1
        if diagonal1 == "OOO" or diagonal2 == "OOO":
            winnerO += 1
                    
        if numOfX - numOfO < 0 or numOfX - numOfO > 1:
            return False
        
        for col in range(3):
            winner = ""
            for row in board:
                winner += row[col]
            if winner == "OOO":
                winnerO = 1
            elif winner == "XXX":
                winnerX = 1
        
        if winnerO == 1 and winnerX == 1:
            return False
        elif winnerO == 1 and numOfX > numOfO:
            return False
        elif winnerX == 1 and numOfO >= numOfX:
            return False
        
        return True
            