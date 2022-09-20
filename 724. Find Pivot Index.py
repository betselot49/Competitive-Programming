class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        pivot_index = -1
        i = 0
        while i < len(nums) and left_sum != right_sum - nums[i]:
            left_sum += nums[i]
            right_sum -= nums[i]
            i += 1
        if i != len(nums):
            pivot_index = i
        return pivot_index
