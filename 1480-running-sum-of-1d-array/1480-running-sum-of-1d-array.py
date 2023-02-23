class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # for index, num in enumerate(nums[1:]):
        #     nums[index+1] += nums[index]
        # return nums
        curr = 0
        for index, num in enumerate(nums):
            curr += num
            nums[index] = curr
            
        return nums