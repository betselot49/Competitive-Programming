class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        counter = Counter(guess)
        bulls = set()
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                counter[secret[i]] -= 1
                bulls.add(i)
                
        cows = 0
        for i in range(len(secret)):
            if i in bulls: continue
            if secret[i] in counter and counter[secret[i]] > 0:
                cows += 1
                counter[secret[i]] -= 1
        
        return str(len(bulls)) + "A" + str(cows) + "B"