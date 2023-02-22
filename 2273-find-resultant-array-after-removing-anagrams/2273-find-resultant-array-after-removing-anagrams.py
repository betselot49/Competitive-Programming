class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        left = right = 0
        anagram = []
        while right < len(words):
            leftCount = Counter(words[left])
            while right < len(words) and leftCount == Counter(words[right]):
                right += 1
            anagram.append(words[left])
            left = right
            
        return anagram
                
            
            