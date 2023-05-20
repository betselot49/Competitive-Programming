class Solution:
    def reverseWords(self, s: str) -> str:
        array = s.split(" ")
        answer = []
        for s in array:
            answer.append(s[::-1])
        return " ".join(answer)