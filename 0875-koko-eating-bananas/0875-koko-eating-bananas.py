class Solution:
    def can_koko_eat(self, piles, speed, target_hour):
        total_hour = 0
        for pile in piles:
            total_hour +=  ceil(pile / speed)
        print(speed, total_hour)
        return total_hour <= target_hour
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 0
        high = sum(piles) + 1
        
        while high > low + 1:
            mid = low + (high - low) // 2
            if self.can_koko_eat(piles, mid, h):
                high = mid
            else:
                low = mid
                
        return high