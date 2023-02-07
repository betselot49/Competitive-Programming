class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i, j = 0, 0
        while j < len(fruits) and fruits[i] == fruits[j]:
            j += 1
        maxi = j - i
        while j < len(fruits):
            first_basket = fruits[i]
            second_basket = fruits[j]
            temp = j
            while j < len(fruits) and (fruits[j] == first_basket or fruits[j] == second_basket):
                if fruits[j] != fruits[temp]:
                    temp = j
                j += 1

            maxi = max(maxi, j - i)
            i = temp
        return max(maxi, j - i)