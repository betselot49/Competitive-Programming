class Solution:
    def isPalindrome(self, s: str) -> bool:
        simple = ""
        for char in s:
            if char.isalnum():
                simple += char.lower()
        
        print(simple)
        
        i = 0
        j = len(simple) - 1
        while i <= j:
            if simple[i] != simple[j]:
                return False
            i += 1
            j -= 1
                
        return True