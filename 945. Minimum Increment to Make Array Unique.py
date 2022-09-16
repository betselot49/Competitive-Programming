class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        j = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                nums[i] += 1
                j += 1
            elif nums[i] < nums[i-1]:
                j += (nums[i-1] - nums[i]) + 1
                nums[i] += (nums[i-1] - nums[i]) + 1
        return j
