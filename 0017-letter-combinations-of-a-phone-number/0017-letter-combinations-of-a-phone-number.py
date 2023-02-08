class Solution:
    def combination(self, string1, string2):
        combination = []
        for str1 in string1:
            for str2 in string2:
                combination.append(str1+str2)
        return combination
    
    def letterCombinations(self, digits: str) -> List[str]:      
        numberLetter = { '2': ['a', 'b', 'c'] , '3': ['d', 'e', 'f'] , '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p','q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'], "": [] }
        if len(digits) < 2:
            return numberLetter[digits]
 
        combination = self.combination(numberLetter[digits[-2]], numberLetter[digits[-1]])
        index = len(digits) - 3
        while index >= 0:
            combination = self.combination(numberLetter[digits[index]], combination)
            index -= 1
            
        return combination

        
    
    
        
            
        
        