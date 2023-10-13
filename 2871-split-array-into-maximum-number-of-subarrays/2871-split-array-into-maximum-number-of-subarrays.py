class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        run_and = -1 # All bits are 1
        counter = 0
        for num in nums:
            run_and &= num
            if run_and == 0:
                counter += 1
                run_and = -1
         
        return max(1, counter)