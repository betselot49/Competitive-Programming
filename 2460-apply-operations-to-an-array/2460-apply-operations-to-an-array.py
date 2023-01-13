class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
                
                
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