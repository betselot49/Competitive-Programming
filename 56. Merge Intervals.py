class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]
        i, j = 1, 0
        while i < len(intervals):
            mini, maxi = merged[j][0], merged[j][1]
            if intervals[i][0] <= merged[j][1] and intervals[i][1] >= merged[j][0]:
                mini = min(intervals[i][0], mini)
                maxi = max(intervals[i][1], maxi)
                merged[j] = [mini, maxi]
                i += 1
            else:
                merged.append([intervals[i][0], intervals[i][1]])
                j += 1
                i += 1
        return merged
