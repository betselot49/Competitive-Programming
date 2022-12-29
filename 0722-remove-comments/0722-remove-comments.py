class Solution:
    def removeComments(self, source: List[str]) -> List[str]:       
        """
        ["     /*Test program */     ", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a
                i
        
        test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
        
       
       
       
       stack =  [' ', ' ', ' ', /, ]
       
       if /, check if next is / then move your pointer until you get #
       if /, and next is * move your pointer until you find * and next /
       if # and stack[-1] is not / push to answer
       
       iterate through the source,  
       
       """
        
        
        
        """
joined = "     /*Test program       #int main()#{ #   variable  */ declaration #int a, b, c;#/* This is a test#   multiline  #   comment for #   testing */#a = b + c;#}
"
        """
    
        joined = "#".join(source)
        stack = []
        ans = []
        pointer = 0
        print(joined)        

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
    
        
        
                        
        
        
        
  
                        
        
        