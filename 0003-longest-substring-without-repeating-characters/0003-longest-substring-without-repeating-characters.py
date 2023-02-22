class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = left = 0
        dic = defaultdict(int)
        for right, string in enumerate(s):
            if string in dic and dic[string] >= left:
                left = dic[string] + 1
                dic[string] = right
            max_len = max(max_len, right - left + 1)
            dic[string] = right
            
        return max_len