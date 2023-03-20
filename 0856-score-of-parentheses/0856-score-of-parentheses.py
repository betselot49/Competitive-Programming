class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == ")":
                print(stack)
                if isinstance(stack[-1], int):
                    curr_score = 2 * stack.pop()
                    stack.pop()
                    while stack and isinstance(stack[-1], int):
                        curr_score += stack.pop()
                    stack.append(curr_score)
                else:
                    stack.pop()
                    curr_score = 1
                    while stack and isinstance(stack[-1], int):
                        curr_score += stack.pop()
                    stack.append(curr_score)
            else:
                stack.append(ch)
        return stack[0]