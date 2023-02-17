class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        p, t, count = 0, 0, 0
       
        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                count += 1
                p += 1
                t += 1
            else:
                t += 1
                
        return count