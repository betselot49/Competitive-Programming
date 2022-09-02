class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        mapped = list(map(lambda x : int(x), nums))
        mapped.sort()
        return str(mapped[len(nums) - k])
