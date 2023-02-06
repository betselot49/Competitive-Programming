class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffle = []
        for i in range(len(nums) // 2):
            shuffle.append(nums[i])
            shuffle.append(nums[n+i])
            
        return shuffle