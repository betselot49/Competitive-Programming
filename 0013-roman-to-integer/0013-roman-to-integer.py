class Solution(object):
    def romanToInt(self, s):
        romanNumerals = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "": 0 }
        holder = ""
        number = 0
        for roman in s[::-1]:
            if holder == "":
                holder = roman
            elif romanNumerals[holder] > romanNumerals[roman]:
                number += romanNumerals[holder] - romanNumerals[roman]
                holder = ""
            else:
                number += romanNumerals[holder]
                holder = roman
            print(holder)
        return number + romanNumerals[holder]  
        
        