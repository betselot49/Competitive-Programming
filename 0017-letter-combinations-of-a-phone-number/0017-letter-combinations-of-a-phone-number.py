class Solution:
    def combination(self, string1, string2):
        combination = []
        for str1 in string1:
            for str2 in string2:
                combination.append(str1+str2)
        return combination
    
    def letterCombinations(self, digits: str) -> List[str]:      
        numberLetter = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz',"":[] }
        if len(digits) < 2:
            return list(numberLetter[digits])
 
        combination = self.combination(numberLetter[digits[-2]], numberLetter[digits[-1]])
        index = len(digits) - 3
        while index >= 0:
            combination = self.combination(numberLetter[digits[index]], combination)
            index -= 1
            
        return combination

        
    
    
        
            
        
        