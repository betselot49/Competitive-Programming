class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        count = 0
        for j in range(N - 1, 1, -1):
            i = 0
            k = j - 1
            while i < k:
                if nums[i] + nums[k] > nums[j]:
                    count += k - i
                    k -= 1
                else:
                    i += 1
        return count
                    