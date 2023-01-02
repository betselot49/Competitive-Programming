class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        left = 0
        ans = []
        for right in spaces:
            ans.append(s[left: right])
            left = right
       
        ans.append(s[left:])
        return " ".join(ans)
            