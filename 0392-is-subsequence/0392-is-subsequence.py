class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer = 0
        for char in t:
            if pointer < len(s) and s[pointer] == char:
                pointer += 1
        return pointer == len(s)