class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        array = [[]]
        def backtrack(ind):
            if ind == len(nums) - 1:
                array.append([nums[ind]])
                return array
            
            sub_sets = backtrack(ind+1).copy()
            for sub_set in sub_sets:
                curr = sub_set.copy()
                curr.append(nums[ind])
                array.append(sorted(curr))
            return array
        
        return backtrack(0)
    
  