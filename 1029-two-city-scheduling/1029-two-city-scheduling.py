class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x : x[0] - x[1])
        min_cost, n = 0, len(costs)
        for i in range(n // 2):
            min_cost += costs[i][0] + costs[n-i-1][1]
        return min_cost