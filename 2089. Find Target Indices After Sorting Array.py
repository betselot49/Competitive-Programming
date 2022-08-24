from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            index = i
            for j in range(i + 1, len(nums)):
                if nums[index] > nums[j]:
                    index = j
            nums[i], nums[index] = nums[index], nums[i]
            if target == nums[i]:
                output.append(i)
        return output
