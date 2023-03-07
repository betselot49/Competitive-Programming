class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        low, high = -1, N
        while low + 1 < high:
            mid = low + (high - low)//2
            
            if nums[mid] >= target:
                high = mid
            else:
                low = mid
                
        left = -1 if high == N or high < N and nums[high] != target else high
        
        low, high = -1, N
        while low + 1 < high:
            mid = low + (high - low) // 2
            
            if nums[mid] <= target:
                low = mid
            else:
                high = mid
        
        right = -1 if low >= 0 and nums[low] != target else low
        
        return [left, right]     
            
        
            