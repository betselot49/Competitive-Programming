class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splited = s.split(" ")
        for s in splited[: : -1]:
            if s:
                return len(s)