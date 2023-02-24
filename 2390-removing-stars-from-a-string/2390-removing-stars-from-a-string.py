class Solution:
    def removeStars(self, s: str) -> str:
        strStack = []
        for char in s:
            strStack.pop() if char == "*" else strStack.append(char)        
        return "".join(strStack)