class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = []
        seen = set()
        def backtrack(perm, path):
            if len(perm) == len(nums):
                if tuple(perm) not in seen:
                    seen.add(tuple(perm))
                    answer.append(perm)
                return
                
            for i in range(len(nums)):
                if i not in path:
                    path.add(i)
                    perm.append(nums[i])
                    backtrack(perm.copy(), path.copy())
                    path.remove(i)
                    perm.pop()
                    
        backtrack([], set())
        return answer
    
    
    