class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for index in range(len(nums) - 1):
            if nums[index] == nums[index+1]:
                nums[index] *= 2
                nums[index+1] = 0
                
        #  this section is to move all zeros to the right
         left, right = 0, 0  
            
        while right < len(nums):
            while left < len(nums) and nums[left] != 0:
                left += 1
                
            right = left
            while right < len(nums) and nums[right] == 0:
                right += 1
                
            if right < len(nums):
                nums[left], nums[right] = nums[right], nums[left]     
                
        return nums
    
    # < ===============  more optimal solution ================= >
    # This does both the operation and moving zeros to the right in one loop.
        
        left = 0
        for right in range(len(nums)):
            if right + 1 < len(nums) and nums[right] == nums[right+1]:
                nums[right] *= 2
                nums[right+1] = 0
               
            if nums[right]:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                
        return nums
    
    
