class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        hash_map = {}
        
        # precompure needle and substring in hystack with length needle
        def preCompute(word):
            num = 0
            for i, char in enumerate(word):
                num += (ord(char) - 96) * (27 ** i)
            return num
        
        # add to the right if the string => word is a number representation not a string
        def add(word, char):
            word *= 27
            word += ord(char) - 96
            return word
        
        # remove from the left
        def remove(word, char, m):
            word -= (ord(char) - 96) * (27 ** m)
            return word
            
            
        first = preCompute(haystack[:m][::-1])
        needle = preCompute(needle[::-1]) 
        
        hash_map[0] = first
        # find the maching substring
        for i in range(0, len(haystack) - m):
            curr = remove(first, haystack[i], m-1)
            curr = add(curr, haystack[i+m])
            hash_map[i+1] = curr
            first = curr
            
        for i in range(len(haystack) - m + 1):
            if hash_map[i] == needle: return i
        
        return -1
          
