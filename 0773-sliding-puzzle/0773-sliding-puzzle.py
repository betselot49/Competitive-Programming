class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def inbound(row, col):
            return 0 <= row and 0 <= col and row <= 1 and col <= 2
        
        def verify(state):
            return state[0][0] == 1 and state[0][1] == 2 and state[0][2] == 3 and state[1][0] == 4 and state[1][1] == 5 and state[1][2] == 0 
        
        for row in range(2):
            for col in range(3):
                if board[row][col] == 0:
                    position = (row, col)
        
        DIRECTIONS = [(-1 ,0), (1, 0), (0, 1), (0, -1)]
        self.min = float("inf")
        queue = deque([(board[:], 0, position[0], position[1])])
        visited = set(tuple(board[0][:] + board[1][:]))
        while queue:
            curr, moves, row, col = queue.popleft()
            if verify(curr):
                self.min = min(self.min, moves)
            
            for r, c in DIRECTIONS:
                if inbound(row+r, col+c):
                    _next = copy.deepcopy(curr)
                    _next[row+r][col+c], _next[row][col] = _next[row][col], _next[row+r][col+c]
                    new_state = tuple(_next[0][:] + _next[1][:])
                    if new_state not in visited:
                        queue.append((_next[:], moves + 1, row+r, col+c))
                        visited.add(new_state)
        
        return -1 if self.min == float("inf") else self.min