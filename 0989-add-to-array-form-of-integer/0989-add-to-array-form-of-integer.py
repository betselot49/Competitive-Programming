class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = 0
        k = str(k)
        ind1 = len(num)-1
        ind2 = len(k)-1
        total = []
        while ind1 >= 0 or ind2 >= 0:
            val1 = int(k[ind2]) if ind2 >= 0 else 0
            val2 = int(num[ind1]) if ind1 >= 0 else 0
            curSum = val1 + val2 + carry
            total.append(curSum % 10)
            carry = curSum // 10
            ind1 -= 1
            ind2 -= 1
            
        if carry:
            total.append(carry)
        return total[::-1]