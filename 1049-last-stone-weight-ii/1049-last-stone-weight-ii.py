class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def balanced_diff(G1, G2, i):
            # min ( add to G1, add to G2 ) 
            return abs(G2 - G1) if i >= len(stones) else min(balanced_diff(G1 + stones[i], G2, i + 1), balanced_diff(G1, G2 + stones[i], i + 1))
        return balanced_diff(0, 0, 0)