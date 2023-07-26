class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)
        count = Counter(nums)
        for key, value in list(count.items()):
            if value > N // 2: return key