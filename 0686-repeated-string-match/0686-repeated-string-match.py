class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:    
        lps = [0]
        i = 0
        j = 1
        while j < len(b):
            if i == 0 and b[i] != b[j]:
                lps.append(0)
                j += 1
            elif b[i] == b[j]:
                lps.append(i + 1)
                i += 1
                j += 1
            else:
                i = lps[i - 1]
                
        turn = 1
      
        a_i = b_i = 0
        while a_i < len(a):
            if a[a_i] != b[b_i] and turn > 2: return -1
            
            if a[a_i] == b[b_i]:
                a_i += 1
                b_i += 1
            elif b_i == 0:
                a_i += 1
            else:
                b_i = lps[b_i - 1]
                
            if b_i == len(b): return turn 
            if a_i == len(a):
                a_i = 0
                turn += 1
                
        return -1