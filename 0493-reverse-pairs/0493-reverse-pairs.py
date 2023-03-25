class Solution(object):
    def __init__(self):
        self.reverse_pair = 0
        
    def divide_conquer(self, array):
        if len(array) < 2: return array

        low, high = 0, len(array)
        mid = low + (high - low) // 2

        left = self.divide_conquer(array[:mid])
        right = self.divide_conquer(array[mid:])

        self.reversePairCalculate(left, right)
        return self.merger(left, right)
    
    def merger(self, left, right):
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

    def reversePairCalculate(self, left, right):
        idx2 = 0
        for idx1, num in enumerate(left):
            while idx2 < len(right) and num > right[idx2] * 2:
                idx2 += 1
            self.reverse_pair += idx2
        
        
    def reversePairs(self, nums):
        self.divide_conquer(nums)
        return self.reverse_pair
        
        