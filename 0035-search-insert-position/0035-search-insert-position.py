class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        mid = (low + high) // 2
        
        while high - low > 1:
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                low = mid
            else:
                high = mid
                
            mid = (low + high) // 2
            
        
        if nums[mid] < target:
            return mid + 1
        else:
            return mid
        
        
  