class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list2 = {char:i for i, char in enumerate(list2)}
        dic = {}
        min_sum = float("inf")
        for i, char in enumerate(list1):
            if char in list2:
                curr = i + list2[char]
                dic[char] = curr
                min_sum = min(min_sum, curr)
                
        output = []
        for key, value in list(dic.items()):
            if value == min_sum:
                output.append(key)
                
        return output
   