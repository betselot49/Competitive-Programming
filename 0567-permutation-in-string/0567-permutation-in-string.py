class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        k = len(s1)
        i = 0
    
        while i < len(s2) and s2[i] not in counter:
            i += 1
          
        j = i
        while i < len(s2):
            if i >= j:
                j = i
            while j < len(s2) and counter[s2[j]] > 0:
                counter[s2[j]] -= 1
                j += 1
                if j - i == k:
                    return True
            if s2[i] in counter:
                counter[s2[i]] += 1
            i += 1
            
            while i < len(s2) and s2[i] not in counter:
                i += 1

        return False
    
                    

            