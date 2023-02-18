class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        seen = set()
        nums.sort()
        left = 0
        right = len(nums)-1
        while left < right:
            seen.add((nums[left] + nums[right])/2)
            left += 1
            right -= 1
            
        return len(seen)