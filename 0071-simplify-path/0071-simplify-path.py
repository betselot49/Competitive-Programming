class Solution:
    def simplifyPath(self, path: str) -> str:        
        simplified = path.split("/")
                
        stack = []
        for path in simplified:
            if path == "." or path == "":
                continue 
            elif path == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append("/" + path)
        
        if not stack:
            stack.append("/")
            
        return "".join(stack)
    