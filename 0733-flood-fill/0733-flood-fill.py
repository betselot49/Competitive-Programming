class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()
        def backtrack(row, col, color, target):
            if (row < 0 or col < 0 or
               row == len(image) or col == len(image[0]) or 
               image[row][col] != target): return 
            
            image[row][col] = color
            visited.add((row, col))
            for cord1, cord2 in directions:
                if (row + cord1, col + cord2) not in visited:
                    backtrack(row + cord1, col + cord2, color, target)
        
        target = image[sr][sc]
        backtrack(sr, sc, color, target)
        return image