class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        ans = ""
        while i < len(s):
            if len(s) > i + 2 and s[i+2] == '#':
                key = int(s[i: i+2])
                ans += chr(key+96)
                i += 3
            else:
                key = int(s[i])
                ans += chr(key+96)
                i += 1
        return ans
        