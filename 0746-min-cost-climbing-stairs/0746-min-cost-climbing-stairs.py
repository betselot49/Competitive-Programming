class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def backtrack(idx):
            if idx >= len(cost): return 0
            if idx in memo: return memo[idx]
            
            memo[idx] = min(cost[idx] + backtrack(idx+1), cost[idx] + backtrack(idx+2))
            return memo[idx]
        
        backtrack(0)
        return min(memo[0], memo[1])
      
        