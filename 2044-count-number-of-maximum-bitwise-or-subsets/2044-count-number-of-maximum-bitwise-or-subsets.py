class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.max_or = 0
        self.sub_set = defaultdict(int)
        def backtrack(idx, path):
            if idx > len(nums): return 
            if len(path) > 0:
                OR = path[0]
                for num in path[1:]:
                    OR |= num
                self.max_or = max(self.max_or, OR)
                self.sub_set[OR] += 1
            
            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path[:])
                path.pop()
                
        backtrack(0, [])
        return self.sub_set[self.max_or]
                