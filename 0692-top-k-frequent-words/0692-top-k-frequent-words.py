class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        for key, value in list(count.items()):
            heappush(heap, (-value, key))
        return [heappop(heap)[1] for _ in range(k)]
        