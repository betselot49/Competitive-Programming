class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp, N = defaultdict(lambda : (0, 0)), len(prices)
        for i in range(N-1, -1, -1):
            # buying at this index
            buy = dp[i+1][1] - prices[i]          
            buy = max(buy, dp[i+1][0])
            
            # selling at this index
            sell = dp[i+1][0] + (prices[i] - fee)
            sell = max(sell, dp[i+1][1])
            
            # store dp[i] in the format of (max_buy, max_sell)
            dp[i] = (buy, sell)
        
        return dp[0][0]