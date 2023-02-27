class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * n for i in range(n)]
        
        for query in queries:
            row1, col1, row2, col2 = query
            mat[row1][col1] += 1
            if col2 + 1 < n:
                mat[row1][col2+1] -= 1
            if row2 + 1 < n:
                mat[row2+1][col1] -= 1
            if row2+1 < n and col2 + 1 < n:
                mat[row2+1][col2+1] += 1
                
        for row in range(n):
            total = 0
            for col in range(n):
                total += mat[row][col]
                mat[row][col] = total
                
        for col in range(n):
            total = 0
            for row in range(len(mat)):
                total += mat[row][col]
                mat[row][col] = total
                
        return mat