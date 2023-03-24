class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        idx = 0
        while idx < len(nums):
            curr = nums[idx]
            nums[idx], nums[curr-1] = nums[curr-1], nums[idx]
            if idx+1 == nums[idx] or curr == nums[idx]:
                idx += 1

                
        duplicate = []
        for idx, num in enumerate(nums):
            if idx+1 != num:
                duplicate.append(idx+1)
        return duplicate