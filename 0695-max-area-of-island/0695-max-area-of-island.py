class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.area = self.max_area = 0
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def dfs(row, col):
            if (row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] == 0): return 
            self.area += 1
            grid[row][col] = 0
            for cord1, cord2 in self.directions:
                dfs(row + cord1, col + cord2)
                
                
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    self.area = 0
                    dfs(row, col)
                    self.max_area = max(self.area, self.max_area)
        return self.max_area
                    