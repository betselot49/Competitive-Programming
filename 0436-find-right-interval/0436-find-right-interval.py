class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        index_map = sorted([[interval[0], idx] for idx, interval in enumerate(intervals)])  
        return [self.search(index_map, target[1]) for target in intervals]
        
        
    def search(self, array, target):
        left = -1
        right = len(array)
        
        while left+1 < right:
            mid = left + (right - left) // 2
            
            if array[mid][0] >= target:
                right = mid
            else:
                left = mid
                
        right = -1 if right >= len(array) or array[right][0] < target else array[right][1]
        return right
        