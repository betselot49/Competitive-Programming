class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        n = len(nums) - 1
        for _ in range(2):
            for ind, num in enumerate(nums[::-1]):
                while stack and stack[-1] <= num:
                    stack.pop()
                if stack:
                    ans[n-ind] = stack[-1] if ans[n-ind] == -1 else ans[n-ind]
                stack.append(num)
        return ans