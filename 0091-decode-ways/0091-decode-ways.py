class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s) 
        dp = { N : 1, N-1 : 1 if s[-1] != "0" else 0 }
        
        for i in range(N-2, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
                
            ways = 0 if int(s[i]+s[i+1]) > 26 else 1
            dp[i] = dp[i+1] + (ways * dp[i+2])
        
        return dp[0]