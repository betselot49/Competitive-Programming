class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, k, stack = -1, 0, []
        for j in range(len(pushed)):
            if pushed[j] == popped[k]:
                k += 1
                while i > -1 and stack[i] == popped[k]:
                    stack.pop()
                    i -= 1
                    k += 1
            else:
                stack.append(pushed[j])
                i += 1
        return i == -1
