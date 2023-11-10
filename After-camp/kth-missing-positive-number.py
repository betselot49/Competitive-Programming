class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k: return k
        k -= arr[0] - 1
        
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff > k:
                return arr[i-1] + k
            else:
                k -= (diff - 1)
        
        return arr[-1] + k
        