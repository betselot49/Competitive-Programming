class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # holds the next numbers needed for each group
        next_number = defaultdict(list)
        for num in nums:
            if not next_number[num]:
                # the current number now needs a number greater than it self by one
                heappush(next_number[num+1], (1, [num]))
            else:
                # the number got its place so append it and add to the next_number on num+1 key
                length, new_member = heappop(next_number[num])
                new_member.append(num)
                heappush(next_number[num+1], (length+1, new_member))
    
        for value in list(next_number.values()):
            # check each group has more than or equal to 3 members
            for length, array in value:
                if length < 3: return False
        return True
                