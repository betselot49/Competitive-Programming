class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums = Counter(nums)
        twice = []
        for num in nums:
            if nums[num] == 2:
                twice.append(num)
                
        return twice
