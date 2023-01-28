class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums[0] = str(nums[0])
        for i in range(len(nums) - 1):
            nums[i] = str(nums[i])
            for j in range(i + 1, len(nums)):
                nums[j] = str(nums[j])
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return str(int("".join(nums)))