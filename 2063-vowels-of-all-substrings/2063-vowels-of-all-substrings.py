class Solution:
    def countVowels(self, word: str) -> int:
        vwl_sbstrg = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        for i, char in enumerate(word):
            if char in vowels:
                vwl_sbstrg += (i + 1) * (len(word) - i)
                
        return vwl_sbstrg