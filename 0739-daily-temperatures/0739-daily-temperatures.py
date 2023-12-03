class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        idx = 0
        answer = [0] * len(temperatures)
        
        while idx < len(temperatures):
            if not stack or temperatures[stack[-1]] >= temperatures[idx]:
                stack.append(idx)
                idx += 1
            else:
                poppedIdx = stack.pop()
                answer[poppedIdx] = idx - poppedIdx
                
        return answer
                