class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        compare = float("inf")
        two_arr = [nums[0]]   # this array contain atmost two element in it
        
        for num in nums[1:]:
            if compare < num: return True
            
            if len(two_arr) == 1:
                if two_arr[0] >= num:
                    two_arr = [num]
                else:
                    two_arr.append(num)
                    compare = min(compare, num)
            else:
                two_arr.pop()
                if two_arr[0] < num:
                    compare = min(compare, num)
                    two_arr.append(num)
                else:
                    two_arr = [num]
        return False
                
            