class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        i = 0
        j = 0
        cur_sum = 0
        length = len(nums)
        while j < len(nums):
            cur_sum += nums[j]
            if cur_sum < target:
                j += 1
            else:
                while cur_sum - nums[i] >= target:
                    cur_sum -= nums[i]
                    i += 1
                length = min(length, j - i + 1)
                if length == 1:
                    return length
                j += 1
        return length
                