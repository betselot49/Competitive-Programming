class Solution:
    def sortSentence(self, s: str) -> str:
        a = s.split()
        for i in range(len(a)):
            first = i
            for j in range(i + 1, len(a)):
                if int(a[first][len(a[first]) - 1]) > int(a[j][len(a[j]) - 1]):
                    first = j
            temp = a[first][:len(a[first]) - 1]
            a[first], a[i] = a[i], temp
        return " ".join(a)
