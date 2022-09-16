class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        i = 0
        checked = [-1]
        for index, num in enumerate(citations):
            if num != checked[-1]:
                if num <= len(citations) and num <= len(citations) - index:
                    i = num
                    checked.append(num)
                elif num > len(citations) and i < len(citations) - index <= len(citations):
                    return len(citations) - index
                else:
                    i = max(i, len(citations) - index)
        return i
