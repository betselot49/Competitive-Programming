class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
#         i = -1
#         j = 0
#         while j < len(nums):
#             if nums[j] == 0 and i == -1:
#                 i = j
#             elif nums[j] != 0 and i != -1:
#                 nums[j], nums[i] = nums[i], nums[j]
#                 i += 1
#             j += 1  
            
        seeker = 0
        holder = 0
        while seeker < len(nums):
            if nums[seeker] != 0:
                nums[seeker], nums[holder] = nums[holder], nums[seeker]
                holder += 1
            seeker += 1