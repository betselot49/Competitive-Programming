class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums = Counter(nums)
        ans = []
        for num in nums:
            if nums[num] == 2:
                ans.append(num)
                
        return ans
