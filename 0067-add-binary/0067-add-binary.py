class Solution:
    def addBinary(self, a: str, b: str) -> str:
        indexA = len(a) - 1
        indexB = len(b) - 1
        binarySum = ""
        carry = 0
        while indexA >= 0 or indexB >= 0:
            val1 = int(a[indexA]) if indexA >= 0 else 0
            val2 = int(b[indexB]) if indexB >= 0 else 0
            curSum = val1 + val2 + carry
            binarySum = str(curSum%2) + binarySum
            carry = curSum // 2
            indexA -= 1
            indexB -= 1
            
        if carry:
            binarySum = str(carry) + binarySum
        return binarySum
            