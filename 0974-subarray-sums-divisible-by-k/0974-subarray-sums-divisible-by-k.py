class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        modulo = defaultdict(int)
        modulo[0], counter, total = 1, 0, 0
        for num in nums:
            total += num
            counter += modulo[total%k]
            modulo[total%k] += 1
        return counter