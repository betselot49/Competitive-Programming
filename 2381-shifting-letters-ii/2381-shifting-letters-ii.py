class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        alpha_num = {chr(i+97): i for i in range(0, 26)}
        num_alpha = {i: chr(i+97) for i in range(0, 26)}
        new_str = ""
        
        mapping = [0] * len(s)
        for shift in shifts:
            constant = 1 if shift[2] else -1
            mapping[shift[0]] += constant
            if shift[1] < (len(s)-1):
                mapping[shift[1]+1] -= constant
        
        for i in range(1, len(mapping)):
            mapping[i] += mapping[i-1]
        
        for index, num in enumerate(mapping):
            newVal = alpha_num[s[index]] + num
            new_str += num_alpha[newVal % 26]
    
        return new_str
    
                