class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dic = set()
        for num in arr:
            if num * 2 in dic or num / 2 in dic:
                return True
            dic.add(num)
        return False