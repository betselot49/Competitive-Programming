class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left = 0
        maxFre = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxFre = max(maxFre, count[s[right]])
            
            while (right - left + 1) - maxFre > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res