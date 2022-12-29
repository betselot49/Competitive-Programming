class Solution:
    def removeComments(self, source: List[str]) -> List[str]:       
    
        joined = "#".join(source)
        stack = []
        ans = []
        pointer = 0
        
        while pointer < len(joined):
            if joined[pointer] == "/":
                if joined[pointer + 1] == "/":
                    if stack:
                        ans.append("".join(stack))
                    stack = []
                    while pointer < len(joined) and joined[pointer] != "#":
                        pointer += 1
                elif joined[pointer + 1] == "*":
                    pointer += 2
                    while pointer < len(joined):
                        if joined[pointer] == "*" and joined[pointer + 1] == "/":
                            break
                        pointer += 1
                    pointer += 2
                else:
                    stack.append(joined[pointer])
                    pointer += 1
            
            elif joined[pointer] == "#":
                if stack:
                    ans.append("".join(stack))
                stack = []
                pointer += 1
            
            else:
                stack.append(joined[pointer])
                pointer += 1
            
        if stack:
            ans.append("".join(stack))
        return ans
    
        
        
                        
        
        
        
  
                        
        
        