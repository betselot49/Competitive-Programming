class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:    
        left = 1
        while left < len(nums) and nums[left] > nums[left-1]:
            left += 1
        right = left
        
        while left < len(nums) and right < len(nums):
            while left < len(nums) and nums[left] > nums[left-1]:
                left += 1
                
            cur = nums[right]
            while right < len(nums) and nums[right] == cur:
                right += 1
            
            if right < len(nums) and left < len(nums):
                nums[left] = nums[right]
                left += 1
                
        while len(nums) > left:
            nums.pop()
            
                
                
            