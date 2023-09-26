class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp, N, M = {}, len(dungeon), len(dungeon[0])
        for i in range(N-1, -1, -1):
            for j in range(M-1, -1, -1):
                if j + 1 == M and i + 1 == N:
                    dp[(i, j)] = 1 - dungeon[i][j] if dungeon[i][j] < 1 else 1
                    continue
                    
                
                right = float("inf")
                bottom = float("inf")
                if j + 1 < M:
                    right = dp[(i, j+1)] - dungeon[i][j]
                
                if i + 1 < N:
                    bottom = dp[(i+1, j)] - dungeon[i][j]
                    
                right = 1 if right < 1 else right
                bottom = 1 if bottom < 1 else bottom
            
                dp[(i, j)] = min(right, bottom)
                
        return dp[(0,0)]