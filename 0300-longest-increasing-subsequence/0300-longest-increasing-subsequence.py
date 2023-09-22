class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp, N = {}, len(nums)
        max_sub_sequence = 1
        for i in range(N-1, -1, -1):
            local_max = 1
            for j in range(i + 1, N):
                if nums[i] < nums[j]:
                    local_max = max(local_max, 1 + dp[j])
            dp[i] = local_max
            max_sub_sequence = max(max_sub_sequence, local_max)
        return max_sub_sequence