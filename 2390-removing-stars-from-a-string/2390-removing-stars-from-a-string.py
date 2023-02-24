class Solution:
    def removeStars(self, s: str) -> str:
        strStack = []
        for char in s:
            strStack.append(char)
            if strStack[-1] == "*":
                strStack.pop()
                strStack.pop()
                
        return "".join(strStack)