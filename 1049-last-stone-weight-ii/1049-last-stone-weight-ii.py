class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def balanced_diff(group1, group2, idx):
            if idx >= len(stones):
                return abs(group2 - group1)
            
            add_to_G1 = balanced_diff(group1 + stones[idx], group2, idx + 1)
            add_to_G2 = balanced_diff(group1, group2  + stones[idx], idx + 1)

            return min(add_to_G1, add_to_G2)
        
        return balanced_diff(0, 0, 0)
    
    
    # One liner
    def backtrack(G1, G2, i): return abs(G2 - G1) if i >= len(stones) else min(backtrack(G1 + stones[i], G2, i + 1), backtrack(G1, G2 + stones[i], i + 1))