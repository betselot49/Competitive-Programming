class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def balanced_diff(group1, group2, idx):
            return abs(group2 - group1) if idx >= len(stones) else min(balanced_diff(group1 + stones[idx], group2, idx + 1), balanced_diff(group1, group2 + stones[idx], idx + 1))
        return balanced_diff(0, 0, 0)