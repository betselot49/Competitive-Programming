class Solution(object):
    def missingNumber(self, nums):
        ans = 0
        for i in range(1, len(nums)+1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans
        