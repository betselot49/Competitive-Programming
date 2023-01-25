class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        maxCoin = 0
        
        # Take the second largest number from 2 of piles starting from end until you reach 1/3rd of array. 
        for index in range(len(piles) - 2, len(piles) // 3 - 1, -2): 
            maxCoin += piles[index]
        
        return maxCoin