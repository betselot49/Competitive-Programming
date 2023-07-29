class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        dic = Counter(stones)
        for jewel in jewels:
            if jewel in dic:
                count += dic[jewel]
                dic[jewel] = 0
        return count