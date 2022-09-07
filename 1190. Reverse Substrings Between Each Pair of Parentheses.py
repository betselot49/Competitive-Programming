class Solution:
    def reverseParentheses(self, s: str) -> str:
        i, j = 0, 0
        stack, counter = [], []
        while j < len(s):
            while j < len(s) and s[j] != ")":
                if s[j] == "(":
                    counter.append(j)
                j += 1
            if j == len(s):
                break
            i = counter.pop()
            sub = s[i+1:j]
            s = s[:i] + sub[::-1] + s[j+1:]
            j -= 1
        return s
