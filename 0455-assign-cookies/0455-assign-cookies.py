class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        idxG = idxS = count = 0
        while idxG < len(g) and idxS < len(s):
            if g[idxG] <= s[idxS]:
                count += 1
                idxG += 1
                idxS += 1
            else:
                idxS += 1
        return count