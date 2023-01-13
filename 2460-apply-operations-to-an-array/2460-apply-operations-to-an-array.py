class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
#         for index in range(len(nums) - 1):
#             if nums[index] == nums[index+1]:
#                 nums[index] *= 2
#                 nums[index+1] = 0
                
            
                
#         left, right = 0, 0
        
#         while right < len(nums):
#             while left < len(nums) and nums[left] != 0:
#                 left += 1
                
#             right = left
#             while right < len(nums) and nums[right] == 0:
#                 right += 1
                
#             if right < len(nums):
#                 nums[left], nums[right] = nums[right], nums[left]     
                
#         return nums
    
    # ===============  more optimal solution =================
        
        left = 0
        for index in range(len(nums)):
            if index + 1 < len(nums) and nums[index] == nums[index+1]:
                nums[index] *= 2
                nums[index+1] = 0
               
            if nums[index]:
                nums[index], nums[left] = nums[left], nums[index]
                left += 1
                
        return nums