class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
     
        for left in range(len(s)//2):
            s[left], s[right-left] = s[right-left], s[left]
        
        return s