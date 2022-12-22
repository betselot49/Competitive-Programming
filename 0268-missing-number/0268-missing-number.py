class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        Set = { i for i in nums }
        print(Set)
        for i in range(len(nums)+1):
            if i not in Set:
                return i