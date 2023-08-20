class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        ahead=[0]*2
        ahead2=[0]*2
        curr=[0]*2
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                profit=0
                if buy==0: #buy a stock
                    take=-prices[ind]+ahead[1] 
                    not_take=0+ahead[0]
                    profit=max(take,not_take)
                else:
                    take=prices[ind]+ahead2[0] # +2 for cooldown
                    not_take=0+ahead[1]
                    profit=max(take,not_take)
                curr[buy]=profit
            ahead2=ahead[:]
            ahead=curr[:]
        return curr[0]