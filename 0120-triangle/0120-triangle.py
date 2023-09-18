class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        for i in range(N-2, -1, -1):
            for j in range(len(triangle[i])):
                curr = triangle[i][j]
                triangle[i][j] = min(curr +  triangle[i+1][j], curr +  triangle[i+1][j+1])
                
        return triangle[0][0]