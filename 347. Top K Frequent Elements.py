class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = sorted(Counter(nums).items(), key=lambda x : -x[1])
        i, output = 0, []
        while i < k:
            output.append(freq[i][0])
            i += 1
        return output
