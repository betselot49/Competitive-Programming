class Solution:   
    def splitString(self, s: str) -> bool:
        
        array = []
        def checker(ind):
            if ind >= len(s):
                return len(array) >= 2
            
            for i in range(ind, len(s)):
                curr = int(s[ind:i+1])
                if len(array) == 0 or array[-1] - curr == 1:
                    array.append(curr)
                    if checker(i+1):
                        return True
            
                    array.pop()
           
            return False
        
        return checker(0)
                    
            
                    