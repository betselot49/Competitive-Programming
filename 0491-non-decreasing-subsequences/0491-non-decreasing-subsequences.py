class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.seen = set()
        
        def backtrack(idx, array):
            if len(array) > 1 and tuple(array) not in self.seen:
                self.result.append(array[:])
                self.seen.add(tuple(array))
            
            for i in range(idx, len(nums)):
                if len(array) == 0 or array[-1] <= nums[i]:
                    array.append(nums[i])
                backtrack(i+1, array[:])
                array.pop()
                
        backtrack(0, [])
        return self.result