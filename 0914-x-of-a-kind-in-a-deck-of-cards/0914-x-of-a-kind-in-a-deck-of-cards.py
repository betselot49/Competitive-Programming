class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = Counter(deck)
        curr = counter[deck[0]]
        for num in counter.values():
            curr = math.gcd(num, curr)
            if curr == 1:
                return False
        return True
           
        