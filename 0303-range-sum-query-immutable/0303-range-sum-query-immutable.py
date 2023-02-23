class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.preSum = [0]
        curSum = 0
        for num in nums:
            curSum += num
            self.preSum.append(curSum)

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right + 1] - self.preSum[left]