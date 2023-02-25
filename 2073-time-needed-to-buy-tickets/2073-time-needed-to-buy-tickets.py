class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        target = tickets[k]
        ind = 0
        while ind <= k:
            count += min(target, tickets[ind])
            ind += 1
            
        target -= 1
        while ind < len(tickets):
            count += min(target, tickets[ind])
            ind += 1
        return count