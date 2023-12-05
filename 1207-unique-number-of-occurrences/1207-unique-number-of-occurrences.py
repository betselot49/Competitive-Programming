class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        fre = Counter(arr).values()
        return len(fre) == len(set(fre))