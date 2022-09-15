class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = ['0']
        for j in range(len(num)):
            if len(stack) == 0:
                stack.append(num[j])
            elif num[j] >= stack[-1]:
                stack.append(num[j])
            else:
                while len(stack) > 0 and k > 0 and stack[-1] > num[j]:
                    stack.pop()
                    k -= 1
                stack.append(num[j])
        while k > 0:
            stack.pop()
            k -= 1
        
        return str(int(''.join(stack)))
                
