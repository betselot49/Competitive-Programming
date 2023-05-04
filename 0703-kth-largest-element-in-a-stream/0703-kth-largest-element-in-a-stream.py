class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        heapify(nums)
        while len(nums) > k:
            heappop(nums)
        self.nums = nums
        self.k = k
        print()

    def add(self, val: int) -> int:
        heappush(self.nums, val)
        if(len(self.nums) > self.k): heappop(self.nums)
            
        return self.nums[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)