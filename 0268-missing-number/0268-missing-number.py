class Solution:
    def missingNumber(self, array: List[int]) -> int:
        idx = 0
        while idx < len(array):
            if array[idx] == -1: return idx
            
            curr = array[idx]    
            if array[idx] == len(array) or array[curr] == -1:
                array[idx], array[curr-1] = array[curr-1], -1
            elif idx != array[idx]:
                array[curr], array[idx] = array[idx], array[curr]
            
            if idx == array[idx]:
                idx += 1
        
        return idx