class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indexHolder = defaultdict(int)
        numIndexPair = defaultdict(int)

        for index, num in enumerate(nums):
            numIndexPair[index] = num
            indexHolder[num] = index

        for operation in operations:
            index = indexHolder[operation[0]]
            numIndexPair[index] = operation[1]
            indexHolder[operation[1]] = index

        for index, num in numIndexPair.items():
            nums[index] = num

        return nums

        
            
        