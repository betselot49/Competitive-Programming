class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pair_sum, l = 0, len(nums)
        for i in range(l//2):
            if nums[i] + nums[l-1-i] > max_pair_sum:
                max_pair_sum = nums[i] + nums[l-1-i]
        return max_pair_sum
