class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick(pivot, end, target):
            write = pivot + 1
            for read in range(pivot+1, end):
                if nums[read] <= nums[pivot]:
                    nums[read], nums[write] = nums[write], nums[read]
                    write += 1
                    
            nums[write-1], nums[pivot] =  nums[pivot], nums[write-1]
            
            if target == write - 1:
                return nums[target]
            
            if target > write - 1:
                return quick(write, end, target)
            else:
                return quick(pivot, write-1, target)
            
        return quick(0, len(nums), len(nums)-k)
                