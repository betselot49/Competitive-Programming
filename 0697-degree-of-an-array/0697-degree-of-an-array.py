class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree =  max(list(Counter(nums).values()))
        n = len(nums)
        counter = defaultdict(int)
        min_len = n
        left = right = 0
        while right < n:
            counter[nums[right]] += 1
            while counter[nums[right]] == degree:
                min_len = min(min_len, right - left + 1)
                counter[nums[left]] -= 1
                left += 1
            right += 1
                
        return min_len