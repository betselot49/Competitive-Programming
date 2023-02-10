class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        length = len(grid)
        queue = deque()  # to store the position of land in the grid.
        for row in range(length):
            for col in range(length):
                if grid[row][col]:
                    queue.append([row, col])
                    
                    
        distance = -1
        directions = [[0,1], [1,0], [-1,0], [0,-1]]  # the four possible directions relative to land
        
        while queue:
            row, col = queue.popleft()  # for every land in the queue and the appended lands
            distance = grid[row][col]
            
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if (min(newRow, newCol) >= 0 and
                    max(newRow, newCol) < length and
                    grid[newRow][newCol] == 0):
                    grid[newRow][newCol] = grid[row][col] + 1
                    queue.append([newRow, newCol])
                    
        return distance - 1 if distance > 1 else -1  
                    