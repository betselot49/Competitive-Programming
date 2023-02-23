class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr = 0
        for index, num in enumerate(nums):
            curr += num
            nums[index] = curr
            
        return nums