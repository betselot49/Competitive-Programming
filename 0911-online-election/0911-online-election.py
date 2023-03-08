class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        leadingDic = defaultdict(int)
        leadingDic[persons[0]] += 1
        leading = [persons[0]]
        for person in persons[1:]:
            leadingDic[person] += 1
            leading.append(person) if leadingDic[leading[-1]] <= leadingDic[person] else leading.append(leading[-1])
        
        self.persons = persons
        self.times = times
        self.leading = leading
        print(leading)

    def q(self, t: int) -> int:
        low = -1
        high = len(self.times)
        
        while low + 1 < high:
            mid = low + (high - low) // 2
            if self.times[mid] <= t:
                low = mid
            else:
                high = mid
                
        return self.leading[low]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)