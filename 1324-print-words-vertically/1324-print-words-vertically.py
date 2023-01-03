class Solution:
    def printVertically(self, s: str) -> List[str]:
        given = s.split(" ")
        ans, index = [], 0

        while True:
            space, temp = 0, ""
            for word in given:
                if index < len(word):
                    temp += word[index]
                    space = len(temp)
                else:
                    temp += " "
            if space == 0:
                break
            else:
                ans.append(temp[:space])
                index += 1
        return ans