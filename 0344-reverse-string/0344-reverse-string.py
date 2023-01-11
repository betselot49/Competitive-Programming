class Solution:
    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1
     
        for i in range(len(s)//2):
            s[i], s[j-i] = s[j-i], s[i]
        
        return s