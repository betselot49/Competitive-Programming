class Solution:
    def countOrders(self, n: int) -> int:
        MOD = (10 ** 9)+ 7   
        return (factorial(2*n) // 2 ** n) % MOD
    
        dp = [0, 1]
        for i in range(2, n+1):
            hole = ((i - 1) * 2) + 1
            total = ((1 + hole) * hole) // 2
            dp.append(dp[i-1] * total % MOD)
            
        return dp[n] % MOD
        
        
        
        
        