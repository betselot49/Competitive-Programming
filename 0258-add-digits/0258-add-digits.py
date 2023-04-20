class Solution:
    def addDigits(self, num: int) -> int:
        # while num > 9:
        #     total = 0
        #     while num > 0:
        #         total += num % 10
        #         num //= 10
        #     num = total
        # return num
        return 9 if num and num % 9 == 0 else num % 9