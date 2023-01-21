class Solution:
    def sortColors(self, nums: List[int]) -> None:
        first = 0
        second = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[second], nums[i] = nums[i], nums[second]
                second += 1
            elif nums[i] == 0:
                nums[second], nums[i] = nums[i], nums[second]
                nums[first], nums[second] = nums[second], nums[first]
                first += 1
                second += 1
        return nums
    
                
                