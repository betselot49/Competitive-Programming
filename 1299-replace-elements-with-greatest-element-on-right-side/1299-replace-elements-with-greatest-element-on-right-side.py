class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = -1
        for index in range(len(arr)-1, -1, -1):
            cur = arr[index]
            arr[index] = maxi
            maxi = max(maxi, cur)
        return arr
            