class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def isValid(row, col):
            row_inbound = 0 <= row < len(grid)
            col_inbound = 0 <= col < len(grid)
            return (row_inbound and col_inbound and grid[row][col] == 0)
        
        def shortestPath(start, goal):
            if grid[0][0] == 1: return -1
            queue = deque([(start, 1)])
            DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            
            while queue:
                current = queue.popleft()
                if current[0] == goal: return current[1]
                
                for cord1, cord2 in DIRECTIONS:
                    row = current[0][0] + cord1
                    col = current[0][1] + cord2
                    if isValid(row, col):
                        grid[row][col] = 1
                        queue.append(((row, col), current[1]+1))
            return -1
        
        N = len(grid) - 1
        return shortestPath((0, 0), (N, N))
    
   