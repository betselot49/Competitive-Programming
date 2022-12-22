class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        numDict = {str(i): i for i in range(10)}
        newNum1, newNum2 = 0, 0
        for n1 in num1:
            newNum1 = (newNum1 * 10) + numDict[n1]
        for n2 in num2:
            newNum2 = (newNum2 * 10) + numDict[n2]
        return str(newNum1 * newNum2)
        
        
        
        