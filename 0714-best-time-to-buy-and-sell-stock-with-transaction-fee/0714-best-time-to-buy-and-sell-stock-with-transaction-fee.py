class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(idx, turn):
            if idx == len(prices):
                return 0
            if turn == "SELL":
                return max(dp(idx + 1,"BUY") + prices[idx], dp(idx + 1, "SELL"))
            else:
                return max(dp(idx + 1, "SELL") - prices[idx] - fee, dp(idx + 1, "BUY"))

        return dp(0, 0)