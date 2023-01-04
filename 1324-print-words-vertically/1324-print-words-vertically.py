class Solution:
    def printVertically(self, s: str) -> List[str]:
        given = s.split(" ")  # O(N) = where N = 200
        ans, index = [], 0

        while True:  
            space, temp = 0, ""
            for word in given:  # O(N) = where N = 200
                if index < len(word):
                    temp += word[index]
                    space = len(temp)
                else:
                    temp += " "
            if space == 0:
                break
            else:
                ans.append(temp[:space])  # O(M)  Where M = length of the maximim word
                index += 1
        return ans