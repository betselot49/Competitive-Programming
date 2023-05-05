class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        word_map = Counter(words)
        for word in word_map:
            heapq.heappush(heap, (-word_map[word], word))
        
        return [heapq.heappop(heap)[1] for _ in range(k)]