class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        next_number = defaultdict(list)
        for num in nums:
            if not next_number[num]:
                heappush(next_number[num+1], (1, [num]))
            else:
                length, new_member = heappop(next_number[num])
                new_member.append(num)
                heappush(next_number[num+1], (length+1, new_member))
    
        for value in list(next_number.values()):
            for length, array in value:
                if length < 3: return False
        return True
                