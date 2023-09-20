class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def robber(i):
            if i >= len(nums): return 0
            take = nums[i] + robber(i+2)
            skip = max(robber(i+1), robber(i+2))
            return max(take, skip)
        return robber(0)