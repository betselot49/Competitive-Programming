class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = -1
        high = len(citations)
        
        while low + 1 < high:
            mid = low + (high - low) // 2
            
            if citations[mid] >= len(citations[mid:]):
                high = mid
            else:
                low = mid
            
        return len(citations[high:])