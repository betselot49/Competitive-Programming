class Solution:
    def operate(self, l, o, r):
        if o == '+':
            return str(int(l) + int(r))
        elif o == '-':
            return str(int(l) - int(r))
        elif o == '*':
            return str(int(l) * int(r))
        elif o == '/':
            return str(int(l) // int(r))

    def calculate(self, s: str) -> int:
        stack = []
        i = 1
        op1 = ['*', '/']
        op2 = ['+', '-']
        num = s[0]
        while i < len(s):
            if s[i] not in op1 + op2:
                num += s[i]
                i += 1
            elif s[i] in op1 or op2:
                if len(stack) > 0 and stack[-1] in op1:
                    r = num
                    o = stack.pop()
                    l = stack.pop()
                    num = self.operate(l, o, r)
                stack.append(num)
                num = ''
                stack.append(s[i])
                i += 1
        if len(stack) > 0 and stack[-1] in op1:
            r = num
            o = stack.pop()
            l = stack.pop()
            num = self.operate(l, o, r)
        stack.append(num)

        l = stack[0]
        if len(stack) > 1:
            i = 1
            while i < len(stack):
                l = self.operate(l, stack[i], stack[i + 1])
                i += 2

        return str(int(l))
