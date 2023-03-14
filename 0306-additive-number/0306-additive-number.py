class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        array = []
        def additive(ind):
            if ind >= len(num): 
                return len(array) >= 3
            
            for i in range(ind, len(num)):
                curr = num[ind: i+1]
                if (len(str(int(curr))) == len(curr) and   # checks for leading zeros except for the number zero itself alone
                   (len(array) < 2 or array[-1] + array[-2] == int(curr))):  # cheks the sum of last two numbers == curr 
                    array.append(int(curr))
                    
                    if additive(i+1):
                        return True
                    
                    array.pop()
            return False
        
        return additive(0)
