class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = []
        for match in matches:
            winners.add(match[0])
            losers.append(match[1])
        losers = Counter(losers)
        
        winnerList = []
        loserList = []
        for winner in winners:
            if winner not in losers:
                winnerList.append(winner)
                
        for loser in losers:
            if losers[loser] == 1:
                loserList.append(loser)
                
        loserList.sort()
        winnerList.sort()
        
        return [winnerList, loserList]
        
