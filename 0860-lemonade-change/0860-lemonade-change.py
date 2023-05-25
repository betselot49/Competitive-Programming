class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        
        for bill in bills:
            if bill == 20:
                if tens and fives:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
                
            elif bill == 10:
                tens += 1
                
                if fives:
                    fives -= 1
                else:
                    return False
            else:
                fives += 1
                
        return True