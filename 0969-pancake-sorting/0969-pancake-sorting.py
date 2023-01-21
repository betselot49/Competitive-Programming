class Solution:
    def flip(self, l, r):
        l.reverse()
        return l + r
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        flips = []
        for i in range(n, 0, -1):
            for j in range(0, i):
                if arr[j] == i:
                    arr = self.flip(arr[:j+1], arr[j+1:])
                    flips.append(j+1)
                    break
            arr = self.flip(arr[:i], arr[i:])
            flips.append(i)
        return flips
                    