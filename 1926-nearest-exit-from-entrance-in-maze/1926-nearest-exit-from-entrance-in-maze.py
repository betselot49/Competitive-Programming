class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def isValid(row, col):
            row_inbound = 0 <= row < len(maze)
            col_inbound = 0 <= col < len(maze[0])
            return row_inbound and col_inbound
               
        queue = deque([(entrance[0], entrance[1], 0)])
        DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]
        while queue:
            row, col, level = queue.popleft()
            if not isValid(row, col) or maze[row][col] == "+": continue
            onBound = row == 0 or row == len(maze)-1 or col == 0 or col == len(maze[0])-1
            if onBound and maze[row][col] == "." and [row, col] != entrance: return level
            maze[row][col] = "+"
            for cord1, cord2 in DIRECTIONS:
                new_row, new_col = row + cord1, col + cord2
                queue.append((new_row, new_col, level+1))
        return -1
                