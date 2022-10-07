class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        i, j, count, maxVowel = 0, 0, 0, 0
        while j < k:
            if s[j] in vowels:
                count += 1
            j += 1
        maxVowel = max(maxVowel, count)
            
        while j < len(s):
            if s[i] in vowels:
                count -= 1
            if s[j] in vowels:
                count += 1
            i += 1
            j += 1
            
            maxVowel = max(maxVowel, count)
        return maxVowel
