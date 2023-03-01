class Solution:
    def decoder(self, encoded, index, stack):
        if index == len(encoded):
            return stack[0]
        
        if encoded[index].isnumeric():
            number = encoded[index]
            if stack[-1].isnumeric():
                stack[-1] += number
            else:
                stack.append(encoded[index])
        elif encoded[index] == "[":
            stack.append("")
        elif encoded[index] == "]":
            word = stack.pop()
            number = int(stack.pop())
            stack[-1] += word * number
        else:
            stack[-1] += encoded[index]
            
        return self.decoder(encoded, index+1, stack)
        
        
    def decodeString(self, s: str) -> str:
        stack = [""]
        return self.decoder(s, 0, stack)
        