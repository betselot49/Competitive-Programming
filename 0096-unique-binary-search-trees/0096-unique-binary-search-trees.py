class Solution:
    def numTrees(self, n: int) -> int:
        cache = {0: 1, 1: 1}
        def dp(n):
            if n in cache: return cache[n]
            
            unique_bsts = 0
            for i in range(n):
                unique_bsts += dp(i) * dp(n-i-1)
            cache[n] = unique_bsts
            return unique_bsts
            
        return dp(n)