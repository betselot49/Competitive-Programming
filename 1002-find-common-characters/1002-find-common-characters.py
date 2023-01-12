class Solution:
    def counter(self, word):
        asciiList = [0] * 26
        for char in word:
            asciiList[ord(char) - 97] += 1

        return asciiList
    
    
    def commonChars(self, words: List[str]) -> List[str]:
        asciiList = self.counter(words[0]) 
        for word in words[1:]:
            temp = self.counter(word)
            for index, num in enumerate(temp):
                asciiList[index] = min(num, asciiList[index])
            
        duplicate = []
        for index, num in enumerate(asciiList):
            if num:
                for i in range(num):
                    duplicate.append(chr(index + 97))
        return duplicate
        
        
        
        