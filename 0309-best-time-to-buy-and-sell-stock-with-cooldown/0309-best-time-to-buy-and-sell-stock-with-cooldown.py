class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = {}
        
        max_profit = 0
        for i in range(N-1, -1, -1):
            
            # buying at this index
            buy_profit = -prices[i]
            for j in range(i+1, N):
                buy_profit = max(buy_profit, dp[j][1] + (prices[j] - prices[i]))
            max_profit = max(max_profit, buy_profit)
            
            # selling at this index
            sell_profit = 0
            for j in range(i+2, N):
                sell_profit = max(sell_profit, dp[j][0])
            max_profit = max(max_profit, sell_profit)
           
            dp[i] = [buy_profit, sell_profit]
            
        print(dp)
        return max_profit
            