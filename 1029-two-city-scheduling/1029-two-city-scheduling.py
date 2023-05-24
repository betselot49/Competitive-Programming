class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # sort based on the cost differnce to go to B rather than A
        costs.sort(key=lambda x : x[0] - x[1])
        n = len(costs)
        running_sum = 0
        for i in range(n//2):
            running_sum += costs[i][0]
            running_sum += costs[n-1-i][1]
        return running_sum