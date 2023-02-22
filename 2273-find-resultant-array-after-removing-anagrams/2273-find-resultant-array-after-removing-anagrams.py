class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        left = right = 0
        anagram = []
        while right < len(words):
            while right < len(words) and Counter(words[left]) == Counter(words[right]):
                right += 1
            anagram.append(words[left])
            left = right
            
        return anagram
                
            
            