class Solution:
    def checker(self, array, mid):
        total = 0
        for num in array:
            total += ceil(num / mid)
        return total
    
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 0
        high = max(nums) + 1
        
        while low + 1 < high:
            mid = low + (high - low) // 2
        
            if self.checker(nums, mid) <= threshold:
                high = mid
            else:
                low = mid
                
        return high
            