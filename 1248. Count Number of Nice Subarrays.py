class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for index, num in enumerate(nums):
            if num % 2 == 0:
                nums[index] = 0
            else:
                nums[index] = 1
        count, pre_sum, ps_dict = 0, 0, {0: 1}
        for num in nums:
            pre_sum += num
            count += ps_dict.get(pre_sum - k, 0)
            ps_dict[pre_sum] = 1 + ps_dict.get(pre_sum, 0)
        return count
