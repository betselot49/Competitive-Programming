class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        cur_sum = 0
        left = 0
        res = [-1] * len(nums)
        for right, num in enumerate(nums):
            cur_sum += num
            if right - left == 2 * k:
                res[left + k] = cur_sum // (2 * k + 1)
                cur_sum -= nums[left]
                left += 1
                
        return res