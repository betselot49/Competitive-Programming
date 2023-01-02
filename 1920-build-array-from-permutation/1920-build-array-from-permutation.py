class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        
        for index in nums:
            ans[index] = nums[nums[index]]
            
        return ans