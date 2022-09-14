class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monStack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while monStack and temperatures[i] > monStack[-1][0]:
                index = monStack.pop()[1]
                answer[index] = i - index
            monStack.append([temperatures[i], i])
        return answer
