class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            nums[i] = num * num
            
        nums.sort()
        return nums