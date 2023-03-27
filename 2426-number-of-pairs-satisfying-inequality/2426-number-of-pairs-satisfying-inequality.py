class Solution(object):
    def numberOfPairs(self, nums1, nums2, diff):
        self.diff = diff
        self.pairs = 0
        nums = self.arrayGenerate(nums1, nums2)
        self.divide(nums)
        return self.pairs
        
    def divide(self, array):
        if len(array) < 2:
             return array

        left = self.divide(array[:len(array)//2])
        right = self.divide(array[len(array)//2:])

        return self.merger(left, right)
        
    def merger(self, left, right):
        idx2 = 0
        for num in left:
            while idx2 < len(right) and num - right[idx2] > self.diff:
                idx2 += 1
            self.pairs += len(right) - idx2

        idx1, idx2, merged = 0, 0, []
        while idx1 < len(left) and idx2 < len(right):
            if left[idx1] <= right[idx2]:
                merged.append(left[idx1])
                idx1 += 1
            else:
                merged.append(right[idx2])
                idx2 += 1

        merged.extend(left[idx1:])
        merged.extend(right[idx2:])
        
        return merged
    
    def arrayGenerate(self, left, right):
        new_array = []
        for idx in range(len(left)):
            new_array.append(left[idx]-right[idx])
            idx += 1
        return new_array
            
     
            
                
            
            