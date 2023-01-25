class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinct = set()
        for num in nums:
            stringNum = str(num)[::-1]
            distinct.add(num)
            distinct.add(int(stringNum))

        return len(distinct)
            
