class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curSum = sum(arr[:k])
        count = 0
        if curSum / k >= threshold:
            count += 1
            
        i, j = 0, k
        while j < len(arr):
            curSum = curSum - arr[i] + arr[j]
            if curSum / k >= threshold:
                count += 1
            j += 1 
            i += 1
        return count
            
