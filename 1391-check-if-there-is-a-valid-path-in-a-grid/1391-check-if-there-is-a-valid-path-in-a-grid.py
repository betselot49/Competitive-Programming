class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        direction = { 1: [(0, 1), (0, -1)], 2: [(-1, 0), (1, 0)], 3: [(0, -1), (1, 0)], 4: [(0, 1), (1, 0)], 5: [(-1, 0), (0, -1)], 6: [(0, 1), (-1, 0)] }
        street = {(0, 1):(1, 3, 5), (0 ,-1): (1, 4, 6), (1, 0):(2, 5, 6), (-1, 0): (2, 3, 4)}
        
        visited = set()
        def traverse(row, col):
            if (row, col) == (len(grid)-1, len(grid[0])-1): return True
            print(row, col)
            visited.add((row, col))
            for r, c in direction[grid[row][col]]:
                newR, newC = row + r, col + c
                if not inbound(newR, newC) or (newR, newC) in visited: continue
                if grid[newR][newC] in street[(r, c)]:
                    if traverse(newR, newC): return True
            
            return False
                

        def inbound(row, col):
            return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])
        
        return traverse(0, 0)