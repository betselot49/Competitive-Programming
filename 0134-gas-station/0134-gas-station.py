class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        dp = [0] * (len(gas) + 1)
        idx = -1
        min_req = 0
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i] + dp[i]
            if diff >= 0:
                idx = i if idx == -1 else idx
                dp[i+1] = diff
            else:
                min_req += diff
                idx = -1
        if dp[-1] >= abs(min_req): return idx
        return -1
            