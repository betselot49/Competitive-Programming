class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = defaultdict(int)
        pre_sum[0], total, sub_arrays = 1, 0, 0
        for num in nums:
            total += num
            sub_arrays += pre_sum[total - k]
            pre_sum[total] += 1
        return sub_arrays