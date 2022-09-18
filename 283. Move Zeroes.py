class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = -1
        j = 0
        while j < len(nums):
            if nums[j] == 0 and i == -1:
                i = j
            elif nums[j] != 0 and i != -1:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            j += 1  
        return nums
