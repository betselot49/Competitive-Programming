class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowSum, colSum = [], [0] * len(grid[0])
    
        for row in grid:
            cur = 0
            for index, col in enumerate(row):
                if col:
                    cur += 1
                    colSum[index] += 1  # prepare column sum
                else:
                    cur -= 1
                    colSum[index] -= 1
            rowSum.append(cur)  # prepare row sum
        
        diff = []
        for row in rowSum:
            cur = []
            for col in colSum:
                cur.append(row + col) # add row and colum
            diff.append(cur)
        
        return diff
        
        
       