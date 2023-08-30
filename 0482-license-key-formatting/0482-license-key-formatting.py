class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = "".join(s.split("-"))
        idx = len(s) - 1
        temp = ""
        ans = []
        while idx >= 0:
            temp = s[idx].upper() + temp
            
            if len(temp) == k:
                ans.append(temp)
                temp = ""
                
            idx -= 1
        
        if temp:
            ans.append(temp)
            
        ans.reverse()
        return "-".join(ans)