class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 == 0:
            quotient = num // 3
            return [quotient - 1, quotient, quotient + 1]
        return []