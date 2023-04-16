class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def subIsland(row, col):
            if (row < 0 or col < 0 or row == len(grid2) or col == len(grid2[0]) or grid2[row][col] == 0): return 
            if grid1[row][col] == 0:
                self.sub_island = False
            grid2[row][col] = 0
            for cord1, cord2 in directions:
                subIsland(row + cord1, col + cord2)
            
        sub_islands = 0
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col]:
                    self.sub_island = True
                    subIsland(row, col)
                    if self.sub_island:
                        sub_islands += 1
        return sub_islands