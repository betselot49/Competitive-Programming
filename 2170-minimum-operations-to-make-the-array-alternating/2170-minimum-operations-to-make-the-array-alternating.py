class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        
        odd_c = defaultdict(int)
        even_c = defaultdict(int)
        
        odds = evens = 0
        
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_c[num] += 1
                evens += 1
            else:
                odd_c[num] += 1
                odds += 1
               
        first_odd = sec_odd = first_even = second_even = (-1, 0)
        odd_c = sorted(odd_c.items(), key=lambda x : x[1], reverse = True)
        even_c = sorted(even_c.items(), key=lambda x : x[1], reverse = True)
        
        odd_c.append((-1, 0))
        even_c.append((-1, 0))
        
        if odd_c[0][0] != even_c[0][0]:
            return (odds - odd_c[0][1]) + (evens - even_c[0][1])
        
        return min((odds - odd_c[0][1]) + (evens - even_c[1][1]), (odds - odd_c[1][1]) + (evens - even_c[0][1]))
        