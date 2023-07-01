class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = click
        if board[row][col] == "M":
            board[row][col] = "X"
            return board
        
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        def inbound(row, col):
            return row >= 0 and col >= 0 and row < len(board) and col < len(board[0])  
        
        queue = deque([click])
        visited = set(tuple(click))
        while queue:
            row, col = queue.popleft()  
            mine = 0
            next_click = []
            for direction in DIRECTIONS:
                r, c = direction
                if not inbound(row+r, col+c): continue
                
                if board[row+r][col+c] == "E" and (row+r, col+c) not in visited:
                    next_click.append([row+r, col+c])
                elif board[row+r][col+c] == "M":
                    mine += 1
                    
            if mine:
                board[row][col] = str(mine)
            else:
                queue.extend(next_click)
                for click in next_click:
                    visited.add(tuple(click))
                board[row][col] = "B"
                
        return board
        