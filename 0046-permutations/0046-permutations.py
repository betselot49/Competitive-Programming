class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.seen = set()
        self.permutation = []
        def helper(nums, path):
            if len(path) == len(nums):
                self.permutation.append(path)
                return
            
            for num in nums:
                if num not in self.seen:
                    path.append(num)
                    self.seen.add(num)
                    helper(nums, path[:])
                    path.pop()
                    self.seen.remove(num)
        helper(nums, [])
        return self.permutation