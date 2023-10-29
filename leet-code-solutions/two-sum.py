class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Follow-up --> O(N) 
        look_back = {}
        for idx, num in enumerate(nums):
            if num in look_back: return [idx, look_back[num]]
            look_back[target - num] = idx