class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output, total, prefix_sum = 0, 0, {0:1}
        for num in nums:
            total += num
            difference = total - k
            output += prefix_sum.get(difference, 0)
            prefix_sum[total] = 1 + prefix_sum.get(total, 0)
        return output
    
