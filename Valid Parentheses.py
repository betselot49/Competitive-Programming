class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {')': '(', '}': '{', ']': '['}
        stack, i = [], -1
        for i in s:
            if i in bracket.values():
                stack.append(i)
            elif i in bracket.keys():
                if len(stack) != 0 and stack[len(stack) - 1] == bracket.get(i):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
