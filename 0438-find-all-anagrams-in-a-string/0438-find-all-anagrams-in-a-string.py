class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        i, j, ans = 0, 0, [] 
        c = Counter(p)
        
        while j < len(s):
            if c.get(s[j], 0) > 0:
                var = {s[j]: -1}
                c.update(var)
                j += 1
                if j - i == len(p):
                    ans.append(i)
                    var = {s[i]: +1}
                    c.update(var)
                    i += 1
            else:
                while s[i] != s[j]:
                    var = {s[i]: +1}
                    c.update(var)
                    i += 1
                j += 1
                i += 1

        return(ans)
     
        
        """
        ------- brute force sollution -------------------   
   
        i, j, res, sortedp = 0, len(p) - 1, [], sorted(p)
        
        while j < len(s):
            if sorted(s[i:j+1]) == sortedp:
                res.append(i)
            i += 1
            j += 1
        return res
        
        """
        
        
    
    