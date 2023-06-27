class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
#         Top down
#         memo = {}
#         def backtrack(idx):
#             if idx >= len(cost): return 0
#             if idx in memo: return memo[idx]
            
#             memo[idx] = min(cost[idx] + backtrack(idx+1), cost[idx] + backtrack(idx+2))
#             return memo[idx]
        
#         backtrack(0)
#         return min(memo[0], memo[1])
    
    
        #  bottom up
        n = len(cost) 
        memo = [0] * (n + 1)
        for i in range(2, n+1):
            memo[i] = min(memo[i-1] + cost[i-1], memo[i-2]+ cost[i-2])
        return memo[n]
    
    
      
        