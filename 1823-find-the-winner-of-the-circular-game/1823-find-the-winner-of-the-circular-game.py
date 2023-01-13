class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players, pointer = [index+1 for index in range(n)], 0
    
        while len(players) > 1:
            pointer += k - 1
            pointer %= len(players)
            players.pop(pointer)
        
        return players[0]