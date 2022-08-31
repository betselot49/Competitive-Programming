class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        fre = sorted(Counter(arr).values())
        total, i, count = 0, len(fre)-1, 0
        while total < len(arr) // 2:
            total += fre[i]
            i -= 1
            count += 1
        return count
