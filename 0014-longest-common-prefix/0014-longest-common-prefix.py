class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i, s in enumerate(strs[0]):
            for string in strs:
                if len(string) <= i or string[i] != s:
                    return ans
            ans += s
        return ans
            
        