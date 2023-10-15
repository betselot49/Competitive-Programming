# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def peak_finder():
            left = 0
            right = mountain_arr.length() - 1

            while left <= right:
                mid = (left + right) // 2
                l_num = mountain_arr.get(mid-1) if mid - 1 >= 0 else -1
                num = mountain_arr.get(mid)
                r_num = mountain_arr.get(mid+1) if mid + 1 < mountain_arr.length() else -1

                if l_num < num and num > r_num: return mid

                if l_num < num:
                    left = mid + 1
                else:
                    right = mid - 1
                
        def binarySearch_left(left, right, target):
            while left + 1 <  right:
                mid = (left + right) // 2
                curr =  mountain_arr.get(mid)
                if curr == target: return mid
                if curr < target:
                    left = mid
                else:
                    right = mid
                    
            if left >= 0 and mountain_arr.get(left) == target: return left
            if right < mountain_arr.length() and mountain_arr.get(right) == target: return right
            return -1
        
        def binarySearch_right(left, right, target):
            while left + 1 < right:
                mid = (left + right) // 2
                curr =  mountain_arr.get(mid)
                
                if curr == target: return mid
                if curr < target:
                    right = mid
                else:
                    left = mid
                    
            if left >= 0 and mountain_arr.get(left) == target: return left
            if right < mountain_arr.length() and mountain_arr.get(right) == target: return right
            return -1
        
        peak = peak_finder()
        left_part = binarySearch_left(0, peak, target)
        if left_part != -1: return left_part
        
        right_part = binarySearch_right(peak, mountain_arr.length() - 1, target)
        if right_part != -1: return right_part
        
        return -1

        