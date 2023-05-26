class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def DP(n):
            if n <= 2: return n
            
            if n not in memo:
                memo[n] = DP(n-1) + DP(n - 2)
            return memo[n]
        
        return DP(n)
        