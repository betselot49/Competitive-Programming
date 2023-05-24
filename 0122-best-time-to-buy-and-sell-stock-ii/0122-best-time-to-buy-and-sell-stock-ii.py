class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                cost += prices[i+1] - prices[i]
        return cost
            