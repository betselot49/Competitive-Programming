class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N  = len(grid[0])
        pre_sum1, pre_sum2  = grid[0].copy(), grid[1].copy()
        
        for i in range(1, N):
            pre_sum1[i] += pre_sum1[i-1]
            pre_sum2[i] += pre_sum2[i-1]
        
        res = float('inf')
        for i in range(N):
            top = pre_sum1[-1] - pre_sum1[i]
            bottom = pre_sum2[i-1] if i > 0 else 0
            res = min(res, max(top, bottom))
        return res
        
        
            
                
                
        
        