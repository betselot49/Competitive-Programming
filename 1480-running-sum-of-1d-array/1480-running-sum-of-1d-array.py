class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for index, num in enumerate(nums[1:]):
            nums[index+1] += nums[index]
        return nums
