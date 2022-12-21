class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        ans = ''
        while i < len(command):
            if command[i] == "(":
                if command[i+1] == ")":
                    ans += "o"
                    i += 2
                else:
                    ans += "al"
                    i += 4
            else:
                ans += "G"
                i += 1
        return ans