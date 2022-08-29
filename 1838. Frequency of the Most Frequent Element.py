class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, 0
        total, maximum = 0, 0
        while right < len(nums):
            total += nums[right]
            while nums[right] * (right-left+1) > total + k:
                total -= nums[left]
                left += 1
            maximum = max(maximum, right-left+1)
            right += 1
        return maximum
