class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        merged = [[position[i], speed[i]] for i in range(len(speed))]
        merged.sort()
        stack = [(target - merged[-1][0]) / merged.pop()[1]]
        while len(merged) != 0:
            time = (target - merged[-1][0]) / merged.pop()[1]
            if stack[-1] < time:
                stack.append(time)
        return len(stack)
