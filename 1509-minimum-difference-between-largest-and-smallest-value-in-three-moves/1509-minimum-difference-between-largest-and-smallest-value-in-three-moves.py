class Solution:
    def minDifference(self, arr: List[int]) -> int:
        if len(arr) <= 4: return 0 

        arr.sort()
        i, n = 0, len(arr) - 1
        min_diff = float("inf")
        for i in range(4):
            min_diff = min(min_diff, arr[n-3+i] - arr[i])
        return min_diff