class Solution:
    def capacityCheck(self, weights, capacity, days):
        curr_sum = 0
        curr_day = 0
        for weight in weights:
            curr_sum += weight
            
            if curr_sum > capacity:
                curr_day += 1
                curr_sum = weight
                
        curr_day += 1
        return curr_day <= days
        
    
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights) - 1
        high = sum(weights)
        print(high)
        
        while low + 1 < high:
            mid = low + (high - low) // 2
            
            if self.capacityCheck(weights, mid, days):
                high = mid
            else:
                low = mid
                
        return high