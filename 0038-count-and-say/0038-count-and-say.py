class Solution:
    def countAndSay(self, n: int) -> str:
        answer = '1'
        for _ in range(n-1):
            curr, temp, count = answer[0], '', 0
            for l in answer:
                if curr == l:
                    count += 1
                else:
                    temp += str(count)+curr
                    curr = l
                    count = 1
            temp += str(count)+curr
            answer = temp
        return answer