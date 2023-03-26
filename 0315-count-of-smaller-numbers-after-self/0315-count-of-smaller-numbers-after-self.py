class Solution(object):
    def divide(self, nums):
        if len(nums) < 2:
            return nums
        mid = len(nums) // 2
        left = self.divide(nums[:mid])
        right = self.divide(nums[mid:])

        return self.mergeEval(left, right)
    
    def mergeEval(self, left, right):
        idx1, idx2, merged = 0, 0, []
     
        while idx1 < len(left) and idx2 < len(right):
            if right[idx2][0] < left[idx1][0]:
                merged.append(right[idx2])
                idx2 += 1
            else:
                merged.append(left[idx1])
                self.ans[left[idx1][1]] += idx2
                idx1 += 1
                
        while idx1 < len(left):
            merged.append(left[idx1])
            self.ans[left[idx1][1]] += idx2
            idx1 += 1
        merged.extend(right[idx2:])
       
        return merged
            
    def countSmaller(self, nums):
        for idx, num in enumerate(nums):
            nums[idx] = [num, idx]
    
        self.ans = [0] * len(nums)
        self.divide(nums)
        return self.ans
        
        
        
                    