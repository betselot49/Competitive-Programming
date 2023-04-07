class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def initialLand():
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == 1: return (row, col)
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.perimeter = 0
        visited = set()
        def backtrack(land):
            if (land[0] < 0 or land[0] == len(grid) or
                land[1] < 0 or land[1] == len(grid[0]) or
                grid[land[0]][land[1]] == 0): 
                self.perimeter += 1
                return 
            
            visited.add(land)
            for cord1, cord2 in directions:
                row = cord1 + land[0]
                col = cord2 + land[1]
                if (row, col) not in visited:
                    backtrack((row, col))
                
        
        initial_land = initialLand()
        backtrack(initial_land)
        return self.perimeter
        