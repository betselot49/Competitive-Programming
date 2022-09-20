class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_window, i, j = 0, 0, 0
        while j < len(nums):
            if nums[j] == 1:
                j += 1
            elif nums[j] == 0 and k > 0:
                j += 1
                k -= 1
            else:
                max_window = max(max_window, j - i)
                while nums[i] == 1:
                    i += 1
                i += 1
                k += 1
        return(max(max_window, j - i))
