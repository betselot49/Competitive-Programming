class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l = len(piles)
        max_coin = 0 
        for i in range(l - 2, l//3 - 1, -2):
            max_coin += piles[i]
        return max_coin
