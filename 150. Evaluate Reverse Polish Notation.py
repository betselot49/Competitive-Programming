class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 3:
            return tokens.pop()
        
        def select(l, r, o):
            operators = {"+", "-", "/", "*"}
            if r in operators:
                r = select(tokens.pop(), l, r)
                l = tokens.pop()
                return select(l, r, o)
            elif l in operators:
                right = tokens.pop()
                left = tokens.pop()
                l = select(left, right, l)
                return select(l, r, o)
            else:
                if o == "+":
                    return int(l) + int(r)
                elif o == "-":
                    return int(l) - int(r)
                elif o == "*":
                    return int(l) * int(r)
                elif o == "/":
                    return int(int(l) / int(r))

        o = tokens.pop()
        r = tokens.pop()
        l = tokens.pop()
        return select(l, r, o)
                
