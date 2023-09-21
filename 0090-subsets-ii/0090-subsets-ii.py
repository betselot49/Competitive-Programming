class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans, seen = [], set()
        
        def backtrack(idx, temp):
            if tuple(temp) not in seen:
                ans.append(temp[:])
                seen.add(tuple(temp[:]))
            
            for i in range(idx, len(nums)):
                temp.append(nums[i])
                backtrack(i+1, temp[:])
                temp.pop()
                
        backtrack(0, [])
        return ans
                