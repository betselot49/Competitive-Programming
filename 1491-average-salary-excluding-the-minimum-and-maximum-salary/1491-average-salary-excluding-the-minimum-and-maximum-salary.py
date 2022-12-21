class Solution:
    def average(self, salary: List[int]) -> float:
        maxi = max(salary[0], salary[1])
        mini = min(salary[0], salary[1])
        curSum = salary[0] + salary[1]
        for i in range(2, len(salary)):
            mini = min(mini, salary[i])
            maxi = max(maxi, salary[i])
            curSum += salary[i]
        curSum -= (maxi + mini)
        return curSum / (len(salary) - 2)
        